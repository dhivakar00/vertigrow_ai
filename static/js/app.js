// VertiGrow AI - Client-side JavaScript functionality

document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    setupFormValidation();
    setupTooltips();
    setupChartDefaults();
    setupAccessibility();
}

// Form validation and enhancement
function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                e.stopPropagation();
            } else {
                showLoadingState(this);
            }
        });
        
        // Real-time validation
        const inputs = form.querySelectorAll('input, select');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                clearValidation(this);
            });
        });
    });
}

function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input[required], select[required]');
    
    inputs.forEach(input => {
        if (!validateField(input)) {
            isValid = false;
        }
    });
    
    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let message = '';
    
    // Required field validation
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        message = 'This field is required';
    }
    
    // Type-specific validation
    if (value && field.type === 'number') {
        const num = parseFloat(value);
        const min = parseFloat(field.min);
        const max = parseFloat(field.max);
        
        if (isNaN(num)) {
            isValid = false;
            message = 'Please enter a valid number';
        } else if (min && num < min) {
            isValid = false;
            message = `Value must be at least ${min}`;
        } else if (max && num > max) {
            isValid = false;
            message = `Value must not exceed ${max}`;
        }
    }
    
    // Email validation
    if (value && field.type === 'email') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            message = 'Please enter a valid email address';
        }
    }
    
    // Location validation
    if (field.name === 'location' && value) {
        if (value.length < 2) {
            isValid = false;
            message = 'Location must be at least 2 characters';
        }
    }
    
    // Apply validation styling
    if (isValid) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
        removeErrorMessage(field);
    } else {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
        showErrorMessage(field, message);
    }
    
    return isValid;
}

function clearValidation(field) {
    field.classList.remove('is-valid', 'is-invalid');
    removeErrorMessage(field);
}

function showErrorMessage(field, message) {
    removeErrorMessage(field);
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    errorDiv.id = field.id + '-error';
    
    field.parentNode.appendChild(errorDiv);
    field.setAttribute('aria-describedby', errorDiv.id);
}

function removeErrorMessage(field) {
    const existingError = field.parentNode.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
        field.removeAttribute('aria-describedby');
    }
}

// Loading states for forms
function showLoadingState(form) {
    const submitButton = form.querySelector('button[type="submit"]');
    if (submitButton) {
        const originalText = submitButton.innerHTML;
        submitButton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Processing...';
        submitButton.disabled = true;
        
        // Store original text for potential restoration
        submitButton.setAttribute('data-original-text', originalText);
    }
}

function hideLoadingState(form) {
    const submitButton = form.querySelector('button[type="submit"]');
    if (submitButton) {
        const originalText = submitButton.getAttribute('data-original-text');
        if (originalText) {
            submitButton.innerHTML = originalText;
            submitButton.disabled = false;
        }
    }
}

// Bootstrap tooltip initialization
function setupTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Chart.js default configuration
function setupChartDefaults() {
    if (typeof Chart !== 'undefined') {
        Chart.defaults.color = '#ffffff';
        Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.1)';
        Chart.defaults.backgroundColor = 'rgba(40, 167, 69, 0.8)';
        
        // Set default font
        Chart.defaults.font.family = "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
        Chart.defaults.font.size = 12;
        
        // Plugin defaults
        Chart.defaults.plugins.legend.labels.usePointStyle = true;
        Chart.defaults.plugins.legend.labels.padding = 20;
    }
}

// Accessibility improvements
function setupAccessibility() {
    // Add ARIA labels to interactive elements
    const buttons = document.querySelectorAll('button:not([aria-label])');
    buttons.forEach(button => {
        const text = button.textContent.trim();
        if (text) {
            button.setAttribute('aria-label', text);
        }
    });
    
    // Improve form field accessibility
    const formFields = document.querySelectorAll('input, select, textarea');
    formFields.forEach(field => {
        const label = document.querySelector(`label[for="${field.id}"]`);
        if (!label && field.placeholder) {
            field.setAttribute('aria-label', field.placeholder);
        }
    });
    
    // Add skip link functionality
    addSkipLinks();
}

