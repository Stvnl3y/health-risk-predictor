"""
UTILITY FUNCTIONS

Helper functions for validation, calculations, and formatting.
"""


def validate_range(value, min_val, max_val, field_name):
    """
    Validate that a value is within a specified range
    
    Args:
        value: Value to check
        min_val: Minimum allowed value
        max_val: Maximum allowed value
        field_name: Name of the field (for error messages)
    
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        val = float(value)
        if val < min_val or val > max_val:
            return False, f"{field_name} must be between {min_val} and {max_val}"
        return True, ""
    except (ValueError, TypeError):
        return False, f"{field_name} must be a valid number"


def validate_required_fields(inputs_dict, required_fields):
    """
    Check that all required fields have values
    
    Args:
        inputs_dict: Dictionary of input values
        required_fields: List of required field names
    
    Returns:
        tuple: (is_valid, missing_fields)
    """
    missing = [field for field in required_fields if not inputs_dict.get(field)]
    return len(missing) == 0, missing


def calculate_bmi(weight_kg, height_cm):
    """
    Calculate Body Mass Index
    
    Args:
        weight_kg: Weight in kilograms
        height_cm: Height in centimeters
    
    Returns:
        float: BMI value
    """
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def format_percentage(value):
    """
    Format a decimal as a percentage
    
    Args:
        value: Decimal value (0-1)
    
    Returns:
        str: Formatted percentage (e.g., "75.5%")
    """
    return f"{value * 100:.1f}%"


# Normal ranges for health parameters
NORMAL_RANGES = {
    'glucose': (70, 100),  # mg/dL (fasting)
    'blood_pressure_systolic': (90, 120),  # mm Hg
    'blood_pressure_diastolic': (60, 80),  # mm Hg
    'bmi': (18.5, 24.9),
    'cholesterol': (125, 200),  # mg/dL
    'heart_rate': (60, 100),  # bpm
}


# Validation ranges (wider than normal, for safety)
VALIDATION_RANGES = {
    'pregnancies': (0, 20),
    'glucose': (40, 300),
    'blood_pressure_systolic': (70, 250),
    'blood_pressure_diastolic': (40, 150),
    'bmi': (10, 70),
    'age': (18, 120),
    'cholesterol': (100, 400),
    'heart_rate': (30, 200),
    'diabetes_pedigree': (0, 2.5),
    'cigarettes_per_day': (0, 100),
}
