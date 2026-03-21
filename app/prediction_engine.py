"""
PREDICTION ENGINE - MOBILE OPTIMIZED VERSION

Handles loading ML models and making predictions.
Uses numpy arrays instead of pandas DataFrames for Android compatibility.
"""

import joblib
import numpy as np
import os
import warnings

# Suppress sklearn feature name warnings (expected when using numpy arrays)
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')


class PredictionEngine:
    """Engine for loading models and making predictions"""

    def __init__(self):
        """Initialize and load models"""
        self.models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
        self.load_models()

    def load_models(self):
        """Load all trained models and scalers"""
        try:
            # Diabetes
            self.diabetes_model = joblib.load(os.path.join(self.models_dir, 'diabetes_model.pkl'))
            self.diabetes_scaler = joblib.load(os.path.join(self.models_dir, 'scaler_diabetes.pkl'))
            print("✓ Diabetes model loaded successfully")

            # Hypertension
            self.hypertension_model = joblib.load(os.path.join(self.models_dir, 'hypertension_model.pkl'))
            self.hypertension_scaler = joblib.load(os.path.join(self.models_dir, 'scaler_hypertension.pkl'))
            print("✓ Hypertension model loaded successfully")

        except Exception as e:
            print(f"❌ Error loading models: {e}")
            raise

    def predict_diabetes(self, user_inputs):
        """Make diabetes risk prediction

        Args:
            user_inputs: Dict with 6 features

        Returns:
            Dict with prediction results
        """
        # Feature order MUST match training order
        features = np.array([[
            float(user_inputs['Pregnancies']),
            float(user_inputs['Glucose']),
            float(user_inputs['BloodPressure']),
            float(user_inputs['BMI']),
            float(user_inputs['DiabetesPedigreeFunction']),
            float(user_inputs['Age'])
        ]], dtype=np.float64)

        # Scale and predict
        features_scaled = self.diabetes_scaler.transform(features)
        prediction = self.diabetes_model.predict(features_scaled)[0]
        probability = self.diabetes_model.predict_proba(features_scaled)[0][1]

        # Determine risk level
        if probability < 0.30:
            risk_level, risk_color = 'Low', 'success'
        elif probability < 0.60:
            risk_level, risk_color = 'Moderate', 'warning'
        else:
            risk_level, risk_color = 'High', 'error'

        return {
            'risk_level': risk_level,
            'risk_color': risk_color,
            'probability': round(probability * 100, 1),
            'prediction': int(prediction),
            'confidence': self._get_confidence_description(probability),
            'top_factors': self._get_diabetes_top_factors(user_inputs),
            'recommendations': self._get_diabetes_recommendations(risk_level, user_inputs)
        }

    def predict_hypertension(self, user_inputs):
        """Make hypertension risk prediction

        Args:
            user_inputs: Dict with 12 features

        Returns:
            Dict with prediction results
        """
        # Feature order MUST match training order
        features = np.array([[
            float(user_inputs['male']),
            float(user_inputs['age']),
            float(user_inputs['currentSmoker']),
            float(user_inputs['cigsPerDay']),
            float(user_inputs['BPMeds']),
            float(user_inputs['diabetes']),
            float(user_inputs['totChol']),
            float(user_inputs['sysBP']),
            float(user_inputs['diaBP']),
            float(user_inputs['BMI']),
            float(user_inputs['heartRate']),
            float(user_inputs['glucose'])
        ]], dtype=np.float64)

        # Scale and predict
        features_scaled = self.hypertension_scaler.transform(features)
        prediction = self.hypertension_model.predict(features_scaled)[0]
        probability = self.hypertension_model.predict_proba(features_scaled)[0][1]

        # Determine risk level
        if probability < 0.30:
            risk_level, risk_color = 'Low', 'success'
        elif probability < 0.60:
            risk_level, risk_color = 'Moderate', 'warning'
        else:
            risk_level, risk_color = 'High', 'error'

        return {
            'risk_level': risk_level,
            'risk_color': risk_color,
            'probability': round(probability * 100, 1),
            'prediction': int(prediction),
            'confidence': self._get_confidence_description(probability),
            'top_factors': self._get_hypertension_top_factors(user_inputs),
            'recommendations': self._get_hypertension_recommendations(risk_level, user_inputs)
        }

    def _get_diabetes_top_factors(self, inputs):
        """Identify contributing factors for diabetes"""
        factors = []
        if float(inputs['Glucose']) > 100:
            factors.append("Elevated glucose level")
        if float(inputs['BMI']) > 25:
            factors.append("BMI above normal range")
        if float(inputs['Age']) > 45:
            factors.append("Age factor (higher risk over 45)")
        if float(inputs['BloodPressure']) > 80:
            factors.append("Elevated blood pressure")
        if float(inputs['DiabetesPedigreeFunction']) > 0.5:
            factors.append("Family history of diabetes")

        if not factors:
            if float(inputs['Glucose']) < 100:
                factors.append("Healthy glucose level")
            if float(inputs['BMI']) < 25:
                factors.append("Healthy BMI")

        return factors[:3]

    def _get_hypertension_top_factors(self, inputs):
        """Identify contributing factors for hypertension"""
        factors = []
        if float(inputs['sysBP']) > 120 or float(inputs['diaBP']) > 80:
            factors.append("Elevated blood pressure readings")
        if float(inputs['currentSmoker']) == 1:
            factors.append("Current smoking status")
        if float(inputs['BMI']) > 25:
            factors.append("BMI above normal range")
        if float(inputs['age']) > 50:
            factors.append("Age factor (risk increases with age)")
        if float(inputs['totChol']) > 200:
            factors.append("Elevated cholesterol level")
        if float(inputs['diabetes']) == 1:
            factors.append("Existing diabetes diagnosis")

        if not factors:
            if float(inputs['sysBP']) < 120 and float(inputs['diaBP']) < 80:
                factors.append("Healthy blood pressure")
            if float(inputs['currentSmoker']) == 0:
                factors.append("Non-smoker")

        return factors[:3]

    def _get_diabetes_recommendations(self, risk_level, inputs):
        """Get personalized recommendations for diabetes"""
        if risk_level == 'Low':
            return [
                "✓ Keep up the great work! Your risk is low.",
                "✓ Maintain a balanced diet with limited sugar intake.",
                "✓ Continue regular physical activity (30 min/day).",
                "✓ Get annual health checkups to monitor your health."
            ]
        elif risk_level == 'Moderate':
            return [
                "⚠ Consider lifestyle modifications to lower your risk.",
                "⚠ Monitor your glucose levels regularly.",
                "⚠ Aim for 150 minutes of moderate exercise per week.",
                "⚠ Consult a healthcare provider for a personalized plan.",
                "⚠ Focus on weight management if BMI is elevated."
            ]
        else:
            return [
                "🚨 Please consult a healthcare provider soon.",
                "🚨 Get your blood sugar tested (HbA1c test recommended).",
                "🚨 Discuss prevention strategies with your doctor.",
                "🚨 Make dietary changes - reduce sugar and refined carbs.",
                "🚨 Start an exercise routine (with doctor approval).",
                "🚨 Monitor your health closely and follow medical advice."
            ]

    def _get_hypertension_recommendations(self, risk_level, inputs):
        """Get personalized recommendations for hypertension"""
        if risk_level == 'Low':
            return [
                "✓ Excellent! Your risk is low.",
                "✓ Maintain a heart-healthy diet (low sodium, rich in fruits/vegetables).",
                "✓ Continue regular physical activity.",
                "✓ Monitor blood pressure annually.",
                "✓ Limit alcohol consumption."
            ]
        elif risk_level == 'Moderate':
            recs = [
                "⚠ Take steps to lower your risk.",
                "⚠ Reduce sodium intake (less than 2,300mg daily).",
                "⚠ Exercise regularly (at least 150 min/week).",
                "⚠ Monitor blood pressure monthly.",
                "⚠ Manage stress through relaxation techniques.",
                "⚠ Consult a healthcare provider for guidance."
            ]
            if float(inputs['currentSmoker']) == 1:
                recs.append("⚠ Quitting smoking will significantly reduce your risk.")
            return recs
        else:
            recs = [
                "🚨 Please see a healthcare provider soon.",
                "🚨 Get your blood pressure checked regularly.",
                "🚨 Discuss medication options with your doctor.",
                "🚨 Reduce sodium intake immediately.",
                "🚨 Start a supervised exercise program.",
                "🚨 Monitor your blood pressure at home.",
                "🚨 Follow your doctor's treatment plan carefully."
            ]
            if float(inputs['currentSmoker']) == 1:
                recs.insert(2, "🚨 Quit smoking - this is critical for your health.")
            return recs

    def _get_confidence_description(self, probability):
        """Convert probability to description"""
        if probability < 0.30:
            return "Low risk - model is confident you're at low risk"
        elif probability < 0.40:
            return "Low to moderate risk - closer monitoring recommended"
        elif probability < 0.60:
            return "Moderate risk - lifestyle changes recommended"
        elif probability < 0.70:
            return "Moderate to high risk - medical consultation advised"
        else:
            return "High risk - please consult a healthcare provider"
