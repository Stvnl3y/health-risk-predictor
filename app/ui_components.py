"""
UI COMPONENTS - CORRECTED VERSION

This module contains all the user interface components for the app.
Each function creates a screen or reusable UI element.

Updates:
- Fixed Yes/No questions to use radio buttons instead of toggles
- Made optional fields (Cholesterol, Glucose, Heart Rate, Cigarettes) with defaults
- Fixed all indentation issues
"""

import flet as ft

# ========================================
# COLOR SCHEME
# ========================================

COLORS = {
    'primary': '#2196F3',      # Blue
    'success': '#4CAF50',      # Green
    'warning': '#FF9800',      # Orange
    'error': '#F44336',        # Red
    'background': '#F5F5F5',   # Light gray
    'text_primary': '#212121', # Dark gray
    'text_secondary': '#757575' # Medium gray
}

# ========================================
# WELCOME SCREEN
# ========================================

def create_welcome_screen(on_get_started):
    """
    Create the welcome/landing screen
    
    Args:
        on_get_started: Callback function when user clicks "Get Started"
    
    Returns:
        Flet Column with welcome screen content
    """
    return ft.Column(
        controls=[
            # Spacer at top
            ft.Container(height=60),
            
            # App icon/logo
            ft.Icon(
                ft.icons.FAVORITE,
                size=100,
                color=COLORS['error']
            ),
            
            # App title
            ft.Text(
                "Health Risk Checker",
                size=32,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                color=COLORS['primary']
            ),
            
            ft.Container(height=10),
            
            # Subtitle
            ft.Text(
                "AI-Powered Health Risk Assessment",
                size=16,
                text_align=ft.TextAlign.CENTER,
                color=COLORS['text_secondary']
            ),
            
            ft.Container(height=20),
            
            # Description
            ft.Container(
                content=ft.Text(
                    "Check your risk for diabetes and hypertension using "
                    "machine learning. Quick, easy, and private.",
                    size=14,
                    text_align=ft.TextAlign.CENTER,
                    color=COLORS['text_secondary']
                ),
                padding=ft.padding.symmetric(horizontal=30)
            ),
            
            ft.Container(height=40),
            
            # Get Started button
            ft.ElevatedButton(
                "Get Started",
                on_click=on_get_started,
                bgcolor=COLORS['primary'],
                color="white",
                height=55,
                width=250,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                )
            ),
            
            ft.Container(height=40),
            
            # Disclaimer
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(
                            ft.icons.INFO_OUTLINE,
                            size=20,
                            color=COLORS['warning']
                        ),
                        ft.Text(
                            "Not a Medical Diagnosis",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            "This tool provides risk estimates only.\n"
                            "Always consult a healthcare provider\n"
                            "for proper medical advice.",
                            size=10,
                            text_align=ft.TextAlign.CENTER,
                            color=COLORS['text_secondary']
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5
                ),
                padding=20,
                bgcolor=COLORS['background'],
                border_radius=10,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=0
    )


# ========================================
# SELECTION SCREEN
# ========================================

