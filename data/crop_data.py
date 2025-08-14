"""
Agricultural training data for vertical farming AI models.
Contains realistic data for crop recommendations and yield predictions.
"""

import random
import numpy as np

def get_training_data():
    """
    Generate training datasets for crop recommendation and yield prediction models.
    
    Returns:
        tuple: (crop_data, yield_data) containing training datasets
    """
    
    # Generate crop recommendation training data
    crop_data = generate_crop_recommendation_data()
    
    # Generate yield prediction training data
    yield_data = generate_yield_prediction_data()
    
    return crop_data, yield_data


def generate_crop_recommendation_data():
    """
    Generate training data for crop recommendation model.
    Based on real vertical farming crop suitability data.
    """
    
    # Define crop characteristics and optimal growing conditions
    crop_profiles = {
        'Lettuce': {
            'preferred_climate': ['temperate_humid', 'temperate_dry'],
            'water_needs': ['medium', 'high'],
            'light_tolerance': ['natural', 'artificial', 'hybrid'],
            'temp_range': (15, 25),
            'humidity_range': (50, 70),
            'min_budget_per_sqm': 200,
            'min_area': 5
        },
        'Spinach': {
            'preferred_climate': ['temperate_humid', 'cold'],
            'water_needs': ['medium', 'high'],
            'light_tolerance': ['natural', 'artificial', 'hybrid'],
            'temp_range': (12, 22),
            'humidity_range': (60, 75),
            'min_budget_per_sqm': 180,
            'min_area': 3
        },
        'Kale': {
            'preferred_climate': ['temperate_humid', 'temperate_dry', 'cold'],
            'water_needs': ['medium', 'high'],
            'light_tolerance': ['natural', 'artificial', 'hybrid'],
            'temp_range': (10, 24),
            'humidity_range': (55, 75),
            'min_budget_per_sqm': 220,
            'min_area': 4
        },
        'Herbs': {
            'preferred_climate': ['temperate_humid', 'temperate_dry', 'tropical_dry'],
            'water_needs': ['low', 'medium'],
            'light_tolerance': ['artificial', 'hybrid'],
            'temp_range': (18, 28),
            'humidity_range': (45, 65),
            'min_budget_per_sqm': 300,
            'min_area': 2
        },
        'Microgreens': {
            'preferred_climate': ['temperate_humid', 'temperate_dry', 'tropical_humid', 'tropical_dry'],
            'water_needs': ['medium', 'high'],
            'light_tolerance': ['artificial', 'hybrid'],
            'temp_range': (16, 26),
            'humidity_range': (50, 80),
            'min_budget_per_sqm': 400,
            'min_area': 1
        },
        'Tomatoes': {
            'preferred_climate': ['temperate_humid', 'tropical_humid'],
            'water_needs': ['high'],
            'light_tolerance': ['artificial', 'hybrid'],
            'temp_range': (20, 28),
            'humidity_range': (60, 75),
            'min_budget_per_sqm': 500,
            'min_area': 10
        },
        'Peppers': {
            'preferred_climate': ['tropical_humid', 'tropical_dry'],
            'water_needs': ['medium', 'high'],
            'light_tolerance': ['artificial', 'hybrid'],
            'temp_range': (22, 30),
            'humidity_range': (55, 70),
            'min_budget_per_sqm': 450,
            'min_area': 8
        },
        'Cucumbers': {
            'preferred_climate': ['temperate_humid', 'tropical_humid'],
            'water_needs': ['high'],
            'light_tolerance': ['artificial', 'hybrid'],
            'temp_range': (20, 28),
            'humidity_range': (65, 80),
            'min_budget_per_sqm': 400,
            'min_area': 12
        },
        'Strawberries': {
            'preferred_climate': ['temperate_humid', 'temperate_dry'],
            'water_needs': ['medium', 'high'],
            'light_tolerance': ['artificial', 'hybrid'],
            'temp_range': (16, 24),
            'humidity_range': (60, 75),
            'min_budget_per_sqm': 600,
            'min_area': 15
        },
        'Basil': {
            'preferred_climate': ['temperate_humid', 'tropical_humid'],
            'water_needs': ['medium'],
            'light_tolerance': ['artificial', 'hybrid'],
            'temp_range': (18, 26),
            'humidity_range': (50, 70),
            'min_budget_per_sqm': 350,
            'min_area': 2
        }
    }
    
    climate_zones = ['cold', 'temperate_humid', 'temperate_dry', 'tropical_humid', 'tropical_dry']
    water_levels = ['low', 'medium', 'high']
    light_types = ['natural', 'artificial', 'hybrid']
    
    training_data = []
    
    # Generate training samples for each crop
    for crop, profile in crop_profiles.items():
        # Generate positive examples (suitable conditions)
        for _ in range(50):  # 50 positive examples per crop
            climate = random.choice(profile['preferred_climate'])
            water = random.choice(profile['water_needs'])
            light = random.choice(profile['light_tolerance'])
            
            temp = random.uniform(profile['temp_range'][0], profile['temp_range'][1])
            humidity = random.randint(profile['humidity_range'][0], profile['humidity_range'][1])
            
            area_size = random.uniform(profile['min_area'], 200)
            budget_per_sqm = random.uniform(profile['min_budget_per_sqm'], 1000)
            
            training_data.append({
                'climate_zone': climate,
                'water_availability': water,
                'light_access': light,
                'area_size': area_size,
                'budget_per_sqm': budget_per_sqm,
                'temperature': temp,
                'humidity': humidity,
                'crop': crop
            })
        
        # Generate some negative examples (less suitable conditions)
        for _ in range(15):  # 15 negative examples per crop
            # Choose conditions outside optimal ranges
            climate = random.choice([c for c in climate_zones if c not in profile['preferred_climate']])
            water = random.choice([w for w in water_levels if w not in profile['water_needs']])
            light = 'natural' if 'natural' not in profile['light_tolerance'] else random.choice(light_types)
            
            # Temperature outside optimal range
            if random.choice([True, False]):
                temp = random.uniform(5, profile['temp_range'][0] - 2)
            else:
                temp = random.uniform(profile['temp_range'][1] + 3, 35)
            
            humidity = random.randint(20, 95)
            area_size = random.uniform(1, 300)
            budget_per_sqm = random.uniform(50, profile['min_budget_per_sqm'] * 0.8)
            
            training_data.append({
                'climate_zone': climate,
                'water_availability': water,
                'light_access': light,
                'area_size': area_size,
                'budget_per_sqm': budget_per_sqm,
                'temperature': temp,
                'humidity': humidity,
                'crop': crop
            })
    
    # Add some cross-crop examples for better model generalization
    for _ in range(200):
        crop = random.choice(list(crop_profiles.keys()))
        climate = random.choice(climate_zones)
        water = random.choice(water_levels)
        light = random.choice(light_types)
        temp = random.uniform(5, 35)
        humidity = random.randint(20, 95)
        area_size = random.uniform(1, 500)
        budget_per_sqm = random.uniform(50, 1000)
        
        training_data.append({
            'climate_zone': climate,
            'water_availability': water,
            'light_access': light,
            'area_size': area_size,
            'budget_per_sqm': budget_per_sqm,
            'temperature': temp,
            'humidity': humidity,
            'crop': crop
        })
    
    return training_data


