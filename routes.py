from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db
from models import FarmPlan
from ml_models import farming_ai
from weather_service import weather_service
from cost_calculator import cost_calculator
import logging

@app.route('/')
def index():
    """Home page with farm planning form"""
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def create_plan():
    """Create a new farm plan with AI recommendations"""
    try:
        # Get form data
        location = request.form.get('location', '').strip()
        area_size = float(request.form.get('area_size', 0))
        budget = float(request.form.get('budget', 0))
        water_availability = request.form.get('water_availability', 'medium')
        light_access = request.form.get('light_access', 'artificial')
        
        # Validate inputs
        if not location:
            flash('Please enter a valid location.', 'error')
            return redirect(url_for('index'))
        
        if area_size <= 0 or budget <= 0:
            flash('Please enter valid area size and budget.', 'error')
            return redirect(url_for('index'))
        
        # Prepare farm parameters
        farm_params = {
            'area_size': area_size,
            'budget': budget,
            'water_availability': water_availability,
            'light_access': light_access
        }
        
        # Get weather data
        weather_data = weather_service.get_weather_data(location)
        if not weather_data:
            flash(f'Could not find weather data for location: {location}', 'error')
            return redirect(url_for('index'))
        
        # Get AI recommendations
        crop_recommendations = farming_ai.recommend_crops(location, farm_params, weather_data)
        
        # Get yield predictions for recommended crops
        detailed_recommendations = []
        for crop in crop_recommendations[:3]:  # Top 3 crops
            yield_data = farming_ai.predict_yield(crop['crop'], farm_params, weather_data)
            crop['yield_data'] = yield_data
            detailed_recommendations.append(crop)
        
        # Calculate costs and ROI
        setup_costs = cost_calculator.calculate_setup_costs(area_size, farm_params)
        operational_costs = cost_calculator.calculate_operational_costs(area_size, farm_params, {'recommendations': detailed_recommendations})
        revenue_projections = cost_calculator.calculate_revenue_projections(detailed_recommendations, area_size)
        roi_analysis = cost_calculator.calculate_roi_analysis(setup_costs, operational_costs, revenue_projections)
        
        # Generate layout suggestions
        layout_suggestions = generate_layout_suggestions(area_size, detailed_recommendations, farm_params)
        
        # Get climate recommendations
        climate_recommendations = weather_service.get_climate_recommendations(weather_data)
        
        # Save to database
        farm_plan = FarmPlan(
            location=location,
            area_size=area_size,
            budget=budget,
            water_availability=water_availability,
            light_access=light_access
        )
        
        farm_plan.set_recommended_crops(detailed_recommendations)
        farm_plan.set_cost_analysis({
            'setup_costs': setup_costs,
            'operational_costs': operational_costs,
            'revenue_projections': revenue_projections,
            'roi_analysis': roi_analysis
        })
        farm_plan.set_layout_suggestions(layout_suggestions)
        farm_plan.set_weather_data(weather_data)
        
        db.session.add(farm_plan)
        db.session.commit()
        
        # Prepare data for template
        plan_data = {
            'plan_id': farm_plan.id,
            'location': location,
            'area_size': area_size,
            'budget': budget,
            'water_availability': water_availability,
            'light_access': light_access,
            'weather_data': weather_data,
            'crop_recommendations': detailed_recommendations,
            'setup_costs': setup_costs,
            'operational_costs': operational_costs,
            'revenue_projections': revenue_projections,
            'roi_analysis': roi_analysis,
            'layout_suggestions': layout_suggestions,
            'climate_recommendations': climate_recommendations
        }
        
        return render_template('plan.html', **plan_data)
        
    except ValueError as e:
        flash('Please enter valid numeric values for area size and budget.', 'error')
        logging.error(f"ValueError in create_plan: {str(e)}")
        return redirect(url_for('index'))
        
    except Exception as e:
        flash('An error occurred while creating your farm plan. Please try again.', 'error')
        logging.error(f"Error in create_plan: {str(e)}")
        return redirect(url_for('index'))