def create_selection_screen(on_diabetes, on_hypertension, on_both):
    """
    Create the condition selection screen
    
    Args:
        on_diabetes: Callback for diabetes selection
        on_hypertension: Callback for hypertension selection
        on_both: Callback for both conditions
    
    Returns:
        Flet Column with selection screen
    """
    
    def create_option_card(icon, title, description, color, on_click):
        """Helper to create selection cards"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(icon, size=50, color=color),
                    ft.Container(height=10),
                    ft.Text(
                        title,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        description,
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                        color=COLORS['text_secondary']
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5
            ),
            padding=20,
            border=ft.border.all(2, color),
            border_radius=15,
            on_click=on_click,
            ink=True,  # Ripple effect on click
        )
    
    return ft.Column(
        controls=[
            ft.Container(height=30),
            
            # Header
            ft.Text(
                "What would you like to check?",
                size=24,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            
            ft.Container(height=10),
            
            ft.Text(
                "Select the health condition you want to assess",
                size=14,
                text_align=ft.TextAlign.CENTER,
                color=COLORS['text_secondary']
            ),
            
            ft.Container(height=30),
            
            # Diabetes option
            create_option_card(
                icon=ft.icons.WATER_DROP,
                title="Diabetes Risk",
                description="Check your risk for Type 2 Diabetes",
                color=COLORS['primary'],
                on_click=on_diabetes
            ),
            
            ft.Container(height=15),
            
            # Hypertension option
            create_option_card(
                icon=ft.icons.FAVORITE,
                title="Hypertension Risk",
                description="Check your risk for High Blood Pressure",
                color=COLORS['error'],
                on_click=on_hypertension
            ),
            
            ft.Container(height=15),
            
            # Both option
            create_option_card(
                icon=ft.icons.HEALTH_AND_SAFETY,
                title="Check Both",
                description="Assess both diabetes and hypertension risk",
                color=COLORS['success'],
                on_click=on_both
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
        scroll=ft.ScrollMode.AUTO
    )


# ========================================
# HELPER: Create Input Field
# ========================================

def create_input_field(label, hint, value_ref, input_type='number', min_val=None, max_val=None):
    """
    Create a standardized input field
    
    Args:
        label: Field label
        hint: Hint text
        value_ref: Dictionary to store value
        input_type: 'number' or 'text'
        min_val: Minimum value (for validation)
        max_val: Maximum value (for validation)
    
    Returns:
        Flet TextField
    """
    
    def on_change(e):
        """Store value when user types"""
        value_ref['value'] = e.control.value
    
    return ft.TextField(
        label=label,
        hint_text=hint,
        on_change=on_change,
        keyboard_type=ft.KeyboardType.NUMBER if input_type == 'number' else ft.KeyboardType.TEXT,
        border_color=COLORS['primary'],
        focused_border_color=COLORS['primary'],
    )


# ========================================
# DIABETES FORM
# ========================================

def create_diabetes_form(on_submit, on_back):
    """
    Create diabetes risk assessment form
    
    Args:
        on_submit: Callback when form is submitted (receives input dict)
        on_back: Callback for back button
    
    Returns:
        Flet Column with diabetes form
    """
    
    # Storage for input values
    inputs = {
        'Pregnancies': {'value': ''},
        'Glucose': {'value': ''},
        'BloodPressure': {'value': ''},
        'BMI': {'value': ''},
        'DiabetesPedigreeFunction': {'value': ''},
        'Age': {'value': ''}
    }
    
    # Error message container
    error_text = ft.Text("", color=COLORS['error'], size=12)
    
    def validate_and_submit(e):
        """Validate inputs and submit"""
        errors = []
        
        # Check all fields are filled
        for key, val in inputs.items():
            if not val['value']:
                errors.append(f"{key} is required")
        
        if errors:
            error_text.value = "Please fill in all fields"
            error_text.update()
            return
        
        # Validate ranges
        try:
            pregnancies = float(inputs['Pregnancies']['value'])
            glucose = float(inputs['Glucose']['value'])
            bp = float(inputs['BloodPressure']['value'])
            bmi = float(inputs['BMI']['value'])
            dpf = float(inputs['DiabetesPedigreeFunction']['value'])
            age = float(inputs['Age']['value'])
            
            if not (0 <= pregnancies <= 20):
                errors.append("Pregnancies must be 0-20")
            if not (40 <= glucose <= 300):
                errors.append("Glucose must be 40-300 mg/dL")
            if not (40 <= bp <= 150):
                errors.append("Blood Pressure must be 40-150 mm Hg")
            if not (10 <= bmi <= 70):
                errors.append("BMI must be 10-70")
            if not (0 <= dpf <= 2.5):
                errors.append("Family history must be 0-2.5")
            if not (18 <= age <= 120):
                errors.append("Age must be 18-120 years")
            
        except ValueError:
            errors.append("Please enter valid numbers")
        
        if errors:
            error_text.value = "; ".join(errors)
            error_text.update()
            return
        
        # Submit with values
        submit_data = {key: val['value'] for key, val in inputs.items()}
        on_submit(submit_data)
    
    return ft.Column(
        controls=[
            # Header
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=on_back,
                        icon_color=COLORS['primary']
                    ),
                    ft.Text(
                        "Diabetes Risk Assessment",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                ],
            ),
            
            ft.Divider(),
            
            # Form description
            ft.Text(
                "Please enter your health information below. All fields are required.",
                size=12,
                color=COLORS['text_secondary']
            ),
            
            ft.Container(height=10),
            
            # Input fields
            create_input_field(
                "Number of Pregnancies",
                "0 if male or never pregnant",
                inputs['Pregnancies']
            ),
            
            create_input_field(
                "Fasting Glucose (mg/dL)",
                "Normal: 70-100",
                inputs['Glucose']
            ),
            
            create_input_field(
                "Blood Pressure - Diastolic (mm Hg)",
                "Normal: 60-80",
                inputs['BloodPressure']
            ),
            
            create_input_field(
                "Body Mass Index (BMI)",
                "Normal: 18.5-24.9",
                inputs['BMI']
            ),
            
            create_input_field(
                "Family Diabetes History (0-2)",
                "Higher value = more family history",
                inputs['DiabetesPedigreeFunction']
            ),
            
            create_input_field(
                "Age (years)",
                "18-120",
                inputs['Age']
            ),
            
            ft.Container(height=10),
            
            # Error message
            error_text,
            
            ft.Container(height=10),
            
            # Submit button
            ft.ElevatedButton(
                "Check My Risk",
                on_click=validate_and_submit,
                bgcolor=COLORS['primary'],
                color="white",
                height=50,
                width=300,
            ),
            
            ft.Container(height=20),
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=10
    )


# ========================================
# HYPERTENSION FORM - CORRECTED VERSION
# ========================================

def create_hypertension_form(on_submit, on_back):
    """
    Create hypertension risk assessment form
    
    UPDATES:
    - Yes/No questions now use radio buttons (not toggles)
    - Optional fields: Cholesterol, Glucose, Heart Rate, Cigarettes/day
    - Required fields: Age, Gender, BP, BMI, Smoking Status
    
    Args:
        on_submit: Callback when form is submitted
        on_back: Callback for back button
    
    Returns:
        Flet Column with hypertension form
    """
    
    # Storage for input values
    inputs = {
        'male': {'value': ''},
        'age': {'value': ''},
        'currentSmoker': {'value': ''},
        'cigsPerDay': {'value': ''},
        'BPMeds': {'value': ''},
        'diabetes': {'value': ''},
        'totChol': {'value': ''},
        'sysBP': {'value': ''},
        'diaBP': {'value': ''},
        'BMI': {'value': ''},
        'heartRate': {'value': ''},
        'glucose': {'value': ''}
    }
    
    error_text = ft.Text("", color=COLORS['error'], size=12)
    
    # Gender selection
    def on_gender_change(e):
        inputs['male']['value'] = '1' if e.control.value == "Male" else '0'
    
    gender_radio = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Male", label="Male"),
            ft.Radio(value="Female", label="Female"),
        ]),
        on_change=on_gender_change
    )
    
    # Yes/No radio buttons (FIXED - was toggles before)
    def create_yes_no_field(label, key):
        def on_change(e):
            inputs[key]['value'] = e.control.value
        
        return ft.Container(
            content=ft.Column([
                ft.Text(label, size=14, weight=ft.FontWeight.W_500),
                ft.RadioGroup(
                    content=ft.Row([
                        ft.Radio(value="0", label="No"),
                        ft.Radio(value="1", label="Yes"),
                    ]),
                    on_change=on_change
                )
            ]),
            padding=10,
            bgcolor=COLORS['background'],
            border_radius=5
        )
    
    def validate_and_submit(e):
        """Validate and submit with optional fields"""
        errors = []
        
        # REQUIRED fields only
        required_fields = ['male', 'age', 'currentSmoker', 'sysBP', 'diaBP', 'BMI']
        
        for key in required_fields:
            if not inputs[key]['value']:
                errors.append(f"Please fill in all required fields")
                break
        
        if errors:
            error_text.value = errors[0]
            error_text.update()
            return
        
        # OPTIONAL fields - use defaults if empty
        defaults = {
            'glucose': '90',        # Average fasting glucose
            'totChol': '200',       # Average cholesterol
            'heartRate': '75',      # Average resting heart rate
            'cigsPerDay': '0',      # Default to non-smoker
            'BPMeds': '0',          # Default to not on meds
            'diabetes': '0'         # Default to no diabetes
        }
        
        # Apply defaults for empty optional fields
        for key, default_val in defaults.items():
            if not inputs[key]['value']:
                inputs[key]['value'] = default_val
        
        # Validate ranges for all values
        try:
            age = float(inputs['age']['value'])
            cigs = float(inputs['cigsPerDay']['value'])
            chol = float(inputs['totChol']['value'])
            sys_bp = float(inputs['sysBP']['value'])
            dia_bp = float(inputs['diaBP']['value'])
            bmi = float(inputs['BMI']['value'])
            hr = float(inputs['heartRate']['value'])
            glucose = float(inputs['glucose']['value'])
            
            if not (18 <= age <= 120):
                errors.append("Age must be 18-120")
            if not (0 <= cigs <= 100):
                errors.append("Cigarettes/day must be 0-100")
            if not (100 <= chol <= 400):
                errors.append("Cholesterol must be 100-400 mg/dL")
            if not (70 <= sys_bp <= 250):
                errors.append("Systolic BP must be 70-250")
            if not (40 <= dia_bp <= 150):
                errors.append("Diastolic BP must be 40-150")
            if not (10 <= bmi <= 70):
                errors.append("BMI must be 10-70")
            if not (30 <= hr <= 200):
                errors.append("Heart rate must be 30-200")
            if not (40 <= glucose <= 300):
                errors.append("Glucose must be 40-300")
                
        except ValueError:
            errors.append("Please enter valid numbers")
        
        if errors:
            error_text.value = "; ".join(errors)
            error_text.update()
            return
        
        submit_data = {key: val['value'] for key, val in inputs.items()}
        on_submit(submit_data)
    
    return ft.ListView(
        controls=[
            # Header
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=on_back,
                        icon_color=COLORS['primary']
                    ),
                    ft.Text(
                        "Hypertension Risk Assessment",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                ],
            ),
            
            ft.Divider(),
            
            # Form instructions
            ft.Text(
                "Required fields: Age, Gender, Blood Pressure, BMI, Smoking Status",
                size=11,
                color=COLORS['primary'],
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                "Optional fields will use average values if left blank",
                size=10,
                color=COLORS['text_secondary'],
                italic=True
            ),
            
            ft.Container(height=10),
            
            # Demographics Section
            ft.Text("Demographics", size=16, weight=ft.FontWeight.BOLD, color=COLORS['primary']),
            
            ft.Container(
                content=ft.Column([
                    ft.Text("Gender: *", size=14),
                    gender_radio,
                ]),
                padding=10,
                bgcolor=COLORS['background'],
                border_radius=5
            ),
            
            create_input_field("Age (years) *", "Required: 18-120", inputs['age']),
            
            ft.Container(height=10),
            
            # Lifestyle Section
            ft.Text("Lifestyle", size=16, weight=ft.FontWeight.BOLD, color=COLORS['primary']),
            
            create_yes_no_field("Do you currently smoke? *", 'currentSmoker'),
            create_input_field("Cigarettes per day - Optional", "Leave blank if non-smoker (default: 0)", inputs['cigsPerDay']),
            
            ft.Container(height=10),
            
            # Medical History Section
            ft.Text("Medical History - Optional", size=16, weight=ft.FontWeight.BOLD, color=COLORS['primary']),
            
            create_yes_no_field("Taking blood pressure medication?", 'BPMeds'),
            create_yes_no_field("Have diabetes?", 'diabetes'),
            
            ft.Container(height=10),
            
            # Vital Signs Section
            ft.Text("Vital Signs", size=16, weight=ft.FontWeight.BOLD, color=COLORS['primary']),
            
            create_input_field("Systolic BP (mm Hg) *", "Required - Upper number, normal: 90-120", inputs['sysBP']),
            create_input_field("Diastolic BP (mm Hg) *", "Required - Lower number, normal: 60-80", inputs['diaBP']),
            create_input_field("Resting Heart Rate (bpm) - Optional", "Leave blank if unknown (default: 75)", inputs['heartRate']),
            create_input_field("Body Mass Index (BMI) *", "Required - Normal: 18.5-24.9", inputs['BMI']),
            
            ft.Container(height=10),
            
            # Lab Results Section
            ft.Text("Lab Results - Optional", size=16, weight=ft.FontWeight.BOLD, color=COLORS['primary']),
            
            create_input_field("Total Cholesterol (mg/dL) - Optional", "Leave blank if unknown (default: 200)", inputs['totChol']),
            create_input_field("Fasting Glucose (mg/dL) - Optional", "Leave blank if unknown (default: 90)", inputs['glucose']),
            
            ft.Container(height=10),
            
            error_text,
            
            ft.Container(height=10),
            
            # Submit button
            ft.ElevatedButton(
                "Check My Risk",
                on_click=validate_and_submit,
                bgcolor=COLORS['error'],
                color="white",
                height=50,
                width=300,
            ),
            
            ft.Container(height=20),
        ],
        spacing=10,
        padding=20,
        expand=True
    )


# ========================================
# RESULTS SCREEN
# ========================================

def create_results_screen(results, condition_type, on_learn_more, on_reset):
    """
    Create results display screen
    
    Args:
        results: Dictionary with prediction results
        condition_type: 'diabetes' or 'hypertension'
        on_learn_more: Callback for educational content
        on_reset: Callback for reset button
    
    Returns:
        Flet Column with results
    """
    
    # Determine color based on risk level
    if results['risk_level'] == 'Low':
        risk_color = COLORS['success']
        risk_icon = ft.icons.CHECK_CIRCLE
    elif results['risk_level'] == 'Moderate':
        risk_color = COLORS['warning']
        risk_icon = ft.icons.WARNING
    else:
        risk_color = COLORS['error']
        risk_icon = ft.icons.ERROR
    
    # Condition title
    condition_title = "Diabetes" if condition_type == 'diabetes' else "Hypertension"
    
    return ft.ListView(
        controls=[
            ft.Container(height=20),
            
            # Header
            ft.Text(
                f"{condition_title} Risk Assessment",
                size=24,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            
            ft.Container(height=20),
            
            # Risk level indicator
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(risk_icon, size=80, color=risk_color),
                        ft.Text(
                            f"{results['risk_level'].upper()} RISK",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                            color=risk_color,
                            text_align=ft.TextAlign.CENTER
                        ),
                        ft.Text(
                            f"Probability: {results['probability']}%",
                            size=16,
                            text_align=ft.TextAlign.CENTER,
                            color=COLORS['text_secondary']
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                padding=30,
                bgcolor=COLORS['background'],
                border_radius=15,
            ),
            
            ft.Container(height=20),
            
            # Contributing factors
            ft.Text(
                "Key Factors:",
                size=16,
                weight=ft.FontWeight.BOLD
            ),
            
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row([
                            ft.Icon(ft.icons.FIBER_MANUAL_RECORD, size=8),
                            ft.Text(factor, size=12)
                        ]) for factor in results['top_factors']
                    ],
                    spacing=5
                ),
                padding=15,
                bgcolor=COLORS['background'],
                border_radius=10,
            ),
            
            ft.Container(height=20),
            
            # Recommendations
            ft.Text(
                "Recommendations:",
                size=16,
                weight=ft.FontWeight.BOLD
            ),
            
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(rec, size=12) for rec in results['recommendations']
                    ],
                    spacing=8
                ),
                padding=15,
                bgcolor=COLORS['background'],
                border_radius=10,
            ),
            
            ft.Container(height=30),
            
            # Action buttons
            ft.ElevatedButton(
                "Learn More About " + condition_title,
                on_click=on_learn_more,
                bgcolor=COLORS['primary'],
                color="white",
                width=300,
                height=45
            ),
            
            ft.OutlinedButton(
                "Reset & Start Over",
                on_click=on_reset,
                width=300,
                height=45
            ),
            
            ft.Container(height=30),
            
            # Screenshot tip
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.icons.CAMERA_ALT, size=16, color=COLORS['text_secondary']),
                        ft.Text(
                            "Tip: Take a screenshot to save your results",
                            size=11,
                            color=COLORS['text_secondary'],
                            italic=True
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ),
            
            ft.Container(height=20),
        ],
        spacing=0,
        padding=20,
        expand=True
    )


# ========================================
# EDUCATIONAL SCREEN
# ========================================

def create_educational_screen(condition_type, on_back):
    """
    Create educational content screen
    
    Args:
        condition_type: 'diabetes' or 'hypertension'
        on_back: Callback for back button
    
    Returns:
        Flet Column with educational content
    """
    
    if condition_type == 'diabetes':
        title = "About Diabetes"
        icon = ft.icons.WATER_DROP
        color = COLORS['primary']
        
        content = [
            ("What is Diabetes?", 
             "Diabetes is a chronic condition where your body cannot properly process blood sugar (glucose). "
             "Type 2 diabetes, the most common form, occurs when your body becomes resistant to insulin or "
             "doesn't produce enough insulin."),
            
            ("Risk Factors",
             "• Being overweight or obese\n"
             "• Family history of diabetes\n"
             "• Age over 45\n"
             "• Lack of physical activity\n"
             "• High blood pressure\n"
             "• Unhealthy diet high in sugar and processed foods"),
            
            ("Prevention",
             "• Maintain a healthy weight\n"
             "• Exercise regularly (150 minutes/week)\n"
             "• Eat a balanced diet rich in vegetables and whole grains\n"
             "• Limit sugar and refined carbohydrates\n"
             "• Get regular health checkups\n"
             "• Manage stress levels"),
            
            ("When to See a Doctor",
             "Consult a healthcare provider if you experience:\n"
             "• Increased thirst and urination\n"
             "• Unexplained weight loss\n"
             "• Extreme fatigue\n"
             "• Blurred vision\n"
             "• Slow-healing sores\n"
             "• Frequent infections"),
        ]
    else:  # hypertension
        title = "About Hypertension"
        icon = ft.icons.FAVORITE
        color = COLORS['error']
        
        content = [
            ("What is Hypertension?",
             "Hypertension (high blood pressure) occurs when the force of blood against artery walls is "
             "consistently too high. It's often called the 'silent killer' because it usually has no symptoms "
             "but can lead to serious health problems."),
            
            ("Risk Factors",
             "• Family history of high blood pressure\n"
             "• Age (risk increases with age)\n"
             "• Being overweight or obese\n"
             "• Lack of physical activity\n"
             "• High sodium diet\n"
             "• Smoking and alcohol use\n"
             "• Chronic stress"),
            
            ("Prevention",
             "• Maintain a healthy weight\n"
             "• Exercise regularly\n"
             "• Reduce sodium intake (less than 2,300mg/day)\n"
             "• Eat a heart-healthy diet (DASH diet)\n"
             "• Limit alcohol consumption\n"
             "• Don't smoke\n"
             "• Manage stress\n"
             "• Get adequate sleep"),
            
            ("When to See a Doctor",
             "See a healthcare provider if:\n"
             "• Blood pressure readings are consistently 140/90 or higher\n"
             "• You have severe headaches\n"
             "• You experience chest pain\n"
             "• You have difficulty breathing\n"
             "• You notice irregular heartbeat\n"
             "• You have a family history of heart disease"),
        ]
    
    return ft.ListView(
        controls=[
            # Header
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=on_back,
                        icon_color=color
                    ),
                    ft.Text(
                        title,
                        size=24,
                        weight=ft.FontWeight.BOLD
                    ),
                ],
            ),
            
            ft.Divider(),
            
            ft.Container(height=10),
            
            # Icon
            ft.Icon(icon, size=60, color=color),
            
            ft.Container(height=20),
            
            # Content sections
            *[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                section_title,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=color
                            ),
                            ft.Text(
                                section_content,
                                size=13,
                                color=COLORS['text_secondary']
                            ),
                        ],
                        spacing=10
                    ),
                    padding=15,
                    bgcolor=COLORS['background'],
                    border_radius=10,
                    margin=ft.margin.only(bottom=15)
                )
                for section_title, section_content in content
            ],
            
            # Disclaimer
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(ft.icons.INFO, size=20, color=COLORS['warning']),
                        ft.Text(
                            "This information is for educational purposes only and should not "
                            "replace professional medical advice. Always consult with a qualified "
                            "healthcare provider for diagnosis and treatment.",
                            size=11,
                            text_align=ft.TextAlign.CENTER,
                            color=COLORS['text_secondary'],
                            italic=True
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                padding=20,
                bgcolor=COLORS['background'],
                border_radius=10,
            ),
            
            ft.Container(height=20),
        ],
        spacing=0,
        padding=20,
        expand=True
    )