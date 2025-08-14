from app import db
from datetime import datetime
import json

class FarmPlan(db.Model):
    """Model to store farm planning data and results"""
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    area_size = db.Column(db.Float, nullable=False)  # in square meters
    budget = db.Column(db.Float, nullable=False)  # in USD
    water_availability = db.Column(db.String(50), nullable=False)  # low/medium/high
    light_access = db.Column(db.String(50), nullable=False)  # natural/artificial/hybrid
    
    # Store results as JSON strings
    recommended_crops = db.Column(db.Text)  # JSON string of crop recommendations
    yield_predictions = db.Column(db.Text)  # JSON string of yield predictions
    cost_analysis = db.Column(db.Text)  # JSON string of cost analysis
    layout_suggestions = db.Column(db.Text)  # JSON string of layout recommendations
    
    # Weather data at time of planning
    weather_data = db.Column(db.Text)  # JSON string of weather data
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, location, area_size, budget, water_availability, light_access):
        self.location = location
        self.area_size = area_size
        self.budget = budget
        self.water_availability = water_availability
        self.light_access = light_access
    
    def set_recommended_crops(self, crops_data):
        """Store crop recommendations as JSON"""
        self.recommended_crops = json.dumps(crops_data)
    
    def get_recommended_crops(self):
        """Get crop recommendations from JSON"""
        if self.recommended_crops:
            return json.loads(self.recommended_crops)
        return []
    
    def set_yield_predictions(self, yield_data):
        """Store yield predictions as JSON"""
        self.yield_predictions = json.dumps(yield_data)
    
    def get_yield_predictions(self):
        """Get yield predictions from JSON"""
        if self.yield_predictions:
            return json.loads(self.yield_predictions)
        return {}
    
    def set_cost_analysis(self, cost_data):
        """Store cost analysis as JSON"""
        self.cost_analysis = json.dumps(cost_data)
    
    def get_cost_analysis(self):
        """Get cost analysis from JSON"""
        if self.cost_analysis:
            return json.loads(self.cost_analysis)
        return {}
    
    def set_layout_suggestions(self, layout_data):
        """Store layout suggestions as JSON"""
        self.layout_suggestions = json.dumps(layout_data)
    
    def get_layout_suggestions(self):
        """Get layout suggestions from JSON"""
        if self.layout_suggestions:
            return json.loads(self.layout_suggestions)
        return {}
    
    def set_weather_data(self, weather_data):
        """Store weather data as JSON"""
        self.weather_data = json.dumps(weather_data)
    
    def get_weather_data(self):
        """Get weather data from JSON"""
        if self.weather_data:
            return json.loads(self.weather_data)
        return {}
