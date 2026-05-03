"""
ML MODEL COMPARISON FOR HEALTH RISK PREDICTION

Compares 8 different ML models on diabetes and hypertension datasets.
Shows evaluation metrics to help choose the best model.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, 
    roc_auc_score, confusion_matrix, classification_report
)

# Import all models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# LOAD AND PREPARE DATA
# ============================================================================

def load_diabetes_data(filepath):
    """Load and prepare diabetes dataset"""
    df = pd.read_csv(filepath)
    
    # Handle zeros as missing values
    zero_columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for col in zero_columns:
        df[col] = df[col].replace(0, np.nan)
        mean_val = df[col].mean()
        df[col] = df[col].fillna(mean_val)
    
    # Use 6 features (removed Insulin and SkinThickness)
    features = ['Pregnancies', 'Glucose', 'BloodPressure', 'BMI', 
                'DiabetesPedigreeFunction', 'Age']
    
    X = df[features]
    y = df['Outcome']
    
    return X, y, features


def load_hypertension_data(filepath):
    """Load and prepare hypertension dataset"""
    df = pd.read_csv(filepath)
    
    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))
    
    # All 12 features
    features = ['male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds',
                'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 
                'heartRate', 'glucose']
    
    X = df[features]
    y = df['Risk']
    
    return X, y, features


# ============================================================================
# MODEL DEFINITIONS
# ============================================================================

def get_models():
    """Define all models to compare"""
    models = {
        'Logistic Regression': LogisticRegression(
            max_iter=1000, 
            random_state=42,
            class_weight='balanced'  # Handle imbalanced data
        ),
        
        'Random Forest': RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            class_weight='balanced'
        ),
        
        'XGBoost (Gradient Boosting)': GradientBoostingClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            random_state=42
        ),
        
        'Support Vector Machine': SVC(
            kernel='rbf',
            probability=True,  # Enable probability predictions
            random_state=42,
            class_weight='balanced'
        ),
        
        'Neural Network': MLPClassifier(
            hidden_layer_sizes=(64, 32),
            max_iter=1000,
            random_state=42,
            early_stopping=True
        ),
        
        'Naive Bayes': GaussianNB(),
        
        'K-Nearest Neighbors': KNeighborsClassifier(
            n_neighbors=5,
            weights='distance'  # Weight by distance
        ),
        
        'Decision Tree': DecisionTreeClassifier(
            max_depth=10,
            random_state=42,
            class_weight='balanced'
        )
    }
    
    return models


# ============================================================================
# EVALUATION FUNCTIONS
# ============================================================================

def evaluate_model(model, X_train, X_test, y_train, y_test):
    """Train and evaluate a single model"""
    # Train
    model.fit(X_train, y_train)
    
    # Predict
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
    
    # Calculate metrics
    results = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, zero_division=0),
        'Recall': recall_score(y_test, y_pred, zero_division=0),
        'F1-Score': f1_score(y_test, y_pred, zero_division=0),
    }
    
    if y_pred_proba is not None:
        results['ROC-AUC'] = roc_auc_score(y_test, y_pred_proba)
    else:
        results['ROC-AUC'] = None
    
    # Confusion matrix for specificity
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    results['Specificity'] = tn / (tn + fp) if (tn + fp) > 0 else 0
    
    return results, y_pred


def compare_models(X, y, dataset_name):
    """Compare all models on a dataset"""
    print(f"\n{'='*80}")
    print(f"  {dataset_name.upper()} DATASET - MODEL COMPARISON")
    print(f"{'='*80}\n")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Get models
    models = get_models()
    
    # Store results
    all_results = {}
    
    # Evaluate each model
    for name, model in models.items():
        print(f"Training {name}...")
        results, y_pred = evaluate_model(
            model, X_train_scaled, X_test_scaled, y_train, y_test
        )
        all_results[name] = results
    
    # Create results DataFrame
    results_df = pd.DataFrame(all_results).T
    
    # Sort by F1-Score (best balance for healthcare)
    results_df = results_df.sort_values('F1-Score', ascending=False)
    
    # Display results
    print(f"\n{'='*80}")
    print("RESULTS (sorted by F1-Score)")
    print(f"{'='*80}\n")
    print(results_df.to_string())
    
    # Highlight best model
    best_model = results_df.index[0]
    best_f1 = results_df.loc[best_model, 'F1-Score']
    
    print(f"\n{'='*80}")
    print(f"🏆 BEST MODEL: {best_model}")
    print(f"   F1-Score: {best_f1:.4f}")
    print(f"{'='*80}\n")
    
    # Explain metrics for healthcare context
    print("\n📊 WHAT THESE METRICS MEAN FOR HEALTHCARE:\n")
    print("Accuracy:    Overall correctness (can be misleading with imbalanced data)")
    print("Precision:   Of predicted HIGH RISK, how many are actually high risk?")
    print("             (High = fewer false alarms)")
    print("Recall:      Of actual HIGH RISK people, how many did we catch?")
    print("             (High = fewer missed cases - CRITICAL for healthcare!)")
    print("F1-Score:    Balance between precision and recall")
    print("             (Best overall metric for healthcare)")
    print("ROC-AUC:     Ability to distinguish high vs low risk (0.5-1.0)")
    print("             (Higher = better discrimination)")
    print("Specificity: Of healthy people, how many did we correctly identify?")
    print("             (High = fewer false positives)\n")
    
    return results_df


# ============================================================================
# RECOMMENDATIONS
# ============================================================================

def get_recommendations(diabetes_results, hypertension_results):
    """Provide model recommendations based on results"""
    print("\n" + "="*80)
    print("  RECOMMENDATIONS")
    print("="*80 + "\n")
    
    print("🎯 FOR DIABETES PREDICTION:")
    print(f"   Best Model: {diabetes_results.index[0]}")
    print(f"   F1-Score: {diabetes_results.iloc[0]['F1-Score']:.4f}")
    print(f"   Why: {get_model_explanation(diabetes_results.index[0])}\n")
    
    print("🎯 FOR HYPERTENSION PREDICTION:")
    print(f"   Best Model: {hypertension_results.index[0]}")
    print(f"   F1-Score: {hypertension_results.iloc[0]['F1-Score']:.4f}")
    print(f"   Why: {get_model_explanation(hypertension_results.index[0])}\n")
    
    print("💡 GENERAL GUIDANCE:\n")
    print("• Logistic Regression: Simple, interpretable, fast, works well for linear relationships")
    print("• Random Forest: Handles non-linear patterns, robust, less overfitting")
    print("• XGBoost: Often best performance, handles complex patterns, industry standard")
    print("• Neural Network: Captures very complex patterns, needs more data")
    print("• SVM: Good for high-dimensional data, can be slow")
    print("• Naive Bayes: Very fast, works with small data, assumes independence")
    print("• KNN: Simple, no training, sensitive to scaling")
    print("• Decision Tree: Easy to interpret, prone to overfitting\n")
    
    print("🏥 FOR HEALTHCARE APPS:\n")
    print("Priority: HIGH RECALL (catch all high-risk cases)")
    print("Balance: Good precision (avoid too many false alarms)")
    print("Ideal: F1-Score > 0.75, Recall > 0.80\n")
    
    print("📦 DEPLOYMENT CONSIDERATIONS:\n")
    print("• Logistic Regression: Smallest file size, fastest inference")
    print("• Random Forest/XGBoost: Larger files (~5-10 MB), still fast")
    print("• Neural Networks: Largest files, slower inference")
    print("• SVM: Can be slow for large datasets\n")


def get_model_explanation(model_name):
    """Get explanation for why a model performs well"""
    explanations = {
        'Logistic Regression': 'Simple, interpretable, works well for linearly separable data',
        'Random Forest': 'Handles non-linear relationships well, resistant to overfitting',
        'XGBoost (Gradient Boosting)': 'Excellent performance, handles complex patterns, industry standard',
        'Support Vector Machine': 'Good for high-dimensional data with clear margins',
        'Neural Network': 'Captures very complex non-linear patterns',
        'Naive Bayes': 'Fast, works well with small datasets',
        'K-Nearest Neighbors': 'Simple, effective for local patterns',
        'Decision Tree': 'Easy to interpret, captures non-linear relationships'
    }
    return explanations.get(model_name, 'Good performance on this dataset')


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main comparison function"""
    print("\n" + "="*80)
    print("  MACHINE LEARNING MODEL COMPARISON")
    print("  Health Risk Prediction: Diabetes & Hypertension")
    print("="*80)
    
    # Load datasets
    print("\n📂 Loading datasets...")
    
    # Update these paths to your actual file locations
    diabetes_path = "data/raw/diabetes.csv" # Update this path
    hypertension_path = "data/raw/hypertension.csv"  # Update this path
    
    try:
        X_diabetes, y_diabetes, diabetes_features = load_diabetes_data(diabetes_path)
        print(f"✓ Diabetes dataset loaded: {len(X_diabetes)} samples, {len(diabetes_features)} features")
    except FileNotFoundError:
        print(f"✗ Diabetes dataset not found at: {diabetes_path}")
        print("  Please update the path in the script!")
        return
    
    try:
        X_hypertension, y_hypertension, hypertension_features = load_hypertension_data(hypertension_path)
        print(f"✓ Hypertension dataset loaded: {len(X_hypertension)} samples, {len(hypertension_features)} features")
    except FileNotFoundError:
        print(f"✗ Hypertension dataset not found at: {hypertension_path}")
        print("  Please update the path in the script!")
        return
    
    # Compare models on both datasets
    diabetes_results = compare_models(X_diabetes, y_diabetes, "Diabetes")
    hypertension_results = compare_models(X_hypertension, y_hypertension, "Hypertension")
    
    # Provide recommendations
    get_recommendations(diabetes_results, hypertension_results)
    
    print("\n" + "="*80)
    print("  COMPARISON COMPLETE!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