@app.route('/history')
def history():
    """Display user's farm planning history"""
    try:
        # Get all farm plans ordered by creation date
        plans = FarmPlan.query.order_by(FarmPlan.created_at.desc()).limit(20).all()
        
        # Prepare data for template
        plans_data = []
        for plan in plans:
            cost_analysis = plan.get_cost_analysis()
            roi_data = cost_analysis.get('roi_analysis', {}) if cost_analysis else {}
            
            plan_summary = {
                'id': plan.id,
                'location': plan.location,
                'area_size': plan.area_size,
                'budget': plan.budget,
                'created_at': plan.created_at.strftime('%Y-%m-%d %H:%M'),
                'top_crops': [crop['crop'] for crop in plan.get_recommended_crops()[:3]],
                'roi_percentage': roi_data.get('roi_percentage', 0),
                'profitability_status': roi_data.get('profitability_status', 'Unknown')
            }
            plans_data.append(plan_summary)
        
        return render_template('history.html', plans=plans_data)
        
    except Exception as e:
        flash('An error occurred while loading your history.', 'error')
        logging.error(f"Error in history: {str(e)}")
        return render_template('history.html', plans=[])

@app.route('/plan/<int:plan_id>')
def view_plan(plan_id):
    """View a specific farm plan"""
    try:
        plan = FarmPlan.query.get_or_404(plan_id)
        
        # Get all stored data
        crop_recommendations = plan.get_recommended_crops()
        cost_analysis = plan.get_cost_analysis()
        layout_suggestions = plan.get_layout_suggestions()
        weather_data = plan.get_weather_data()
        
        # Get climate recommendations
        climate_recommendations = weather_service.get_climate_recommendations(weather_data) if weather_data else {}
        
        # Prepare data for template
        plan_data = {
            'plan_id': plan.id,
            'location': plan.location,
            'area_size': plan.area_size,
            'budget': plan.budget,
            'water_availability': plan.water_availability,
            'light_access': plan.light_access,
            'weather_data': weather_data,
            'crop_recommendations': crop_recommendations,
            'setup_costs': cost_analysis.get('setup_costs', {}),
            'operational_costs': cost_analysis.get('operational_costs', {}),
            'revenue_projections': cost_analysis.get('revenue_projections', {}),
            'roi_analysis': cost_analysis.get('roi_analysis', {}),
            'layout_suggestions': layout_suggestions,
            'climate_recommendations': climate_recommendations,
            'created_at': plan.created_at.strftime('%Y-%m-%d %H:%M')
        }
        
        return render_template('plan.html', **plan_data)
        
    except Exception as e:
        flash('Plan not found or an error occurred.', 'error')
        logging.error(f"Error in view_plan: {str(e)}")
        return redirect(url_for('history'))

@app.route('/api/weather/<location>')
def api_weather(location):
    """API endpoint to get weather data"""
    try:
        weather_data = weather_service.get_weather_data(location)
        if weather_data:
            return jsonify({'success': True, 'data': weather_data})
        else:
            return jsonify({'success': False, 'error': 'Location not found'}), 404
            
    except Exception as e:
        logging.error(f"API weather error: {str(e)}")
        return jsonify({'success': False, 'error': 'Internal server error'}), 500

@app.route('/api/crops/recommend', methods=['POST'])
def api_crop_recommendations():
    """API endpoint for crop recommendations"""
    try:
        data = request.get_json()
        
        location = data.get('location')
        farm_params = {
            'area_size': float(data.get('area_size', 50)),
            'budget': float(data.get('budget', 5000)),
            'water_availability': data.get('water_availability', 'medium'),
            'light_access': data.get('light_access', 'artificial')
        }
        
        # Get weather data
        weather_data = weather_service.get_weather_data(location)
        if not weather_data:
            return jsonify({'success': False, 'error': 'Location not found'}), 404
        
        # Get recommendations
        recommendations = farming_ai.recommend_crops(location, farm_params, weather_data)
        
        return jsonify({
            'success': True,
            'recommendations': recommendations,
            'weather_data': weather_data
        })
        
    except Exception as e:
        logging.error(f"API crop recommendations error: {str(e)}")
        return jsonify({'success': False, 'error': 'Internal server error'}), 500

