# Overview

VertiGrow AI is a web-based vertical farming planner that leverages artificial intelligence to provide smart crop recommendations, yield predictions, and comprehensive cost analysis for urban vertical farming projects. The application integrates weather data, machine learning models, and economic calculations to help users make informed decisions about their vertical farming ventures.

The system guides users through farm planning by collecting location, area size, budget, and resource availability data, then generates personalized recommendations using AI models trained on agricultural data. It provides detailed cost breakdowns, ROI projections, and layout suggestions to support both novice and experienced vertical farmers.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Framework**: Flask with Jinja2 templating engine for server-side rendering
- **UI Components**: Bootstrap with dark theme for responsive design and consistent styling
- **Client-side Interactivity**: Vanilla JavaScript for form validation, chart rendering with Chart.js, and dynamic user interactions
- **Styling Strategy**: Custom CSS with CSS variables for theming, hover effects for enhanced user experience

## Backend Architecture
- **Web Framework**: Flask application with modular route handling
- **Database ORM**: SQLAlchemy with declarative base model for data persistence
- **Model Design**: Single `FarmPlan` model storing farm parameters and results as JSON for flexible data structure
- **Service Layer**: Separate modules for weather data (`weather_service.py`), cost calculations (`cost_calculator.py`), and ML predictions (`ml_models.py`)

## Machine Learning Architecture
- **Model Types**: Multiple scikit-learn models including Decision Tree for crop recommendations, Random Forest for yield prediction
- **Training Data**: Generated synthetic agricultural data based on real vertical farming characteristics and crop profiles
- **Feature Engineering**: Location-based climate zones, resource availability parameters, and environmental conditions
- **Prediction Pipeline**: Integrated ML workflow that processes user inputs and environmental data to generate recommendations

## Data Storage Solutions
- **Primary Database**: SQLite for development with configurable PostgreSQL support via environment variables
- **Connection Management**: Connection pooling with automatic reconnection and health checks
- **Data Serialization**: JSON storage for complex nested data structures (crop recommendations, cost analysis, yield predictions)
- **Schema Design**: Single-table approach with JSON columns for flexibility and rapid development

## External Service Integration
- **Weather API**: OpenWeather API integration for location-based climate data that influences crop recommendations
- **Environment Configuration**: Environment variable-based configuration for API keys and database connections
- **Error Handling**: Graceful degradation when external services are unavailable

# External Dependencies

## Third-party APIs
- **OpenWeather API**: Provides current weather conditions, temperature, humidity, and other environmental factors used in crop recommendation algorithms

## Python Libraries
- **Web Framework**: Flask, Flask-SQLAlchemy for web application and database management
- **Machine Learning**: scikit-learn for ML models, numpy and pandas for data processing
- **HTTP Requests**: requests library for external API communication
- **Database**: SQLAlchemy ORM with SQLite/PostgreSQL support

## Frontend Dependencies
- **UI Framework**: Bootstrap CSS framework with Replit dark theme
- **Charts**: Chart.js for data visualization and analytics display
- **Icons**: Font Awesome for consistent iconography
- **JavaScript**: Vanilla JavaScript for client-side functionality

## Infrastructure
- **Database**: Configurable between SQLite (development) and PostgreSQL (production)
- **Deployment**: Flask development server with proxy fix middleware for production deployment
- **Environment Management**: Environment variables for sensitive configuration like API keys and database URLs