def generate_yield_prediction_data():
    """
    Generate training data for yield prediction models.
    Based on real vertical farming yield data and research.
    """
    
    # Yield characteristics for different crops (kg per m² per harvest)
    yield_profiles = {
        'Lettuce': {
            'base_yield_per_sqm': 3.0,
            'yield_variance': 0.8,
            'base_growth_days': 35,
            'growth_variance': 10,
            'light_sensitivity': 1.2,
            'nutrient_sensitivity': 1.1,
            'water_sensitivity': 1.3
        },
        'Spinach': {
            'base_yield_per_sqm': 2.5,
            'yield_variance': 0.6,
            'base_growth_days': 30,
            'growth_variance': 8,
            'light_sensitivity': 1.1,
            'nutrient_sensitivity': 1.2,
            'water_sensitivity': 1.4
        },
        'Kale': {
            'base_yield_per_sqm': 2.0,
            'yield_variance': 0.5,
            'base_growth_days': 40,
            'growth_variance': 12,
            'light_sensitivity': 1.0,
            'nutrient_sensitivity': 1.3,
            'water_sensitivity': 1.2
        },
        'Herbs': {
            'base_yield_per_sqm': 1.5,
            'yield_variance': 0.4,
            'base_growth_days': 25,
            'growth_variance': 8,
            'light_sensitivity': 1.4,
            'nutrient_sensitivity': 1.5,
            'water_sensitivity': 1.1
        },
        'Microgreens': {
            'base_yield_per_sqm': 4.0,
            'yield_variance': 1.0,
            'base_growth_days': 12,
            'growth_variance': 4,
            'light_sensitivity': 1.6,
            'nutrient_sensitivity': 1.3,
            'water_sensitivity': 1.5
        },
        'Tomatoes': {
            'base_yield_per_sqm': 8.0,
            'yield_variance': 2.0,
            'base_growth_days': 75,
            'growth_variance': 15,
            'light_sensitivity': 1.8,
            'nutrient_sensitivity': 1.7,
            'water_sensitivity': 1.6
        },
        'Peppers': {
            'base_yield_per_sqm': 6.0,
            'yield_variance': 1.5,
            'base_growth_days': 70,
            'growth_variance': 12,
            'light_sensitivity': 1.7,
            'nutrient_sensitivity': 1.6,
            'water_sensitivity': 1.4
        },
        'Cucumbers': {
            'base_yield_per_sqm': 10.0,
            'yield_variance': 2.5,
            'base_growth_days': 60,
            'growth_variance': 10,
            'light_sensitivity': 1.5,
            'nutrient_sensitivity': 1.4,
            'water_sensitivity': 1.8
        },
        'Strawberries': {
            'base_yield_per_sqm': 5.0,
            'yield_variance': 1.2,
            'base_growth_days': 90,
            'growth_variance': 20,
            'light_sensitivity': 1.4,
            'nutrient_sensitivity': 1.8,
            'water_sensitivity': 1.5
        },
        'Basil': {
            'base_yield_per_sqm': 2.0,
            'yield_variance': 0.5,
            'base_growth_days': 28,
            'growth_variance': 7,
            'light_sensitivity': 1.3,
            'nutrient_sensitivity': 1.4,
            'water_sensitivity': 1.2
        }
    }
    
    training_data = []
    
    # Generate training samples for each crop
    for crop, profile in yield_profiles.items():
        for _ in range(100):  # 100 samples per crop
            # Environmental conditions
            area_size = random.uniform(1, 200)
            light_intensity = random.uniform(200, 600)  # PPFD
            nutrients_level = random.randint(1, 10)
            water_frequency = random.randint(1, 8)  # times per day
            temperature = random.uniform(15, 30)
            humidity = random.randint(40, 85)
            co2_level = random.randint(350, 1200)  # ppm
            
            # Calculate yield based on conditions
            base_yield = profile['base_yield_per_sqm']
            
            # Light factor
            optimal_light = 400
            light_factor = 1.0 + profile['light_sensitivity'] * ((light_intensity - optimal_light) / optimal_light)
            light_factor = max(0.3, min(2.0, light_factor))  # Cap between 30% and 200%
            
            # Nutrient factor
            nutrient_factor = 0.5 + (nutrients_level / 10) * 0.7 * profile['nutrient_sensitivity']
            
            # Water factor  
            optimal_water = 4
            water_factor = 1.0 + profile['water_sensitivity'] * ((water_frequency - optimal_water) / optimal_water)
            water_factor = max(0.4, min(1.8, water_factor))
            
            # Temperature factor
            if crop in ['Lettuce', 'Spinach', 'Kale']:
                optimal_temp = 20
            elif crop in ['Herbs', 'Basil', 'Microgreens']:
                optimal_temp = 22
            else:
                optimal_temp = 25
            
            temp_diff = abs(temperature - optimal_temp)
            temp_factor = max(0.5, 1.0 - (temp_diff / 10))
            
            # Humidity factor
            if crop in ['Cucumbers', 'Microgreens']:
                optimal_humidity = 70
            elif crop in ['Herbs', 'Basil']:
                optimal_humidity = 60
            else:
                optimal_humidity = 65
            
            humidity_diff = abs(humidity - optimal_humidity)
            humidity_factor = max(0.6, 1.0 - (humidity_diff / 30))
            
            # CO2 factor
            co2_factor = min(1.5, co2_level / 400)
            
            # Calculate final yield
            yield_modifier = light_factor * nutrient_factor * water_factor * temp_factor * humidity_factor * co2_factor
            predicted_yield = base_yield * yield_modifier
            
            # Add some randomness
            yield_variance = random.uniform(-profile['yield_variance'], profile['yield_variance'])
            final_yield = max(0.1, predicted_yield + yield_variance)
            
            # Calculate growth time
            base_days = profile['base_growth_days']
            
            # Growth time affected by temperature and light
            temp_growth_factor = 1.0 - ((temperature - optimal_temp) / 20)
            temp_growth_factor = max(0.7, min(1.3, temp_growth_factor))
            
            light_growth_factor = max(0.8, min(1.2, optimal_light / light_intensity))
            
            nutrient_growth_factor = max(0.9, min(1.1, 1.0 - (nutrients_level - 5) / 10))
            
            growth_modifier = temp_growth_factor * light_growth_factor * nutrient_growth_factor
            predicted_days = base_days * growth_modifier
            
            # Add growth variance
            growth_variance = random.uniform(-profile['growth_variance'], profile['growth_variance'])
            final_days = max(10, predicted_days + growth_variance)
            
            training_data.append({
                'crop': crop,
                'area_size': area_size,
                'light_intensity': light_intensity,
                'nutrients_level': nutrients_level,
                'water_frequency': water_frequency,
                'temperature': temperature,
                'humidity': humidity,
                'co2_level': co2_level,
                'yield_kg_per_sqm': round(final_yield, 2),
                'growth_time_days': round(final_days)
            })
    
    return training_data