def generate_layout_suggestions(area_size, crop_recommendations, farm_params):
    """Generate space-optimized layout suggestions"""
    try:
        layout = {
            'total_area': area_size,
            'vertical_levels': calculate_optimal_levels(area_size),
            'crop_allocation': {},
            'space_efficiency': {},
            'layout_type': determine_layout_type(area_size),
            'infrastructure_requirements': {}
        }
        
        # Calculate crop allocation
        total_crops = len(crop_recommendations)
        if total_crops > 0:
            base_area_per_crop = area_size / total_crops
            
            for i, crop in enumerate(crop_recommendations):
                crop_name = crop['crop']
                confidence = crop.get('confidence', 50) / 100
                
                # Allocate more space to higher confidence crops
                allocated_area = base_area_per_crop * (0.8 + 0.4 * confidence)
                
                layout['crop_allocation'][crop_name] = {
                    'area_sqm': round(allocated_area, 2),
                    'percentage': round((allocated_area / area_size) * 100, 1),
                    'recommended_plants': calculate_plant_count(crop_name, allocated_area),
                    'growing_levels': calculate_crop_levels(crop_name, layout['vertical_levels'])
                }
        
        # Calculate space efficiency metrics
        layout['space_efficiency'] = {
            'plants_per_sqm': calculate_total_plants_per_sqm(layout['crop_allocation']),
            'yield_density': calculate_yield_density(crop_recommendations, area_size),
            'utilization_rate': 95,  # Assuming 95% space utilization
            'walkway_percentage': 15  # 15% for walkways and access
        }
        
        # Infrastructure requirements
        layout['infrastructure_requirements'] = {
            'grow_towers': calculate_grow_towers(area_size, layout['vertical_levels']),
            'led_fixtures': calculate_led_fixtures(area_size, farm_params['light_access']),
            'irrigation_zones': calculate_irrigation_zones(area_size),
            'climate_sensors': calculate_sensors(area_size)
        }
        
        return layout
        
    except Exception as e:
        logging.error(f"Error generating layout suggestions: {str(e)}")
        return {
            'total_area': area_size,
            'vertical_levels': 4,
            'crop_allocation': {},
            'space_efficiency': {},
            'layout_type': 'Standard',
            'infrastructure_requirements': {}
        }

def calculate_optimal_levels(area_size):
    """Calculate optimal number of vertical levels"""
    if area_size < 20:
        return 3
    elif area_size < 50:
        return 4
    elif area_size < 100:
        return 5
    else:
        return 6

def determine_layout_type(area_size):
    """Determine the best layout type for the area"""
    if area_size < 30:
        return "Compact Vertical"
    elif area_size < 100:
        return "Standard Multi-Level"
    else:
        return "Industrial Scale"

def calculate_plant_count(crop_name, area):
    """Calculate number of plants for a crop in given area"""
    plants_per_sqm = {
        'Lettuce': 25,
        'Spinach': 30,
        'Kale': 20,
        'Herbs': 35,
        'Microgreens': 100,
        'Tomatoes': 8,
        'Peppers': 6,
        'Cucumbers': 4
    }
    
    density = plants_per_sqm.get(crop_name, 20)
    return round(density * area)

def calculate_crop_levels(crop_name, total_levels):
    """Calculate how many levels a crop should occupy"""
    crop_level_requirements = {
        'Lettuce': 2,
        'Spinach': 2,
        'Kale': 2,
        'Herbs': 3,
        'Microgreens': 4,
        'Tomatoes': 1,
        'Peppers': 1,
        'Cucumbers': 1
    }
    
    required_levels = crop_level_requirements.get(crop_name, 2)
    return min(required_levels, total_levels)

def calculate_total_plants_per_sqm(crop_allocation):
    """Calculate average plants per square meter across all crops"""
    total_plants = 0
    total_area = 0
    
    for crop_data in crop_allocation.values():
        total_plants += crop_data['recommended_plants']
        total_area += crop_data['area_sqm']
    
    if total_area > 0:
        return round(total_plants / total_area, 1)
    return 0

def calculate_yield_density(crop_recommendations, area_size):
    """Calculate expected yield density (kg per sqm per year)"""
    total_annual_yield = 0
    
    for crop in crop_recommendations:
        yield_data = crop.get('yield_data', {})
        annual_yield = yield_data.get('total_yield_kg', 0) * yield_data.get('harvests_per_year', 1)
        total_annual_yield += annual_yield
    
    if area_size > 0:
        return round(total_annual_yield / area_size, 2)
    return 0

def calculate_grow_towers(area_size, levels):
    """Calculate number of growing towers needed"""
    towers_per_sqm = 0.8  # Assuming 0.8 towers per square meter
    return round(area_size * towers_per_sqm)

def calculate_led_fixtures(area_size, light_access):
    """Calculate LED fixtures needed"""
    if light_access == 'natural':
        fixtures_per_sqm = 0.5
    elif light_access == 'hybrid':
        fixtures_per_sqm = 0.7
    else:
        fixtures_per_sqm = 1.0
    
    return round(area_size * fixtures_per_sqm)

def calculate_irrigation_zones(area_size):
    """Calculate irrigation zones needed"""
    # One zone per 25 square meters
    return max(1, round(area_size / 25))

def calculate_sensors(area_size):
    """Calculate number of climate sensors needed"""
    # One sensor per 20 square meters
    return max(2, round(area_size / 20))

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    db.session.rollback()
    flash('An internal error occurred. Please try again.', 'error')
    return render_template('index.html'), 500
