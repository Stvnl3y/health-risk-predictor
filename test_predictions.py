"""
HEALTH RISK PREDICTOR - PREDICTION TESTS

Run this before building APK to verify models work correctly.

Usage:
    python test_predictions.py
"""

import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from prediction_engine import PredictionEngine


def test_healthy_diabetes():
    """Test 1: Healthy diabetes profile should show LOW RISK"""
    engine = PredictionEngine()
    
    healthy_profile = {
        'Pregnancies': 0,
        'Glucose': 80,
        'BloodPressure': 70,
        'BMI': 22,
        'DiabetesPedigreeFunction': 0.1,
        'Age': 25
    }
    
    result = engine.predict_diabetes(healthy_profile)
    
    print(f"Test 1: Healthy Diabetes Profile")
    print(f"  Probability: {result['probability']}%")
    print(f"  Risk Level: {result['risk_level']}")
    
    assert result['risk_level'] == 'Low', f"Expected Low, got {result['risk_level']}"
    assert result['probability'] < 30, f"Expected < 30%, got {result['probability']}%"
    print("  ✓ PASSED\n")
    return True


def test_high_risk_diabetes():
    """Test 2: High risk diabetes profile should show HIGH RISK"""
    engine = PredictionEngine()
    
    high_risk_profile = {
        'Pregnancies': 6,
        'Glucose': 180,
        'BloodPressure': 90,
        'BMI': 35,
        'DiabetesPedigreeFunction': 0.8,
        'Age': 55
    }
    
    result = engine.predict_diabetes(high_risk_profile)
    
    print(f"Test 2: High Risk Diabetes Profile")
    print(f"  Probability: {result['probability']}%")
    print(f"  Risk Level: {result['risk_level']}")
    
    assert result['risk_level'] == 'High', f"Expected High, got {result['risk_level']}"
    assert result['probability'] > 60, f"Expected > 60%, got {result['probability']}%"
    print("  ✓ PASSED\n")
    return True


def test_healthy_hypertension():
    """Test 3: Healthy hypertension profile should show LOW RISK"""
    engine = PredictionEngine()
    
    healthy_profile = {
        'male': 0,
        'age': 25,
        'currentSmoker': 0,
        'cigsPerDay': 0,
        'BPMeds': 0,
        'diabetes': 0,
        'totChol': 180,
        'sysBP': 110,
        'diaBP': 70,
        'BMI': 21,
        'heartRate': 75,
        'glucose': 85
    }
    
    result = engine.predict_hypertension(healthy_profile)
    
    print(f"Test 3: Healthy Hypertension Profile")
    print(f"  Probability: {result['probability']}%")
    print(f"  Risk Level: {result['risk_level']}")
    
    assert result['risk_level'] == 'Low', f"Expected Low, got {result['risk_level']}"
    assert result['probability'] < 30, f"Expected < 30%, got {result['probability']}%"
    print("  ✓ PASSED\n")
    return True


def test_high_risk_hypertension():
    """Test 4: High risk hypertension profile should show HIGH RISK"""
    engine = PredictionEngine()
    
    high_risk_profile = {
        'male': 1,
        'age': 65,
        'currentSmoker': 1,
        'cigsPerDay': 20,
        'BPMeds': 1,
        'diabetes': 1,
        'totChol': 250,
        'sysBP': 160,
        'diaBP': 95,
        'BMI': 32,
        'heartRate': 85,
        'glucose': 140
    }
    
    result = engine.predict_hypertension(high_risk_profile)
    
    print(f"Test 4: High Risk Hypertension Profile")
    print(f"  Probability: {result['probability']}%")
    print(f"  Risk Level: {result['risk_level']}")
    
    assert result['risk_level'] == 'High', f"Expected High, got {result['risk_level']}"
    assert result['probability'] > 60, f"Expected > 60%, got {result['probability']}%"
    print("  ✓ PASSED\n")
    return True


def test_moderate_risk():
    """Test 5: Moderate risk profile should show MODERATE"""
    engine = PredictionEngine()
    
    moderate_profile = {
        'Pregnancies': 3,
        'Glucose': 110,
        'BloodPressure': 78,
        'BMI': 27,
        'DiabetesPedigreeFunction': 0.4,
        'Age': 40
    }
    
    result = engine.predict_diabetes(moderate_profile)
    
    print(f"Test 5: Moderate Risk Diabetes Profile")
    print(f"  Probability: {result['probability']}%")
    print(f"  Risk Level: {result['risk_level']}")
    
    # Should be Low or Moderate (borderline)
    assert result['risk_level'] in ['Low', 'Moderate'], f"Unexpected: {result['risk_level']}"
    print("  ✓ PASSED\n")
    return True


def test_recommendations():
    """Test 6: Verify recommendations are provided"""
    engine = PredictionEngine()
    
    profile = {
        'Pregnancies': 2,
        'Glucose': 95,
        'BloodPressure': 75,
        'BMI': 24,
        'DiabetesPedigreeFunction': 0.3,
        'Age': 35
    }
    
    result = engine.predict_diabetes(profile)
    
    print(f"Test 6: Recommendations Check")
    print(f"  Number of recommendations: {len(result['recommendations'])}")
    print(f"  Number of factors: {len(result['top_factors'])}")
    
    assert len(result['recommendations']) > 0, "Should have recommendations"
    assert len(result['top_factors']) > 0, "Should have top factors"
    print("  ✓ PASSED\n")
    return True


def main():
    """Run all tests"""
    print("=" * 60)
    print("HEALTH RISK PREDICTOR - MODEL VERIFICATION")
    print("=" * 60)
    print()
    
    tests = [
        test_healthy_diabetes,
        test_high_risk_diabetes,
        test_healthy_hypertension,
        test_high_risk_hypertension,
        test_moderate_risk,
        test_recommendations
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            failed += 1
            print(f"  ✗ FAILED: {str(e)}\n")
    
    print("=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("\n✅ ALL TESTS PASSED! Models are working correctly.")
        print("   Ready to build APK or deploy to web.")
        return 0
    else:
        print(f"\n❌ {failed} TEST(S) FAILED!")
        print("   Fix issues before building APK.")
        return 1


if __name__ == "__main__":
    exit(main())