def get_crop_market_data():
    """
    Get market price data for vertical farming crops.
    Returns current market prices per kg in USD.
    """
    return {
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


def get_crop_nutritional_requirements():
    """
    Get nutritional requirements for different crops.
    Returns NPK requirements and optimal pH ranges.
    """
    return {
        'Lettuce': {
            'nitrogen': 150,  # ppm
            'phosphorus': 50,
            'potassium': 200,
            'ph_min': 5.5,
            'ph_max': 6.5
        },
        'Spinach': {
            'nitrogen': 200,
            'phosphorus': 60,
            'potassium': 250,
            'ph_min': 6.0,
            'ph_max': 7.0
        },
        'Kale': {
            'nitrogen': 180,
            'phosphorus': 55,
            'potassium': 220,
            'ph_min': 6.0,
            'ph_max': 7.5
        },
        'Herbs': {
            'nitrogen': 120,
            'phosphorus': 40,
            'potassium': 180,
            'ph_min': 5.5,
            'ph_max': 6.8
        },
        'Microgreens': {
            'nitrogen': 100,
            'phosphorus': 30,
            'potassium': 150,
            'ph_min': 5.5,
            'ph_max': 6.5
        },
        'Tomatoes': {
            'nitrogen': 200,
            'phosphorus': 80,
            'potassium': 300,
            'ph_min': 5.8,
            'ph_max': 6.8
        },
        'Peppers': {
            'nitrogen': 180,
            'phosphorus': 70,
            'potassium': 280,
            'ph_min': 5.8,
            'ph_max': 6.5
        },
        'Cucumbers': {
            'nitrogen': 220,
            'phosphorus': 90,
            'potassium': 350,
            'ph_min': 5.5,
            'ph_max': 6.5
        },
        'Strawberries': {
            'nitrogen': 100,
            'phosphorus': 60,
            'potassium': 200,
            'ph_min': 5.5,
            'ph_max': 6.5
        },
        'Basil': {
            'nitrogen': 150,
            'phosphorus': 50,
            'potassium': 200,
            'ph_min': 5.5,
            'ph_max': 6.5
        }
    }


def get_seasonal_growing_data():
    """
    Get seasonal growing recommendations for vertical farming.
    Returns optimal growing seasons and climate considerations.
    """
    return {
        'Lettuce': {
            'best_seasons': ['spring', 'fall', 'winter'],
            'year_round': True,
            'heat_tolerance': 'low',
            'cold_tolerance': 'high'
        },
        'Spinach': {
            'best_seasons': ['fall', 'winter', 'early_spring'],
            'year_round': True,
            'heat_tolerance': 'low',
            'cold_tolerance': 'very_high'
        },
        'Kale': {
            'best_seasons': ['fall', 'winter', 'spring'],
            'year_round': True,
            'heat_tolerance': 'medium',
            'cold_tolerance': 'very_high'
        },
        'Herbs': {
            'best_seasons': ['spring', 'summer', 'fall'],
            'year_round': True,
            'heat_tolerance': 'high',
            'cold_tolerance': 'medium'
        },
        'Microgreens': {
            'best_seasons': ['all'],
            'year_round': True,
            'heat_tolerance': 'medium',
            'cold_tolerance': 'medium'
        },
        'Tomatoes': {
            'best_seasons': ['spring', 'summer'],
            'year_round': False,
            'heat_tolerance': 'high',
            'cold_tolerance': 'low'
        },
        'Peppers': {
            'best_seasons': ['summer'],
            'year_round': False,
            'heat_tolerance': 'very_high',
            'cold_tolerance': 'very_low'
        },
        'Cucumbers': {
            'best_seasons': ['spring', 'summer'],
            'year_round': False,
            'heat_tolerance': 'high',
            'cold_tolerance': 'low'
        },
        'Strawberries': {
            'best_seasons': ['spring', 'fall'],
            'year_round': False,
            'heat_tolerance': 'medium',
            'cold_tolerance': 'medium'
        },
        'Basil': {
            'best_seasons': ['spring', 'summer'],
            'year_round': True,
            'heat_tolerance': 'high',
            'cold_tolerance': 'low'
        }
    }
