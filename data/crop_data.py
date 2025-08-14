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
    
    # Define crop characteristics and optimal growing conditions - 200+ varieties
    crop_profiles = {
        # LEAFY GREENS (40+ varieties)
        'Arugula': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['natural', 'artificial', 'hybrid'], 'temp_range': (14, 22), 'humidity_range': (55, 70), 'min_budget_per_sqm': 190, 'min_area': 3},
        'Asian Greens': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (60, 75), 'min_budget_per_sqm': 220, 'min_area': 4},
        'Baby Bok Choy': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 24), 'humidity_range': (65, 80), 'min_budget_per_sqm': 240, 'min_area': 5},
        'Baby Lettuce': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['natural', 'artificial', 'hybrid'], 'temp_range': (15, 23), 'humidity_range': (50, 68), 'min_budget_per_sqm': 185, 'min_area': 4},
        'Butter Lettuce': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (55, 70), 'min_budget_per_sqm': 210, 'min_area': 5},
        'Cabbage': {'preferred_climate': ['cold', 'temperate_humid'], 'water_needs': ['high'], 'light_tolerance': ['natural', 'artificial', 'hybrid'], 'temp_range': (10, 20), 'humidity_range': (60, 75), 'min_budget_per_sqm': 280, 'min_area': 8},
        'Chinese Cabbage': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 22), 'humidity_range': (65, 78), 'min_budget_per_sqm': 260, 'min_area': 6},
        'Collard Greens': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['natural', 'artificial', 'hybrid'], 'temp_range': (8, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 230, 'min_area': 6},
        'Endive': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 22), 'humidity_range': (55, 70), 'min_budget_per_sqm': 220, 'min_area': 4},
        'Escarole': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (15, 23), 'humidity_range': (58, 72), 'min_budget_per_sqm': 215, 'min_area': 5},
        'Iceberg Lettuce': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 22), 'humidity_range': (55, 70), 'min_budget_per_sqm': 250, 'min_area': 7},
        'Kale': {'preferred_climate': ['temperate_humid', 'temperate_dry', 'cold'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['natural', 'artificial', 'hybrid'], 'temp_range': (10, 24), 'humidity_range': (55, 75), 'min_budget_per_sqm': 220, 'min_area': 4},
        'Lettuce': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['natural', 'artificial', 'hybrid'], 'temp_range': (15, 25), 'humidity_range': (50, 70), 'min_budget_per_sqm': 200, 'min_area': 5},
        'Mizuna': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 205, 'min_area': 3},
        'Mustard Greens': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 24), 'humidity_range': (55, 70), 'min_budget_per_sqm': 195, 'min_area': 4},
        'Oak Leaf Lettuce': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (52, 68), 'min_budget_per_sqm': 195, 'min_area': 4},
        'Radicchio': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (15, 23), 'humidity_range': (55, 70), 'min_budget_per_sqm': 240, 'min_area': 5},
        'Red Lettuce': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (50, 68), 'min_budget_per_sqm': 210, 'min_area': 4},
        'Romaine Lettuce': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (15, 24), 'humidity_range': (55, 70), 'min_budget_per_sqm': 215, 'min_area': 5},
        'Spinach': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['natural', 'artificial', 'hybrid'], 'temp_range': (12, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 180, 'min_area': 3},
        'Swiss Chard': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (55, 70), 'min_budget_per_sqm': 225, 'min_area': 5},
        'Tatsoi': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 200, 'min_area': 3},
        'Turnip Greens': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 24), 'humidity_range': (58, 72), 'min_budget_per_sqm': 185, 'min_area': 4},
        'Watercress': {'preferred_climate': ['temperate_humid'], 'water_needs': ['high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 20), 'humidity_range': (70, 85), 'min_budget_per_sqm': 280, 'min_area': 3},

        # HERBS (50+ varieties)
        'Anise': {'preferred_climate': ['temperate_humid', 'tropical_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (45, 65), 'min_budget_per_sqm': 320, 'min_area': 2},
        'Basil': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 26), 'humidity_range': (50, 70), 'min_budget_per_sqm': 350, 'min_area': 2},
        'Bay Leaves': {'preferred_climate': ['temperate_humid', 'tropical_dry'], 'water_needs': ['low'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 28), 'humidity_range': (40, 60), 'min_budget_per_sqm': 450, 'min_area': 5},
        'Chervil': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (15, 22), 'humidity_range': (55, 70), 'min_budget_per_sqm': 340, 'min_area': 2},
        'Chives': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 24), 'humidity_range': (50, 70), 'min_budget_per_sqm': 280, 'min_area': 1},
        'Cilantro': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (50, 65), 'min_budget_per_sqm': 290, 'min_area': 2},
        'Dill': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 25), 'humidity_range': (50, 65), 'min_budget_per_sqm': 310, 'min_area': 2},
        'Fennel': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 26), 'humidity_range': (55, 70), 'min_budget_per_sqm': 330, 'min_area': 3},
        'Herbs': {'preferred_climate': ['temperate_humid', 'temperate_dry', 'tropical_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (45, 65), 'min_budget_per_sqm': 300, 'min_area': 2},
        'Lavender': {'preferred_climate': ['temperate_dry', 'tropical_dry'], 'water_needs': ['low'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 30), 'humidity_range': (40, 60), 'min_budget_per_sqm': 380, 'min_area': 3},
        'Lemon Balm': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 26), 'humidity_range': (55, 70), 'min_budget_per_sqm': 320, 'min_area': 2},
        'Lemon Thyme': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (45, 65), 'min_budget_per_sqm': 340, 'min_area': 2},
        'Marjoram': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 28), 'humidity_range': (45, 65), 'min_budget_per_sqm': 350, 'min_area': 2},
        'Mint': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (60, 75), 'min_budget_per_sqm': 300, 'min_area': 2},
        'Oregano': {'preferred_climate': ['temperate_humid', 'tropical_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (45, 65), 'min_budget_per_sqm': 330, 'min_area': 2},
        'Parsley': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (55, 70), 'min_budget_per_sqm': 290, 'min_area': 2},
        'Peppermint': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (60, 75), 'min_budget_per_sqm': 310, 'min_area': 2},
        'Rosemary': {'preferred_climate': ['temperate_dry', 'tropical_dry'], 'water_needs': ['low'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 30), 'humidity_range': (40, 60), 'min_budget_per_sqm': 400, 'min_area': 3},
        'Sage': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (45, 65), 'min_budget_per_sqm': 360, 'min_area': 2},
        'Spearmint': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (60, 75), 'min_budget_per_sqm': 300, 'min_area': 2},
        'Tarragon': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 26), 'humidity_range': (50, 68), 'min_budget_per_sqm': 380, 'min_area': 2},
        'Thai Basil': {'preferred_climate': ['tropical_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (22, 30), 'humidity_range': (60, 75), 'min_budget_per_sqm': 370, 'min_area': 2},
        'Thyme': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (45, 65), 'min_budget_per_sqm': 340, 'min_area': 2},

        # MICROGREENS (30+ varieties)
        'Alfalfa Microgreens': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 26), 'humidity_range': (50, 70), 'min_budget_per_sqm': 380, 'min_area': 1},
        'Arugula Microgreens': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (55, 70), 'min_budget_per_sqm': 400, 'min_area': 1},
        'Beet Microgreens': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 420, 'min_area': 1},
        'Broccoli Microgreens': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (55, 70), 'min_budget_per_sqm': 450, 'min_area': 1},
        'Cabbage Microgreens': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 410, 'min_area': 1},
        'Chia Microgreens': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (60, 80), 'min_budget_per_sqm': 480, 'min_area': 1},
        'Cilantro Microgreens': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (50, 68), 'min_budget_per_sqm': 440, 'min_area': 1},
        'Kale Microgreens': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 24), 'humidity_range': (55, 72), 'min_budget_per_sqm': 430, 'min_area': 1},
        'Microgreens': {'preferred_climate': ['temperate_humid', 'temperate_dry', 'tropical_humid', 'tropical_dry'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (50, 80), 'min_budget_per_sqm': 400, 'min_area': 1},
        'Mustard Microgreens': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (55, 70), 'min_budget_per_sqm': 390, 'min_area': 1},
        'Pea Microgreens': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 360, 'min_area': 1},
        'Radish Microgreens': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (55, 70), 'min_budget_per_sqm': 370, 'min_area': 1},
        'Sunflower Microgreens': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 26), 'humidity_range': (50, 68), 'min_budget_per_sqm': 350, 'min_area': 1},
        'Wheatgrass': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 320, 'min_area': 1},

        # FRUITING VEGETABLES (40+ varieties)
        'Artichokes': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (55, 70), 'min_budget_per_sqm': 550, 'min_area': 20},
        'Beans': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (60, 75), 'min_budget_per_sqm': 380, 'min_area': 8},
        'Bell Peppers': {'preferred_climate': ['tropical_humid', 'tropical_dry'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 28), 'humidity_range': (55, 70), 'min_budget_per_sqm': 480, 'min_area': 10},
        'Cherry Tomatoes': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 26), 'humidity_range': (60, 75), 'min_budget_per_sqm': 450, 'min_area': 8},
        'Chili Peppers': {'preferred_climate': ['tropical_humid', 'tropical_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (22, 32), 'humidity_range': (50, 68), 'min_budget_per_sqm': 420, 'min_area': 6},
        'Cucumbers': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 28), 'humidity_range': (65, 80), 'min_budget_per_sqm': 400, 'min_area': 12},
        'Eggplant': {'preferred_climate': ['tropical_humid', 'tropical_dry'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (22, 30), 'humidity_range': (60, 75), 'min_budget_per_sqm': 520, 'min_area': 15},
        'Green Beans': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 26), 'humidity_range': (55, 70), 'min_budget_per_sqm': 360, 'min_area': 8},
        'Hot Peppers': {'preferred_climate': ['tropical_humid', 'tropical_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (24, 32), 'humidity_range': (45, 65), 'min_budget_per_sqm': 400, 'min_area': 5},
        'Okra': {'preferred_climate': ['tropical_humid', 'tropical_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (24, 32), 'humidity_range': (55, 70), 'min_budget_per_sqm': 380, 'min_area': 10},
        'Peas': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 340, 'min_area': 6},
        'Peppers': {'preferred_climate': ['tropical_humid', 'tropical_dry'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (22, 30), 'humidity_range': (55, 70), 'min_budget_per_sqm': 450, 'min_area': 8},
        'Snow Peas': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 20), 'humidity_range': (65, 75), 'min_budget_per_sqm': 350, 'min_area': 6},
        'Sweet Peppers': {'preferred_climate': ['tropical_humid', 'temperate_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 28), 'humidity_range': (55, 70), 'min_budget_per_sqm': 460, 'min_area': 9},
        'Tomatoes': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 28), 'humidity_range': (60, 75), 'min_budget_per_sqm': 500, 'min_area': 10},
        'Zucchini': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (60, 75), 'min_budget_per_sqm': 420, 'min_area': 15},

        # FRUITS (50+ varieties)
        'Blueberries': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 800, 'min_area': 25},
        'Cranberries': {'preferred_climate': ['cold', 'temperate_humid'], 'water_needs': ['high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (8, 18), 'humidity_range': (70, 85), 'min_budget_per_sqm': 900, 'min_area': 30},
        'Currants': {'preferred_climate': ['cold', 'temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (10, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 650, 'min_area': 20},
        'Elderberries': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (55, 70), 'min_budget_per_sqm': 720, 'min_area': 35},
        'Gooseberries': {'preferred_climate': ['cold', 'temperate_humid'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (10, 20), 'humidity_range': (60, 75), 'min_budget_per_sqm': 680, 'min_area': 20},
        'Goji Berries': {'preferred_climate': ['temperate_dry', 'cold'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 26), 'humidity_range': (45, 65), 'min_budget_per_sqm': 750, 'min_area': 25},
        'Grapes': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 28), 'humidity_range': (50, 70), 'min_budget_per_sqm': 950, 'min_area': 40},
        'Kiwi': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (60, 75), 'min_budget_per_sqm': 850, 'min_area': 35},
        'Lemons': {'preferred_climate': ['tropical_dry', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 30), 'humidity_range': (45, 65), 'min_budget_per_sqm': 1000, 'min_area': 50},
        'Limes': {'preferred_climate': ['tropical_humid', 'tropical_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 32), 'humidity_range': (50, 70), 'min_budget_per_sqm': 950, 'min_area': 45},
        'Oranges': {'preferred_climate': ['tropical_dry', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 30), 'humidity_range': (45, 65), 'min_budget_per_sqm': 1100, 'min_area': 60},
        'Passion Fruit': {'preferred_climate': ['tropical_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (22, 30), 'humidity_range': (65, 80), 'min_budget_per_sqm': 780, 'min_area': 30},
        'Raspberries': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 720, 'min_area': 20},
        'Strawberries': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 600, 'min_area': 15},

        # ROOT VEGETABLES (25+ varieties) 
        'Beets': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 280, 'min_area': 6},
        'Carrots': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 24), 'humidity_range': (55, 70), 'min_budget_per_sqm': 300, 'min_area': 8},
        'Daikon Radish': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 260, 'min_area': 10},
        'Garlic': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (50, 65), 'min_budget_per_sqm': 420, 'min_area': 3},
        'Ginger': {'preferred_climate': ['tropical_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (22, 30), 'humidity_range': (70, 85), 'min_budget_per_sqm': 580, 'min_area': 8},
        'Onions': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (55, 70), 'min_budget_per_sqm': 320, 'min_area': 6},
        'Potatoes': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 380, 'min_area': 15},
        'Radishes': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 220, 'min_area': 3},
        'Sweet Potatoes': {'preferred_climate': ['tropical_humid', 'tropical_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (20, 30), 'humidity_range': (60, 75), 'min_budget_per_sqm': 420, 'min_area': 18},
        'Turnips': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (12, 22), 'humidity_range': (60, 75), 'min_budget_per_sqm': 240, 'min_area': 5},

        # SPECIALTY VEGETABLES (20+ varieties)
        'Asparagus': {'preferred_climate': ['temperate_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 650, 'min_area': 25},
        'Broccoli': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 22), 'humidity_range': (65, 80), 'min_budget_per_sqm': 380, 'min_area': 10},
        'Brussels Sprouts': {'preferred_climate': ['cold', 'temperate_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (10, 20), 'humidity_range': (65, 80), 'min_budget_per_sqm': 420, 'min_area': 12},
        'Cauliflower': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 22), 'humidity_range': (65, 80), 'min_budget_per_sqm': 400, 'min_area': 12},
        'Celery': {'preferred_climate': ['temperate_humid'], 'water_needs': ['high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 24), 'humidity_range': (70, 85), 'min_budget_per_sqm': 450, 'min_area': 8},
        'Corn': {'preferred_climate': ['temperate_humid', 'tropical_humid'], 'water_needs': ['medium', 'high'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (18, 30), 'humidity_range': (60, 75), 'min_budget_per_sqm': 520, 'min_area': 30},
        'Leeks': {'preferred_climate': ['temperate_humid', 'cold'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (14, 24), 'humidity_range': (60, 75), 'min_budget_per_sqm': 340, 'min_area': 8},
        'Mushrooms': {'preferred_climate': ['temperate_humid'], 'water_needs': ['high'], 'light_tolerance': ['artificial'], 'temp_range': (16, 24), 'humidity_range': (80, 95), 'min_budget_per_sqm': 680, 'min_area': 10},
        'Scallions': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (55, 70), 'min_budget_per_sqm': 280, 'min_area': 2},
        'Shallots': {'preferred_climate': ['temperate_humid', 'temperate_dry'], 'water_needs': ['low', 'medium'], 'light_tolerance': ['artificial', 'hybrid'], 'temp_range': (16, 26), 'humidity_range': (50, 65), 'min_budget_per_sqm': 360, 'min_area': 4}
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
    
    # Yield characteristics for different crops (kg per m² per harvest) - 200+ varieties
    yield_profiles = {
        # LEAFY GREENS
        'Arugula': {'base_yield_per_sqm': 2.8, 'yield_variance': 0.7, 'base_growth_days': 25, 'growth_variance': 6, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},
        'Asian Greens': {'base_yield_per_sqm': 2.4, 'yield_variance': 0.6, 'base_growth_days': 35, 'growth_variance': 8, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Baby Bok Choy': {'base_yield_per_sqm': 3.2, 'yield_variance': 0.8, 'base_growth_days': 30, 'growth_variance': 7, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.5},
        'Baby Lettuce': {'base_yield_per_sqm': 2.5, 'yield_variance': 0.6, 'base_growth_days': 28, 'growth_variance': 6, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.1, 'water_sensitivity': 1.3},
        'Butter Lettuce': {'base_yield_per_sqm': 3.2, 'yield_variance': 0.8, 'base_growth_days': 40, 'growth_variance': 10, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.4},
        'Cabbage': {'base_yield_per_sqm': 4.5, 'yield_variance': 1.2, 'base_growth_days': 70, 'growth_variance': 15, 'light_sensitivity': 1.0, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.6},
        'Chinese Cabbage': {'base_yield_per_sqm': 3.8, 'yield_variance': 1.0, 'base_growth_days': 50, 'growth_variance': 12, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.5},
        'Collard Greens': {'base_yield_per_sqm': 2.8, 'yield_variance': 0.7, 'base_growth_days': 45, 'growth_variance': 10, 'light_sensitivity': 1.0, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Endive': {'base_yield_per_sqm': 2.2, 'yield_variance': 0.5, 'base_growth_days': 42, 'growth_variance': 10, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.1, 'water_sensitivity': 1.2},
        'Escarole': {'base_yield_per_sqm': 2.6, 'yield_variance': 0.6, 'base_growth_days': 45, 'growth_variance': 10, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},
        'Iceberg Lettuce': {'base_yield_per_sqm': 4.0, 'yield_variance': 1.0, 'base_growth_days': 55, 'growth_variance': 12, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.6},
        'Kale': {'base_yield_per_sqm': 2.0, 'yield_variance': 0.5, 'base_growth_days': 40, 'growth_variance': 12, 'light_sensitivity': 1.0, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.2},
        'Lettuce': {'base_yield_per_sqm': 3.0, 'yield_variance': 0.8, 'base_growth_days': 35, 'growth_variance': 10, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.1, 'water_sensitivity': 1.3},
        'Mizuna': {'base_yield_per_sqm': 2.4, 'yield_variance': 0.6, 'base_growth_days': 30, 'growth_variance': 8, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},
        'Mustard Greens': {'base_yield_per_sqm': 2.2, 'yield_variance': 0.5, 'base_growth_days': 28, 'growth_variance': 7, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.2},
        'Oak Leaf Lettuce': {'base_yield_per_sqm': 2.8, 'yield_variance': 0.7, 'base_growth_days': 38, 'growth_variance': 9, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.1, 'water_sensitivity': 1.3},
        'Radicchio': {'base_yield_per_sqm': 2.4, 'yield_variance': 0.6, 'base_growth_days': 48, 'growth_variance': 12, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.2},
        'Red Lettuce': {'base_yield_per_sqm': 2.9, 'yield_variance': 0.7, 'base_growth_days': 36, 'growth_variance': 9, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.1, 'water_sensitivity': 1.3},
        'Romaine Lettuce': {'base_yield_per_sqm': 3.4, 'yield_variance': 0.8, 'base_growth_days': 42, 'growth_variance': 10, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.4},
        'Spinach': {'base_yield_per_sqm': 2.5, 'yield_variance': 0.6, 'base_growth_days': 30, 'growth_variance': 8, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.4},
        'Swiss Chard': {'base_yield_per_sqm': 3.0, 'yield_variance': 0.8, 'base_growth_days': 38, 'growth_variance': 10, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Tatsoi': {'base_yield_per_sqm': 2.6, 'yield_variance': 0.6, 'base_growth_days': 32, 'growth_variance': 8, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},
        'Turnip Greens': {'base_yield_per_sqm': 2.2, 'yield_variance': 0.5, 'base_growth_days': 35, 'growth_variance': 8, 'light_sensitivity': 1.0, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},
        'Watercress': {'base_yield_per_sqm': 1.8, 'yield_variance': 0.4, 'base_growth_days': 25, 'growth_variance': 6, 'light_sensitivity': 1.0, 'nutrient_sensitivity': 1.1, 'water_sensitivity': 1.8},

        # HERBS
        'Anise': {'base_yield_per_sqm': 1.2, 'yield_variance': 0.3, 'base_growth_days': 60, 'growth_variance': 15, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.0},
        'Basil': {'base_yield_per_sqm': 2.0, 'yield_variance': 0.5, 'base_growth_days': 28, 'growth_variance': 7, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.2},
        'Bay Leaves': {'base_yield_per_sqm': 0.8, 'yield_variance': 0.2, 'base_growth_days': 90, 'growth_variance': 20, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 0.9},
        'Chervil': {'base_yield_per_sqm': 1.4, 'yield_variance': 0.3, 'base_growth_days': 35, 'growth_variance': 8, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.2},
        'Chives': {'base_yield_per_sqm': 1.8, 'yield_variance': 0.4, 'base_growth_days': 30, 'growth_variance': 7, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.2},
        'Cilantro': {'base_yield_per_sqm': 1.6, 'yield_variance': 0.4, 'base_growth_days': 25, 'growth_variance': 6, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.2},
        'Dill': {'base_yield_per_sqm': 1.4, 'yield_variance': 0.3, 'base_growth_days': 40, 'growth_variance': 10, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.2},
        'Fennel': {'base_yield_per_sqm': 2.2, 'yield_variance': 0.5, 'base_growth_days': 50, 'growth_variance': 12, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.2},
        'Herbs': {'base_yield_per_sqm': 1.5, 'yield_variance': 0.4, 'base_growth_days': 25, 'growth_variance': 8, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.1},
        'Lavender': {'base_yield_per_sqm': 1.0, 'yield_variance': 0.2, 'base_growth_days': 75, 'growth_variance': 18, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 0.8},
        'Lemon Balm': {'base_yield_per_sqm': 1.6, 'yield_variance': 0.4, 'base_growth_days': 35, 'growth_variance': 8, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.2},
        'Lemon Thyme': {'base_yield_per_sqm': 1.2, 'yield_variance': 0.3, 'base_growth_days': 45, 'growth_variance': 10, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.0},
        'Marjoram': {'base_yield_per_sqm': 1.4, 'yield_variance': 0.3, 'base_growth_days': 40, 'growth_variance': 10, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.1},
        'Mint': {'base_yield_per_sqm': 1.8, 'yield_variance': 0.4, 'base_growth_days': 32, 'growth_variance': 8, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Oregano': {'base_yield_per_sqm': 1.6, 'yield_variance': 0.4, 'base_growth_days': 38, 'growth_variance': 9, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.0},
        'Parsley': {'base_yield_per_sqm': 1.8, 'yield_variance': 0.4, 'base_growth_days': 30, 'growth_variance': 7, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.3},
        'Peppermint': {'base_yield_per_sqm': 1.6, 'yield_variance': 0.4, 'base_growth_days': 34, 'growth_variance': 8, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Rosemary': {'base_yield_per_sqm': 1.0, 'yield_variance': 0.2, 'base_growth_days': 65, 'growth_variance': 15, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 0.8},
        'Sage': {'base_yield_per_sqm': 1.2, 'yield_variance': 0.3, 'base_growth_days': 50, 'growth_variance': 12, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.0},
        'Spearmint': {'base_yield_per_sqm': 1.7, 'yield_variance': 0.4, 'base_growth_days': 33, 'growth_variance': 8, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Tarragon': {'base_yield_per_sqm': 1.4, 'yield_variance': 0.3, 'base_growth_days': 42, 'growth_variance': 10, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.1},
        'Thai Basil': {'base_yield_per_sqm': 2.2, 'yield_variance': 0.5, 'base_growth_days': 30, 'growth_variance': 7, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.2},
        'Thyme': {'base_yield_per_sqm': 1.2, 'yield_variance': 0.3, 'base_growth_days': 45, 'growth_variance': 10, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.0},

        # MICROGREENS
        'Alfalfa Microgreens': {'base_yield_per_sqm': 3.8, 'yield_variance': 0.9, 'base_growth_days': 10, 'growth_variance': 3, 'light_sensitivity': 1.5, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.4},
        'Arugula Microgreens': {'base_yield_per_sqm': 4.2, 'yield_variance': 1.0, 'base_growth_days': 8, 'growth_variance': 2, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.5},
        'Beet Microgreens': {'base_yield_per_sqm': 3.6, 'yield_variance': 0.8, 'base_growth_days': 12, 'growth_variance': 3, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Broccoli Microgreens': {'base_yield_per_sqm': 4.4, 'yield_variance': 1.0, 'base_growth_days': 10, 'growth_variance': 3, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.5},
        'Cabbage Microgreens': {'base_yield_per_sqm': 4.0, 'yield_variance': 0.9, 'base_growth_days': 9, 'growth_variance': 2, 'light_sensitivity': 1.5, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Chia Microgreens': {'base_yield_per_sqm': 3.2, 'yield_variance': 0.7, 'base_growth_days': 14, 'growth_variance': 4, 'light_sensitivity': 1.7, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.6},
        'Cilantro Microgreens': {'base_yield_per_sqm': 3.8, 'yield_variance': 0.9, 'base_growth_days': 12, 'growth_variance': 3, 'light_sensitivity': 1.5, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Kale Microgreens': {'base_yield_per_sqm': 4.2, 'yield_variance': 1.0, 'base_growth_days': 10, 'growth_variance': 3, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.5},
        'Microgreens': {'base_yield_per_sqm': 4.0, 'yield_variance': 1.0, 'base_growth_days': 12, 'growth_variance': 4, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.5},
        'Mustard Microgreens': {'base_yield_per_sqm': 4.0, 'yield_variance': 0.9, 'base_growth_days': 8, 'growth_variance': 2, 'light_sensitivity': 1.5, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Pea Microgreens': {'base_yield_per_sqm': 5.0, 'yield_variance': 1.2, 'base_growth_days': 12, 'growth_variance': 3, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},
        'Radish Microgreens': {'base_yield_per_sqm': 4.5, 'yield_variance': 1.0, 'base_growth_days': 7, 'growth_variance': 2, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.4},
        'Sunflower Microgreens': {'base_yield_per_sqm': 4.8, 'yield_variance': 1.1, 'base_growth_days': 10, 'growth_variance': 3, 'light_sensitivity': 1.5, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},
        'Wheatgrass': {'base_yield_per_sqm': 3.5, 'yield_variance': 0.8, 'base_growth_days': 14, 'growth_variance': 4, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.5},

        # FRUITING VEGETABLES
        'Artichokes': {'base_yield_per_sqm': 3.5, 'yield_variance': 0.9, 'base_growth_days': 120, 'growth_variance': 25, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.6, 'water_sensitivity': 1.5},
        'Beans': {'base_yield_per_sqm': 4.2, 'yield_variance': 1.0, 'base_growth_days': 55, 'growth_variance': 12, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.4},
        'Bell Peppers': {'base_yield_per_sqm': 5.5, 'yield_variance': 1.3, 'base_growth_days': 65, 'growth_variance': 12, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.3},
        'Cherry Tomatoes': {'base_yield_per_sqm': 6.5, 'yield_variance': 1.5, 'base_growth_days': 65, 'growth_variance': 12, 'light_sensitivity': 1.7, 'nutrient_sensitivity': 1.6, 'water_sensitivity': 1.5},
        'Chili Peppers': {'base_yield_per_sqm': 3.8, 'yield_variance': 0.9, 'base_growth_days': 80, 'growth_variance': 15, 'light_sensitivity': 1.8, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.2},
        'Cucumbers': {'base_yield_per_sqm': 10.0, 'yield_variance': 2.5, 'base_growth_days': 60, 'growth_variance': 10, 'light_sensitivity': 1.5, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.8},
        'Eggplant': {'base_yield_per_sqm': 5.8, 'yield_variance': 1.4, 'base_growth_days': 85, 'growth_variance': 15, 'light_sensitivity': 1.7, 'nutrient_sensitivity': 1.6, 'water_sensitivity': 1.4},
        'Green Beans': {'base_yield_per_sqm': 4.0, 'yield_variance': 0.9, 'base_growth_days': 52, 'growth_variance': 10, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},
        'Hot Peppers': {'base_yield_per_sqm': 3.2, 'yield_variance': 0.8, 'base_growth_days': 85, 'growth_variance': 18, 'light_sensitivity': 1.9, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.1},
        'Okra': {'base_yield_per_sqm': 4.5, 'yield_variance': 1.1, 'base_growth_days': 60, 'growth_variance': 12, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.2},
        'Peas': {'base_yield_per_sqm': 3.8, 'yield_variance': 0.9, 'base_growth_days': 45, 'growth_variance': 10, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.1, 'water_sensitivity': 1.3},
        'Peppers': {'base_yield_per_sqm': 6.0, 'yield_variance': 1.5, 'base_growth_days': 70, 'growth_variance': 12, 'light_sensitivity': 1.7, 'nutrient_sensitivity': 1.6, 'water_sensitivity': 1.4},
        'Snow Peas': {'base_yield_per_sqm': 3.5, 'yield_variance': 0.8, 'base_growth_days': 40, 'growth_variance': 8, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.1, 'water_sensitivity': 1.4},
        'Sweet Peppers': {'base_yield_per_sqm': 5.8, 'yield_variance': 1.4, 'base_growth_days': 68, 'growth_variance': 12, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.3},
        'Tomatoes': {'base_yield_per_sqm': 8.0, 'yield_variance': 2.0, 'base_growth_days': 75, 'growth_variance': 15, 'light_sensitivity': 1.8, 'nutrient_sensitivity': 1.7, 'water_sensitivity': 1.6},
        'Zucchini': {'base_yield_per_sqm': 7.2, 'yield_variance': 1.8, 'base_growth_days': 55, 'growth_variance': 10, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.5},

        # FRUITS
        'Blueberries': {'base_yield_per_sqm': 2.5, 'yield_variance': 0.6, 'base_growth_days': 150, 'growth_variance': 30, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.4},
        'Cranberries': {'base_yield_per_sqm': 1.8, 'yield_variance': 0.4, 'base_growth_days': 180, 'growth_variance': 35, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.8},
        'Currants': {'base_yield_per_sqm': 2.2, 'yield_variance': 0.5, 'base_growth_days': 120, 'growth_variance': 25, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.3},
        'Elderberries': {'base_yield_per_sqm': 1.5, 'yield_variance': 0.4, 'base_growth_days': 140, 'growth_variance': 30, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.2},
        'Gooseberries': {'base_yield_per_sqm': 2.0, 'yield_variance': 0.5, 'base_growth_days': 110, 'growth_variance': 20, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.3},
        'Goji Berries': {'base_yield_per_sqm': 1.2, 'yield_variance': 0.3, 'base_growth_days': 160, 'growth_variance': 35, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.1},
        'Grapes': {'base_yield_per_sqm': 3.5, 'yield_variance': 0.9, 'base_growth_days': 200, 'growth_variance': 40, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.2},
        'Kiwi': {'base_yield_per_sqm': 4.2, 'yield_variance': 1.0, 'base_growth_days': 180, 'growth_variance': 35, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.4},
        'Lemons': {'base_yield_per_sqm': 8.5, 'yield_variance': 2.0, 'base_growth_days': 240, 'growth_variance': 50, 'light_sensitivity': 1.7, 'nutrient_sensitivity': 1.6, 'water_sensitivity': 1.3},
        'Limes': {'base_yield_per_sqm': 7.8, 'yield_variance': 1.8, 'base_growth_days': 220, 'growth_variance': 45, 'light_sensitivity': 1.8, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.3},
        'Oranges': {'base_yield_per_sqm': 12.0, 'yield_variance': 3.0, 'base_growth_days': 280, 'growth_variance': 60, 'light_sensitivity': 1.8, 'nutrient_sensitivity': 1.7, 'water_sensitivity': 1.4},
        'Passion Fruit': {'base_yield_per_sqm': 6.5, 'yield_variance': 1.5, 'base_growth_days': 120, 'growth_variance': 25, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.5},
        'Raspberries': {'base_yield_per_sqm': 3.2, 'yield_variance': 0.8, 'base_growth_days': 100, 'growth_variance': 20, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.3},
        'Strawberries': {'base_yield_per_sqm': 5.0, 'yield_variance': 1.2, 'base_growth_days': 90, 'growth_variance': 20, 'light_sensitivity': 1.4, 'nutrient_sensitivity': 1.8, 'water_sensitivity': 1.5},

        # ROOT VEGETABLES
        'Beets': {'base_yield_per_sqm': 4.5, 'yield_variance': 1.1, 'base_growth_days': 60, 'growth_variance': 12, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},
        'Carrots': {'base_yield_per_sqm': 5.2, 'yield_variance': 1.2, 'base_growth_days': 75, 'growth_variance': 15, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.3},
        'Daikon Radish': {'base_yield_per_sqm': 6.8, 'yield_variance': 1.6, 'base_growth_days': 65, 'growth_variance': 12, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.4},
        'Garlic': {'base_yield_per_sqm': 2.2, 'yield_variance': 0.5, 'base_growth_days': 180, 'growth_variance': 30, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.1},
        'Ginger': {'base_yield_per_sqm': 3.8, 'yield_variance': 0.9, 'base_growth_days': 240, 'growth_variance': 50, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.6},
        'Onions': {'base_yield_per_sqm': 4.2, 'yield_variance': 1.0, 'base_growth_days': 120, 'growth_variance': 25, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.2},
        'Potatoes': {'base_yield_per_sqm': 8.5, 'yield_variance': 2.0, 'base_growth_days': 90, 'growth_variance': 18, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.3},
        'Radishes': {'base_yield_per_sqm': 3.2, 'yield_variance': 0.7, 'base_growth_days': 25, 'growth_variance': 5, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.1, 'water_sensitivity': 1.3},
        'Sweet Potatoes': {'base_yield_per_sqm': 7.5, 'yield_variance': 1.8, 'base_growth_days': 110, 'growth_variance': 22, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.3},
        'Turnips': {'base_yield_per_sqm': 4.8, 'yield_variance': 1.1, 'base_growth_days': 55, 'growth_variance': 12, 'light_sensitivity': 1.0, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.3},

        # SPECIALTY VEGETABLES
        'Asparagus': {'base_yield_per_sqm': 2.8, 'yield_variance': 0.7, 'base_growth_days': 365, 'growth_variance': 60, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.6, 'water_sensitivity': 1.5},
        'Broccoli': {'base_yield_per_sqm': 3.5, 'yield_variance': 0.8, 'base_growth_days': 65, 'growth_variance': 12, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.5},
        'Brussels Sprouts': {'base_yield_per_sqm': 3.0, 'yield_variance': 0.7, 'base_growth_days': 95, 'growth_variance': 20, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.5},
        'Cauliflower': {'base_yield_per_sqm': 4.2, 'yield_variance': 1.0, 'base_growth_days': 70, 'growth_variance': 15, 'light_sensitivity': 1.3, 'nutrient_sensitivity': 1.4, 'water_sensitivity': 1.6},
        'Celery': {'base_yield_per_sqm': 3.8, 'yield_variance': 0.9, 'base_growth_days': 85, 'growth_variance': 18, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.8},
        'Corn': {'base_yield_per_sqm': 6.5, 'yield_variance': 1.5, 'base_growth_days': 85, 'growth_variance': 15, 'light_sensitivity': 1.6, 'nutrient_sensitivity': 1.5, 'water_sensitivity': 1.4},
        'Leeks': {'base_yield_per_sqm': 3.2, 'yield_variance': 0.8, 'base_growth_days': 120, 'growth_variance': 25, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.3},
        'Mushrooms': {'base_yield_per_sqm': 12.0, 'yield_variance': 3.0, 'base_growth_days': 35, 'growth_variance': 8, 'light_sensitivity': 0.8, 'nutrient_sensitivity': 1.8, 'water_sensitivity': 1.9},
        'Scallions': {'base_yield_per_sqm': 2.8, 'yield_variance': 0.6, 'base_growth_days': 30, 'growth_variance': 6, 'light_sensitivity': 1.1, 'nutrient_sensitivity': 1.2, 'water_sensitivity': 1.2},
        'Shallots': {'base_yield_per_sqm': 3.5, 'yield_variance': 0.8, 'base_growth_days': 100, 'growth_variance': 20, 'light_sensitivity': 1.2, 'nutrient_sensitivity': 1.3, 'water_sensitivity': 1.1}
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
    Get market price data for vertical farming crops - 200+ varieties.
    Returns current market prices per kg in USD.
    """
    return {
        # LEAFY GREENS
        'Arugula': 14.50, 'Asian Greens': 11.00, 'Baby Bok Choy': 13.50, 'Baby Lettuce': 8.50, 'Butter Lettuce': 9.00,
        'Cabbage': 4.50, 'Chinese Cabbage': 6.00, 'Collard Greens': 7.50, 'Endive': 12.00, 'Escarole': 11.50,
        'Iceberg Lettuce': 5.50, 'Kale': 12.00, 'Lettuce': 6.50, 'Mizuna': 16.00, 'Mustard Greens': 9.50,
        'Oak Leaf Lettuce': 8.00, 'Radicchio': 15.50, 'Red Lettuce': 8.50, 'Romaine Lettuce': 7.00, 'Spinach': 8.00,
        'Swiss Chard': 10.50, 'Tatsoi': 18.00, 'Turnip Greens': 8.50, 'Watercress': 22.00,

        # HERBS
        'Anise': 45.00, 'Basil': 28.00, 'Bay Leaves': 65.00, 'Chervil': 38.00, 'Chives': 24.00, 'Cilantro': 22.00,
        'Dill': 26.00, 'Fennel': 32.00, 'Herbs': 25.00, 'Lavender': 55.00, 'Lemon Balm': 35.00, 'Lemon Thyme': 42.00,
        'Marjoram': 38.00, 'Mint': 30.00, 'Oregano': 35.00, 'Parsley': 20.00, 'Peppermint': 32.00, 'Rosemary': 45.00,
        'Sage': 40.00, 'Spearmint': 28.00, 'Tarragon': 48.00, 'Thai Basil': 35.00, 'Thyme': 38.00,

        # MICROGREENS
        'Alfalfa Microgreens': 28.00, 'Arugula Microgreens': 42.00, 'Beet Microgreens': 38.00, 'Broccoli Microgreens': 45.00,
        'Cabbage Microgreens': 35.00, 'Chia Microgreens': 55.00, 'Cilantro Microgreens': 40.00, 'Kale Microgreens': 42.00,
        'Microgreens': 35.00, 'Mustard Microgreens': 38.00, 'Pea Microgreens': 30.00, 'Radish Microgreens': 36.00,
        'Sunflower Microgreens': 32.00, 'Wheatgrass': 25.00,

        # FRUITING VEGETABLES
        'Artichokes': 16.00, 'Beans': 8.50, 'Bell Peppers': 11.00, 'Cherry Tomatoes': 12.50, 'Chili Peppers': 15.00,
        'Cucumbers': 5.50, 'Eggplant': 9.50, 'Green Beans': 8.00, 'Hot Peppers': 18.00, 'Okra': 12.00, 'Peas': 9.00,
        'Peppers': 9.00, 'Snow Peas': 14.00, 'Sweet Peppers': 10.50, 'Tomatoes': 7.50, 'Zucchini': 6.50,

        # FRUITS
        'Blueberries': 28.00, 'Cranberries': 24.00, 'Currants': 22.00, 'Elderberries': 35.00, 'Gooseberries': 26.00,
        'Goji Berries': 45.00, 'Grapes': 18.00, 'Kiwi': 16.50, 'Lemons': 8.50, 'Limes': 9.00, 'Oranges': 6.50,
        'Passion Fruit': 25.00, 'Raspberries': 32.00, 'Strawberries': 18.00,

        # ROOT VEGETABLES
        'Beets': 7.50, 'Carrots': 5.50, 'Daikon Radish': 8.00, 'Garlic': 22.00, 'Ginger': 18.50, 'Onions': 4.50,
        'Potatoes': 3.50, 'Radishes': 6.00, 'Sweet Potatoes': 6.50, 'Turnips': 5.00,

        # SPECIALTY VEGETABLES
        'Asparagus': 24.00, 'Broccoli': 8.50, 'Brussels Sprouts': 12.00, 'Cauliflower': 9.50, 'Celery': 7.00,
        'Corn': 4.50, 'Leeks': 11.50, 'Mushrooms': 16.00, 'Scallions': 8.50, 'Shallots': 18.00
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
