import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import os
from data.crop_data import get_training_data
import logging

class VerticalFarmingAI:
    """AI models for vertical farming recommendations and predictions"""
    
    def __init__(self):
        self.crop_recommender = None
        self.yield_predictor = None
        self.growth_time_predictor = None
        self.label_encoders = {}
        self.scalers = {}
        self.crop_names = []
        
        # Initialize and train models
        self._train_models()
    
    def _train_models(self):
        """Train all ML models with agricultural data"""
        try:
            # Get training data
            crop_data, yield_data = get_training_data()
            
            # Train crop recommendation model
            self._train_crop_recommender(crop_data)
            
            # Train yield prediction model
            self._train_yield_predictor(yield_data)
            
            logging.info("ML models trained successfully")
            
        except Exception as e:
            logging.error(f"Error training models: {str(e)}")
    
    def _train_crop_recommender(self, crop_data):
        """Train crop recommendation model using Decision Tree"""
        df = pd.DataFrame(crop_data)
        
        # Features for crop recommendation
        features = ['climate_zone', 'water_availability', 'light_access', 
                   'area_size', 'budget_per_sqm', 'temperature', 'humidity']
        
        X = df[features].copy()
        y = df['crop']
        
        # Encode categorical variables
        categorical_features = ['climate_zone', 'water_availability', 'light_access']
        for feature in categorical_features:
            le = LabelEncoder()
            X[feature] = le.fit_transform(X[feature])
            self.label_encoders[feature] = le
        
        # Store unique crop names
        self.crop_names = list(df['crop'].unique())
        
        # Train model
        self.crop_recommender = DecisionTreeClassifier(
            max_depth=10, 
            min_samples_split=5, 
            random_state=42
        )
        self.crop_recommender.fit(X, y)
        
        logging.info(f"Crop recommender trained with {len(df)} samples")
    
    def _train_yield_predictor(self, yield_data):
        """Train yield and growth time prediction models"""
        df = pd.DataFrame(yield_data)
        
        # Features for yield prediction
        features = ['crop', 'area_size', 'light_intensity', 'nutrients_level',
                   'water_frequency', 'temperature', 'humidity', 'co2_level']
        
        X = df[features].copy()
        
        # Encode crop names
        crop_le = LabelEncoder()
        X['crop'] = crop_le.fit_transform(X['crop'])
        self.label_encoders['crop'] = crop_le
        
        # Scale numerical features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        self.scalers['yield_features'] = scaler
        
        # Train yield predictor
        y_yield = df['yield_kg_per_sqm']
        self.yield_predictor = RandomForestRegressor(
            n_estimators=100, 
            random_state=42
        )
        self.yield_predictor.fit(X_scaled, y_yield)
        
        # Train growth time predictor
        y_growth = df['growth_time_days']
        self.growth_time_predictor = RandomForestRegressor(
            n_estimators=100, 
            random_state=42
        )
        self.growth_time_predictor.fit(X_scaled, y_growth)
        
        logging.info(f"Yield predictors trained with {len(df)} samples")
    
    def recommend_crops(self, location_data, farm_params, weather_data):
        """Recommend crops based on farm parameters and weather"""
        try:
            # Prepare input features
            climate_zone = self._determine_climate_zone(weather_data)
            
            features = {
                'climate_zone': climate_zone,
                'water_availability': farm_params['water_availability'],
                'light_access': farm_params['light_access'],
                'area_size': farm_params['area_size'],
                'budget_per_sqm': farm_params['budget'] / farm_params['area_size'],
                'temperature': weather_data.get('temp', 20),
                'humidity': weather_data.get('humidity', 60)
            }
            
            # Encode categorical features
            input_features = []
            for feature_name in ['climate_zone', 'water_availability', 'light_access']:
                if feature_name in self.label_encoders:
                    try:
                        encoded_value = self.label_encoders[feature_name].transform([features[feature_name]])[0]
                        input_features.append(encoded_value)
                    except ValueError:
                        # Handle unknown categories
                        input_features.append(0)
                else:
                    input_features.append(0)
            
            # Add numerical features
            input_features.extend([
                features['area_size'],
                features['budget_per_sqm'],
                features['temperature'],
                features['humidity']
            ])
            
            X = np.array(input_features).reshape(1, -1)
            
            # Get top crop recommendations
            if self.crop_recommender:
                # Get probabilities for all classes
                probabilities = self.crop_recommender.predict_proba(X)[0]
                crop_classes = self.crop_recommender.classes_
                
                # Get top 5 recommendations
                top_indices = np.argsort(probabilities)[-5:][::-1]
                
                recommendations = []
                for idx in top_indices:
                    crop_name = crop_classes[idx]
                    confidence = probabilities[idx]
                    recommendations.append({
                        'crop': crop_name,
                        'confidence': round(confidence * 100, 2),
                        'suitability': self._get_suitability_level(confidence)
                    })
                
                return recommendations
            else:
                return self._get_default_recommendations()
                
        except Exception as e:
            logging.error(f"Error in crop recommendation: {str(e)}")
            return self._get_default_recommendations()
    
    def predict_yield(self, crop, farm_params, weather_data):
        """Predict yield and growth time for a specific crop"""
        try:
            # Prepare features for yield prediction
            features = {
                'crop': crop,
                'area_size': farm_params['area_size'],
                'light_intensity': self._calculate_light_intensity(farm_params['light_access']),
                'nutrients_level': self._estimate_nutrients_level(farm_params['budget']),
                'water_frequency': self._get_water_frequency(farm_params['water_availability']),
                'temperature': weather_data.get('temp', 20),
                'humidity': weather_data.get('humidity', 60),
                'co2_level': 400  # Standard atmospheric CO2
            }
            
            # Encode crop name
            if 'crop' in self.label_encoders:
                try:
                    crop_encoded = self.label_encoders['crop'].transform([features['crop']])[0]
                except ValueError:
                    crop_encoded = 0
            else:
                crop_encoded = 0
            
            # Prepare input array
            input_features = [
                crop_encoded,
                features['area_size'],
                features['light_intensity'],
                features['nutrients_level'],
                features['water_frequency'],
                features['temperature'],
                features['humidity'],
                features['co2_level']
            ]
            
            X = np.array(input_features).reshape(1, -1)
            
            # Scale features
            if 'yield_features' in self.scalers:
                X_scaled = self.scalers['yield_features'].transform(X)
            else:
                X_scaled = X
            
            # Predict yield and growth time
            if self.yield_predictor and self.growth_time_predictor:
                predicted_yield = self.yield_predictor.predict(X_scaled)[0]
                predicted_growth_time = self.growth_time_predictor.predict(X_scaled)[0]
                
                return {
                    'yield_kg_per_sqm': max(0, round(predicted_yield, 2)),
                    'total_yield_kg': max(0, round(predicted_yield * farm_params['area_size'], 2)),
                    'growth_time_days': max(30, round(predicted_growth_time)),
                    'harvests_per_year': max(1, round(365 / max(30, predicted_growth_time), 1))
                }
            else:
                return self._get_default_yield_prediction(crop, farm_params['area_size'])
                
        except Exception as e:
            logging.error(f"Error in yield prediction: {str(e)}")
            return self._get_default_yield_prediction(crop, farm_params['area_size'])
    
    def _determine_climate_zone(self, weather_data):
        """Determine climate zone based on weather data"""
        temp = weather_data.get('temp', 20)
        humidity = weather_data.get('humidity', 60)
        
        if temp < 10:
            return 'cold'
        elif temp < 25:
            if humidity > 70:
                return 'temperate_humid'
            else:
                return 'temperate_dry'
        else:
            if humidity > 70:
                return 'tropical_humid'
            else:
                return 'tropical_dry'
    
    def _calculate_light_intensity(self, light_access):
        """Calculate light intensity based on access type"""
        light_map = {
            'natural': 300,
            'artificial': 400,
            'hybrid': 500
        }
        return light_map.get(light_access, 300)
    
    def _estimate_nutrients_level(self, budget):
        """Estimate nutrients level based on budget"""
        if budget < 1000:
            return 5  # Basic
        elif budget < 5000:
            return 7  # Good
        else:
            return 9  # Premium
    
    def _get_water_frequency(self, water_availability):
        """Convert water availability to frequency"""
        frequency_map = {
            'low': 2,
            'medium': 4,
            'high': 6
        }
        return frequency_map.get(water_availability, 3)
    
    def _get_suitability_level(self, confidence):
        """Convert confidence to suitability level"""
        if confidence > 0.7:
            return 'Excellent'
        elif confidence > 0.5:
            return 'Good'
        elif confidence > 0.3:
            return 'Fair'
        else:
            return 'Poor'
    
    def _get_default_recommendations(self):
        """Default crop recommendations if model fails"""
        return [
            {'crop': 'Lettuce', 'confidence': 85.0, 'suitability': 'Excellent'},
            {'crop': 'Spinach', 'confidence': 80.0, 'suitability': 'Excellent'},
            {'crop': 'Kale', 'confidence': 75.0, 'suitability': 'Good'},
            {'crop': 'Herbs', 'confidence': 70.0, 'suitability': 'Good'},
            {'crop': 'Microgreens', 'confidence': 65.0, 'suitability': 'Good'}
        ]
    
    def _get_default_yield_prediction(self, crop, area_size):
        """Default yield prediction if model fails"""
        base_yields = {
            'Lettuce': 25,
            'Spinach': 20,
            'Kale': 15,
            'Herbs': 10,
            'Microgreens': 30,
            'Tomatoes': 40,
            'Peppers': 35,
            'Cucumbers': 45
        }
        
        base_yield = base_yields.get(crop, 20)
        
        return {
            'yield_kg_per_sqm': base_yield,
            'total_yield_kg': round(base_yield * area_size, 2),
            'growth_time_days': 45,
            'harvests_per_year': 8.1
        }

# Global instance
farming_ai = VerticalFarmingAI()