function addSkipLinks() {
    const mainContent = document.querySelector('main');
    if (mainContent && !document.querySelector('.skip-link')) {
        const skipLink = document.createElement('a');
        skipLink.href = '#main-content';
        skipLink.className = 'skip-link sr-only';
        skipLink.textContent = 'Skip to main content';
        
        skipLink.addEventListener('focus', function() {
            this.classList.remove('sr-only');
        });
        
        skipLink.addEventListener('blur', function() {
            this.classList.add('sr-only');
        });
        
        document.body.insertBefore(skipLink, document.body.firstChild);
        mainContent.id = 'main-content';
    }
}

// Utility functions for dynamic content updates
function updateWeatherDisplay(weatherData) {
    const weatherContainer = document.querySelector('#weather-display');
    if (!weatherContainer || !weatherData) return;
    
    const html = `
        <div class="row align-items-center">
            <div class="col-md-3 text-center">
                <div class="weather-icon">
                    <i class="fas fa-${getWeatherIcon(weatherData.weather_main)}"></i>
                </div>
                <div class="fs-4 text-info">${weatherData.temp}°C</div>
            </div>
            <div class="col-md-9">
                <h6>${weatherData.location}, ${weatherData.country}</h6>
                <p class="mb-1">${weatherData.weather}</p>
                <div class="row">
                    <div class="col-sm-4">
                        <small class="text-muted">Humidity: ${weatherData.humidity}%</small>
                    </div>
                    <div class="col-sm-4">
                        <small class="text-muted">Wind: ${weatherData.wind_speed} m/s</small>
                    </div>
                    <div class="col-sm-4">
                        <small class="text-muted">Clouds: ${weatherData.clouds}%</small>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    weatherContainer.innerHTML = html;
}

function getWeatherIcon(weatherMain) {
    const iconMap = {
        'Clear': 'sun',
        'Clouds': 'cloud',
        'Rain': 'cloud-rain',
        'Snow': 'snowflake',
        'Thunderstorm': 'bolt',
        'Drizzle': 'cloud-drizzle',
        'Mist': 'smog',
        'Fog': 'smog'
    };
    
    return iconMap[weatherMain] || 'cloud';
}

// Error handling
function showError(message, container = null) {
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-danger alert-dismissible fade show';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    const targetContainer = container || document.querySelector('.container');
    if (targetContainer) {
        targetContainer.insertBefore(alertDiv, targetContainer.firstChild);
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (alertDiv && alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 5000);
    }
}

function showSuccess(message, container = null) {
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-success alert-dismissible fade show';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    const targetContainer = container || document.querySelector('.container');
    if (targetContainer) {
        targetContainer.insertBefore(alertDiv, targetContainer.firstChild);
        
        // Auto-dismiss after 3 seconds
        setTimeout(() => {
            if (alertDiv && alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 3000);
    }
}

// Performance optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Mobile responsiveness helpers
function isMobile() {
    return window.innerWidth <= 768;
}

function isTablet() {
    return window.innerWidth > 768 && window.innerWidth <= 1024;
}

// Initialize responsive behavior
window.addEventListener('resize', debounce(function() {
    // Adjust chart sizes on window resize
    if (typeof Chart !== 'undefined') {
        Chart.helpers.each(Chart.instances, function(instance) {
            instance.resize();
        });
    }
}, 250));

// Export functions for use in other scripts
window.VertiGrowAI = {
    validateForm,
    showError,
    showSuccess,
    updateWeatherDisplay,
    isMobile,
    isTablet,
    debounce
};

// Service worker registration for PWA capabilities (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // Uncomment to enable service worker
        // navigator.serviceWorker.register('/sw.js');
    });
}

console.log('VertiGrow AI - Client application initialized successfully');
