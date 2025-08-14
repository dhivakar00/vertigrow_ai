import logging
from typing import Dict, List

class CostCalculator:
    """Calculate costs and ROI for vertical farming operations"""
    
    def __init__(self):
        # Base costs per square meter (USD)
        self.setup_costs = {
            'structure': 200,      # Growing towers/shelving
            'lighting': 150,       # LED grow lights
            'irrigation': 100,     # Hydroponic system
            'climate_control': 120, # HVAC, fans, sensors
            'nutrients': 30,       # Initial nutrients supply
            'seeds': 20,          # Seeds/seedlings
            'automation': 80,     # Basic automation systems
            'installation': 50    # Setup and installation
        }
        
        # Monthly operational costs per square meter
        self.operational_costs = {
            'electricity': 25,     # Power for lights, HVAC
            'water': 5,           # Water consumption
            'nutrients': 8,       # Ongoing nutrients
            'seeds': 6,           # Seed replacement
            'maintenance': 10,    # System maintenance
            'labor': 15          # Labor costs
        }
        
        # Crop-specific market prices (USD per kg)
        self.market_prices = {
            'Lettuce': 6.50,
            'Spinach': 8.00,
            'Kale': 12.00,
            'Herbs': 25.00,
            'Microgreens': 35.00,
            'Tomatoes': 7.50,
            'Peppers': 9.00,
            'Cucumbers': 5.50,
            'Strawberries': 18.00,
            'Basil': 28.00
        }
    
    def calculate_setup_costs(self, area_size: float, farm_params: Dict) -> Dict:
        """Calculate initial setup costs"""
        try:
            base_cost_per_sqm = sum(self.setup_costs.values())
            
            # Apply modifiers based on farm parameters
            modifiers = self._get_setup_cost_modifiers(farm_params)
            adjusted_cost_per_sqm = base_cost_per_sqm * modifiers['total_modifier']
            
            total_setup_cost = adjusted_cost_per_sqm * area_size
            
            # Detailed breakdown
            breakdown = {}
            for component, base_cost in self.setup_costs.items():
                breakdown[component] = round(base_cost * area_size * modifiers['total_modifier'], 2)
            
            return {
                'base_cost_per_sqm': round(base_cost_per_sqm, 2),
                'adjusted_cost_per_sqm': round(adjusted_cost_per_sqm, 2),
                'total_setup_cost': round(total_setup_cost, 2),
                'breakdown': breakdown,
                'modifiers_applied': modifiers
            }
            
        except Exception as e:
            logging.error(f"Error calculating setup costs: {str(e)}")
            return self._get_default_setup_costs(area_size)
    
    def calculate_operational_costs(self, area_size: float, farm_params: Dict, 
                                  crop_data: Dict) -> Dict:
        """Calculate monthly and annual operational costs"""
        try:
            base_monthly_cost_per_sqm = sum(self.operational_costs.values())
            
            # Apply modifiers
            modifiers = self._get_operational_cost_modifiers(farm_params, crop_data)
            adjusted_monthly_cost_per_sqm = base_monthly_cost_per_sqm * modifiers['total_modifier']
            
            monthly_cost = adjusted_monthly_cost_per_sqm * area_size
            annual_cost = monthly_cost * 12
            
            # Detailed breakdown
            monthly_breakdown = {}
            for component, base_cost in self.operational_costs.items():
                monthly_breakdown[component] = round(
                    base_cost * area_size * modifiers['total_modifier'], 2
                )
            
            return {
                'monthly_cost_per_sqm': round(adjusted_monthly_cost_per_sqm, 2),
                'total_monthly_cost': round(monthly_cost, 2),
                'total_annual_cost': round(annual_cost, 2),
                'monthly_breakdown': monthly_breakdown,
                'modifiers_applied': modifiers
            }
            
        except Exception as e:
            logging.error(f"Error calculating operational costs: {str(e)}")
            return self._get_default_operational_costs(area_size)
    
    def calculate_revenue_projections(self, crop_recommendations: List[Dict], 
                                    area_size: float) -> Dict:
        """Calculate projected revenue from recommended crops"""
        try:
            total_annual_revenue = 0
            crop_revenues = {}
            
            for crop_data in crop_recommendations:
                crop_name = crop_data['crop']
                yield_data = crop_data.get('yield_data', {})
                
                # Get yield and harvest frequency
                harvests_per_year = yield_data.get('harvests_per_year', 4)
                yield_per_harvest = yield_data.get('total_yield_kg', 0)
                
                # Calculate annual yield
                annual_yield = yield_per_harvest * harvests_per_year
                
                # Get market price
                market_price = self.market_prices.get(crop_name, 8.00)
                
                # Calculate revenue for this crop
                crop_revenue = annual_yield * market_price
                
                crop_revenues[crop_name] = {
                    'annual_yield_kg': round(annual_yield, 2),
                    'market_price_per_kg': market_price,
                    'annual_revenue': round(crop_revenue, 2),
                    'harvests_per_year': harvests_per_year
                }
                
                total_annual_revenue += crop_revenue
            
            # Calculate average revenue per square meter
            revenue_per_sqm = total_annual_revenue / area_size if area_size > 0 else 0
            
            return {
                'total_annual_revenue': round(total_annual_revenue, 2),
                'revenue_per_sqm': round(revenue_per_sqm, 2),
                'crop_revenues': crop_revenues,
                'projected_monthly_revenue': round(total_annual_revenue / 12, 2)
            }
            
        except Exception as e:
            logging.error(f"Error calculating revenue projections: {str(e)}")
            return {
                'total_annual_revenue': 0,
                'revenue_per_sqm': 0,
                'crop_revenues': {},
                'projected_monthly_revenue': 0
            }
    
    def calculate_roi_analysis(self, setup_costs: Dict, operational_costs: Dict, 
                             revenue_projections: Dict, analysis_years: int = 5) -> Dict:
        """Calculate comprehensive ROI analysis"""
        try:
            initial_investment = setup_costs['total_setup_cost']
            annual_revenue = revenue_projections['total_annual_revenue']
            annual_costs = operational_costs['total_annual_cost']
            annual_profit = annual_revenue - annual_costs
            
            # Calculate payback period
            if annual_profit > 0:
                payback_period = initial_investment / annual_profit
            else:
                payback_period = float('inf')
            
            # Calculate NPV (assuming 8% discount rate)
            discount_rate = 0.08
            npv = -initial_investment
            
            cumulative_cash_flow = [-initial_investment]
            
            for year in range(1, analysis_years + 1):
                discounted_profit = annual_profit / ((1 + discount_rate) ** year)
                npv += discounted_profit
                
                # Track cumulative cash flow
                prev_cash_flow = cumulative_cash_flow[-1]
                current_cash_flow = prev_cash_flow + annual_profit
                cumulative_cash_flow.append(current_cash_flow)
            
            # Calculate ROI percentage
            if initial_investment > 0:
                roi_percentage = ((annual_profit * analysis_years) / initial_investment) * 100
            else:
                roi_percentage = 0
            
            # Calculate profit margins
            if annual_revenue > 0:
                profit_margin = (annual_profit / annual_revenue) * 100
            else:
                profit_margin = 0
            
            return {
                'initial_investment': round(initial_investment, 2),
                'annual_revenue': round(annual_revenue, 2),
                'annual_costs': round(annual_costs, 2),
                'annual_profit': round(annual_profit, 2),
                'payback_period_years': round(payback_period, 2) if payback_period != float('inf') else None,
                'npv': round(npv, 2),
                'roi_percentage': round(roi_percentage, 2),
                'profit_margin': round(profit_margin, 2),
                'cumulative_cash_flow': [round(cf, 2) for cf in cumulative_cash_flow],
                'break_even_month': self._calculate_break_even_month(
                    initial_investment, annual_profit
                ),
                'profitability_status': self._get_profitability_status(roi_percentage, payback_period)
            }
            
        except Exception as e:
            logging.error(f"Error calculating ROI analysis: {str(e)}")
            return self._get_default_roi_analysis()
    
    def _get_setup_cost_modifiers(self, farm_params: Dict) -> Dict:
        """Calculate cost modifiers based on farm parameters"""
        modifiers = {
            'light_modifier': 1.0,
            'water_modifier': 1.0,
            'budget_modifier': 1.0,
            'area_modifier': 1.0
        }
        
        # Light access modifier
        light_access = farm_params.get('light_access', 'artificial')
        if light_access == 'natural':
            modifiers['light_modifier'] = 0.7  # Lower cost, less LED needed
        elif light_access == 'hybrid':
            modifiers['light_modifier'] = 0.85
        else:
            modifiers['light_modifier'] = 1.0
        
        # Water availability modifier
        water_availability = farm_params.get('water_availability', 'medium')
        if water_availability == 'low':
            modifiers['water_modifier'] = 1.3  # More expensive water systems
        elif water_availability == 'high':
            modifiers['water_modifier'] = 0.9
        
        # Area size modifier (economies of scale)
        area_size = farm_params.get('area_size', 50)
        if area_size > 200:
            modifiers['area_modifier'] = 0.85
        elif area_size > 100:
            modifiers['area_modifier'] = 0.95
        elif area_size < 20:
            modifiers['area_modifier'] = 1.2
        
        # Calculate total modifier
        modifiers['total_modifier'] = (
            modifiers['light_modifier'] * 
            modifiers['water_modifier'] * 
            modifiers['area_modifier']
        )
        
        return modifiers
    
    def _get_operational_cost_modifiers(self, farm_params: Dict, crop_data: Dict) -> Dict:
        """Calculate operational cost modifiers"""
        modifiers = {
            'light_modifier': 1.0,
            'crop_modifier': 1.0,
            'efficiency_modifier': 1.0
        }
        
        # Light access affects electricity costs
        light_access = farm_params.get('light_access', 'artificial')
        if light_access == 'natural':
            modifiers['light_modifier'] = 0.6
        elif light_access == 'hybrid':
            modifiers['light_modifier'] = 0.8
        
        # Crop type affects resource consumption
        # High-value crops like herbs typically require more resources
        high_resource_crops = ['Herbs', 'Microgreens', 'Strawberries']
        if any(crop.get('crop', '') in high_resource_crops for crop in crop_data.get('recommendations', [])):
            modifiers['crop_modifier'] = 1.15
        
        # Efficiency modifier based on farm size and setup
        area_size = farm_params.get('area_size', 50)
        if area_size > 100:
            modifiers['efficiency_modifier'] = 0.9  # Better efficiency at scale
        
        modifiers['total_modifier'] = (
            modifiers['light_modifier'] * 
            modifiers['crop_modifier'] * 
            modifiers['efficiency_modifier']
        )
        
        return modifiers
    
    def _calculate_break_even_month(self, initial_investment: float, annual_profit: float) -> int | None:
        """Calculate break-even point in months"""
        if annual_profit <= 0:
            return None
        
        monthly_profit = annual_profit / 12
        break_even_months = initial_investment / monthly_profit
        
        return round(break_even_months)
    
    def _get_profitability_status(self, roi_percentage: float, payback_period: float) -> str:
        """Determine profitability status"""
        if roi_percentage > 25 and payback_period < 3:
            return "Highly Profitable"
        elif roi_percentage > 15 and payback_period < 5:
            return "Profitable"
        elif roi_percentage > 5 and payback_period < 7:
            return "Moderately Profitable"
        elif roi_percentage > 0:
            return "Marginally Profitable"
        else:
            return "Not Profitable"
    
    def _get_default_setup_costs(self, area_size: float) -> Dict:
        """Default setup costs if calculation fails"""
        base_cost = 750 * area_size
        return {
            'base_cost_per_sqm': 750,
            'adjusted_cost_per_sqm': 750,
            'total_setup_cost': base_cost,
            'breakdown': {
                'structure': area_size * 200,
                'lighting': area_size * 150,
                'irrigation': area_size * 100,
                'climate_control': area_size * 120,
                'nutrients': area_size * 30,
                'seeds': area_size * 20,
                'automation': area_size * 80,
                'installation': area_size * 50
            }
        }
    
    def _get_default_operational_costs(self, area_size: float) -> Dict:
        """Default operational costs if calculation fails"""
        monthly_cost = 69 * area_size
        return {
            'monthly_cost_per_sqm': 69,
            'total_monthly_cost': monthly_cost,
            'total_annual_cost': monthly_cost * 12,
            'monthly_breakdown': {
                'electricity': area_size * 25,
                'water': area_size * 5,
                'nutrients': area_size * 8,
                'seeds': area_size * 6,
                'maintenance': area_size * 10,
                'labor': area_size * 15
            }
        }
    
    def _get_default_roi_analysis(self) -> Dict:
        """Default ROI analysis if calculation fails"""
        return {
            'initial_investment': 0,
            'annual_revenue': 0,
            'annual_costs': 0,
            'annual_profit': 0,
            'payback_period_years': None,
            'npv': 0,
            'roi_percentage': 0,
            'profit_margin': 0,
            'cumulative_cash_flow': [0],
            'break_even_month': None,
            'profitability_status': "Analysis Unavailable"
        }

# Global cost calculator instance
cost_calculator = CostCalculator()
