"""
QUICK FIX: Data Preprocessing Script

This script properly handles missing values in both datasets.
Run this with: py -3.12 fix_data.py
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os

print("="*80)
print("DATA PREPROCESSING - QUICK FIX")
print("="*80)

# ============================================
# 1. LOAD RAW DATA
# ============================================

print("\n📂 Loading raw data...")
diabetes = pd.read_csv('data/raw/diabetes.csv')
hypertension = pd.read_csv('data/raw/hypertension.csv')

print(f"✓ Diabetes: {diabetes.shape}")
print(f"✓ Hypertension: {hypertension.shape}")

# ============================================
# 2. HANDLE DIABETES MISSING VALUES
# ============================================

print("\n🔧 Processing DIABETES dataset...")
print("-" * 50)

# Replace impossible zeros with NaN
zero_columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
diabetes[zero_columns] = diabetes[zero_columns].replace(0, np.nan)

print("Missing values before imputation:")
for col in diabetes.columns:
    missing = diabetes[col].isnull().sum()
    if missing > 0:
        print(f"  {col}: {missing}")

# Fill missing values with column mean
for col in diabetes.columns:
    if diabetes[col].isnull().sum() > 0:
        mean_val = diabetes[col].mean()
        diabetes[col] = diabetes[col].fillna(mean_val)
        print(f"✓ Filled {col} with mean = {mean_val:.2f}")

# Remove Insulin and SkinThickness (6-feature model)
print("\n🗑️ Removing Insulin and SkinThickness columns...")
diabetes = diabetes.drop(['Insulin', 'SkinThickness'], axis=1)
print(f"✓ Now using 6 features: {diabetes.drop('Outcome', axis=1).columns.tolist()}")

# Verify no missing values
missing_diabetes = diabetes.isnull().sum().sum()
print(f"\n📊 Missing values after imputation: {missing_diabetes}")

if missing_diabetes == 0:
    print("✅ SUCCESS: No missing values in diabetes!")
else:
    print(f"❌ ERROR: Still have {missing_diabetes} missing values!")
    exit(1)

# ============================================
# 3. HANDLE HYPERTENSION MISSING VALUES
# ============================================

print("\n🔧 Processing HYPERTENSION dataset...")
print("-" * 50)

print("Missing values before imputation:")
for col in hypertension.columns:
    missing = hypertension[col].isnull().sum()
    if missing > 0:
        print(f"  {col}: {missing}")

# Fill missing values with column mean
for col in hypertension.columns:
    if hypertension[col].isnull().sum() > 0:
        if hypertension[col].dtype in ['float64', 'int64']:
            mean_val = hypertension[col].mean()
            hypertension[col] = hypertension[col].fillna(mean_val)
            print(f"✓ Filled {col} with mean = {mean_val:.2f}")
        else:
            mode_val = hypertension[col].mode()[0]
            hypertension[col] = hypertension[col].fillna(mode_val)
            print(f"✓ Filled {col} with mode = {mode_val}")

# Verify no missing values
missing_hypertension = hypertension.isnull().sum().sum()
print(f"\n📊 Missing values after imputation: {missing_hypertension}")

if missing_hypertension == 0:
    print("✅ SUCCESS: No missing values in hypertension!")
else:
    print(f"❌ ERROR: Still have {missing_hypertension} missing values!")
    exit(1)

# ============================================
# 4. SPLIT DATA (TRAIN/TEST)
# ============================================

print("\n✂️ Splitting datasets (80/20)...")
print("-" * 50)

# Split Diabetes
diabetes_train, diabetes_test = train_test_split(
    diabetes,
    test_size=0.2,
    random_state=42,
    stratify=diabetes['Outcome']
)

print(f"✓ Diabetes train: {diabetes_train.shape}")
print(f"✓ Diabetes test:  {diabetes_test.shape}")

# Split Hypertension
hypertension_train, hypertension_test = train_test_split(
    hypertension,
    test_size=0.2,
    random_state=42,
    stratify=hypertension['Risk']
)

print(f"✓ Hypertension train: {hypertension_train.shape}")
print(f"✓ Hypertension test:  {hypertension_test.shape}")

# ============================================
# 5. SAVE PROCESSED DATA
# ============================================

print("\n💾 Saving processed data...")
print("-" * 50)

os.makedirs('data/processed', exist_ok=True)

diabetes_train.to_csv('data/processed/diabetes_train.csv', index=False)
diabetes_test.to_csv('data/processed/diabetes_test.csv', index=False)
hypertension_train.to_csv('data/processed/hypertension_train.csv', index=False)
hypertension_test.to_csv('data/processed/hypertension_test.csv', index=False)

print("✓ data/processed/diabetes_train.csv")
print("✓ data/processed/diabetes_test.csv")
print("✓ data/processed/hypertension_train.csv")
print("✓ data/processed/hypertension_test.csv")

# ============================================
# 6. FINAL VERIFICATION
# ============================================

print("\n" + "="*80)
print("✅ PHASE 2 COMPLETE - VERIFICATION")
print("="*80)

# Reload to verify
diabetes_train_check = pd.read_csv('data/processed/diabetes_train.csv')
diabetes_test_check = pd.read_csv('data/processed/diabetes_test.csv')
hypertension_train_check = pd.read_csv('data/processed/hypertension_train.csv')
hypertension_test_check = pd.read_csv('data/processed/hypertension_test.csv')

print("\n📊 DIABETES:")
print(f"  Features: {diabetes_train_check.drop('Outcome', axis=1).columns.tolist()}")
print(f"  Number of features: {len(diabetes_train_check.columns) - 1}")
print(f"  Missing values in train: {diabetes_train_check.isnull().sum().sum()}")
print(f"  Missing values in test: {diabetes_test_check.isnull().sum().sum()}")

print("\n📊 HYPERTENSION:")
print(f"  Features: {hypertension_train_check.drop('Risk', axis=1).columns.tolist()}")
print(f"  Number of features: {len(hypertension_train_check.columns) - 1}")
print(f"  Missing values in train: {hypertension_train_check.isnull().sum().sum()}")
print(f"  Missing values in test: {hypertension_test_check.isnull().sum().sum()}")

# Final check
all_good = True

if len(diabetes_train_check.columns) != 7:
    print("\n⚠️ ERROR: Diabetes should have 6 features + Outcome = 7 columns")
    all_good = False

if diabetes_train_check.isnull().sum().sum() > 0 or diabetes_test_check.isnull().sum().sum() > 0:
    print("\n⚠️ ERROR: Diabetes data still has missing values!")
    all_good = False

if hypertension_train_check.isnull().sum().sum() > 0 or hypertension_test_check.isnull().sum().sum() > 0:
    print("\n⚠️ ERROR: Hypertension data still has missing values!")
    all_good = False

if all_good:
    print("\n" + "="*80)
    print("✅✅✅ SUCCESS! All data processed correctly!")
    print("="*80)
    print("\n🚀 Ready for Phase 3: Model Training!")
    print("\nNext step: Run Phase 3 notebook (03_model_training.ipynb)")
else:
    print("\n" + "="*80)
    print("❌ ERROR: Please check the issues above")
    print("="*80)
    exit(1)