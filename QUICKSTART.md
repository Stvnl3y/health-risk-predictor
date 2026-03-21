# ⚡ Quick Start Guide

For experienced users who want to get running fast.

---

## 🚀 5-Minute Setup

```bash
# 1. Install dependencies
py -3.12 -m pip install -r requirements.txt

# 2. Run Phase 2 (Data Preprocessing)
py -3.12 -m notebook
# Open notebooks/02_data_preprocessing.ipynb → Run All

# 3. Run Phase 3 (Model Training)
# Open notebooks/03_model_training.ipynb → Run All

# 4. Run the app
py -3.12 app/main.py
```

---

## 📋 What You Get

- 6-feature diabetes model (removed Insulin, SkinThickness)
- 12-feature hypertension model
- Scalers fitted on DataFrames (proper column names)
- Flet app with radio buttons and optional fields
- No DataFrame/array mismatch warnings

---

## ✅ Expected Results

**Phase 2 Output:**
```
✅ SUCCESS: No missing values!
Diabetes: 6 features (Pregnancies, Glucose, BP, BMI, Family History, Age)
Hypertension: 12 features (all original)
```

**Phase 3 Output:**
```
Diabetes Accuracy: ~77%
Hypertension Accuracy: ~81%
Test predictions: LOW RISK for healthy, HIGH RISK for unhealthy
✅ Models saved with proper feature names
```

**App:**
```
✓ Diabetes model loaded successfully
✓ Hypertension model loaded successfully
(No warnings about feature names)
```

---

## 🧪 Quick Test

**Healthy:** Glucose=80, BP=70, BMI=22, Age=25 → Should show LOW RISK 🟢

**Unhealthy:** Glucose=180, BP=90, BMI=35, Age=55 → Should show HIGH RISK 🔴

---

## 🔧 Key Fixes from v1

1. ✅ Scalers created in Phase 3 (not Phase 2)
2. ✅ All operations use DataFrames (not arrays)
3. ✅ Consistent Python 3.12
4. ✅ Radio buttons for Yes/No (not toggles)
5. ✅ Optional fields with defaults

---

## 📁 File Structure

```
health-risk-predictor-v2/
├── data/raw/              # diabetes.csv, hypertension.csv
├── data/processed/        # Created by Phase 2
├── models/                # Created by Phase 3 (4 .pkl files)
├── notebooks/             # 02 & 03 notebooks
├── app/                   # 4 Python files
└── requirements.txt
```

---

## 🐛 Troubleshooting

| Issue | Fix |
|-------|-----|
| "No module named X" | `py -3.12 -m pip install -r requirements.txt` |
| "Cannot find models" | Run Phase 3 |
| Feature name warnings | Delete models/, re-run Phase 3 |
| All HIGH RISK | Delete models/, re-run Phase 3 with Python 3.12 |

---

**That's it! You're ready to go.** 🎉

See SETUP_GUIDE.md for detailed instructions.
