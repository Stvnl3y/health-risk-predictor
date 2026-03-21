# 📘 Complete Setup Guide

Step-by-step instructions for setting up and running the Health Risk Predictor.

---

## 🎯 What You'll Build

A working health risk assessment app that can:
- Predict diabetes risk
- Predict hypertension risk  
- Provide personalized recommendations
- Run on your computer (Windows/Mac/Linux)

---

## ⏱️ Time Required

- **Setup:** 15 minutes
- **Data Processing (Phase 2):** 5 minutes
- **Model Training (Phase 3):** 10 minutes
- **Testing:** 5 minutes
- **Total:** ~35 minutes

---

## ✅ Prerequisites

### 1. Python 3.12 Installed

**Check if you have it:**
```bash
py -3.12 --version
```

**If not installed:**
- Download from: https://www.python.org/downloads/
- During installation: ✅ CHECK "Add Python to PATH"
- Choose Python 3.12.x (latest stable)

---

## 📦 Step 1: Install Dependencies

Open Command Prompt (Windows) or Terminal (Mac/Linux) and run:

```bash
# Navigate to project folder
cd path/to/health-risk-predictor-v2

# Install all required packages
py -3.12 -m pip install -r requirements.txt
```

**This installs:**
- pandas (data processing)
- scikit-learn (machine learning)
- flet (app framework)
- jupyter (for running notebooks)
- And more...

**Wait 2-3 minutes** for installation to complete.

---

## 📊 Step 2: Run Phase 2 (Data Preprocessing)

This step cleans the data and prepares it for training.

### Open Jupyter Notebook:

```bash
py -3.12 -m notebook
```

**Your browser will open automatically** showing the Jupyter interface.

### Navigate and Run:

1. **Navigate to:** `notebooks/`
2. **Open:** `02_data_preprocessing.ipynb`
3. **Run all cells:**
   - Click: `Cell` → `Run All`
   - OR click the ▶▶ button at the top

### What It Does:

- Loads diabetes.csv and hypertension.csv
- Handles missing values (fills with mean)
- Removes Insulin & SkinThickness columns (6-feature diabetes model)
- Splits into training/testing sets (80/20)
- Saves cleaned data to `data/processed/`

### Expected Output:

```
✅ SUCCESS! All data processed correctly!
```

### Verify:

Check that these files exist:
- `data/processed/diabetes_train.csv`
- `data/processed/diabetes_test.csv`
- `data/processed/hypertension_train.csv`
- `data/processed/hypertension_test.csv`

---

## 🤖 Step 3: Run Phase 3 (Model Training)

This step trains the ML models and creates scalers.

### In Jupyter (still open from Step 2):

1. **Open:** `notebooks/03_model_training.ipynb`
2. **Run all cells:**
   - Click: `Cell` → `Run All`
   - Wait ~5-10 minutes for training

### What It Does:

- Loads processed data
- **Creates scalers** (fitted on DataFrames with column names) ← KEY FIX!
- Scales training and testing data
- Trains Logistic Regression models
- Evaluates performance
- **Runs test predictions** to verify everything works
- Saves models to `models/`

### Expected Output:

```
📊 DIABETES MODEL PERFORMANCE:
Accuracy:  77.9%
Recall:    73.5%
✅ Diabetes model meets performance targets!

📊 HYPERTENSION MODEL PERFORMANCE:
Accuracy:  81.2%
Recall:    78.3%
✅ Hypertension model meets performance targets!

🧪 TEST 1: Healthy Diabetes Profile (Should be LOW RISK)
Probability: 18.5%
✅ CORRECT: Shows LOW RISK as expected!

✅✅✅ SUCCESS! Models trained and saved correctly!
```

### Verify:

Check that these files exist:
- `models/diabetes_model.pkl`
- `models/scaler_diabetes.pkl`
- `models/hypertension_model.pkl`
- `models/scaler_hypertension.pkl`

---

## 🚀 Step 4: Run the App

Close Jupyter (or keep it running, doesn't matter).

### Start the App:

```bash
# From project root directory
py -3.12 app/main.py
```

### Expected Output:

```
✓ Diabetes model loaded successfully
✓ Hypertension model loaded successfully
```

**A window should open** with your Health Risk Checker app!

---

## 🧪 Step 5: Test the App

### Test 1: Healthy Profile (LOW RISK)

**Diabetes Form:**
```
Pregnancies: 0
Glucose: 80
Blood Pressure: 70
BMI: 22
Family History: 0.1
Age: 25
```

**Expected:** LOW RISK 🟢 (15-30%)

**Hypertension Form:**
```
Gender: Female
Age: 25
Smoking: No
Systolic BP: 110
Diastolic BP: 70
BMI: 21
(Leave optional fields blank)
```

**Expected:** LOW RISK 🟢 (10-25%)

### Test 2: High Risk Profile (HIGH RISK)

**Diabetes Form:**
```
Pregnancies: 6
Glucose: 180
Blood Pressure: 90
BMI: 35
Family History: 0.8
Age: 55
```

**Expected:** HIGH RISK 🔴 (70-90%)

**Hypertension Form:**
```
Gender: Male
Age: 65
Smoking: Yes
Systolic BP: 160
Diastolic BP: 95
BMI: 32
Cholesterol: 250
```

**Expected:** HIGH RISK 🔴 (75-95%)

---

## ✅ Verification Checklist

- [ ] Python 3.12 installed
- [ ] All dependencies installed (no errors)
- [ ] Phase 2 completed successfully
- [ ] Phase 3 completed successfully  
- [ ] 4 model files exist in models/
- [ ] App starts without errors
- [ ] Models load successfully (no warnings)
- [ ] Healthy profile shows LOW RISK
- [ ] High risk profile shows HIGH RISK

**If all checked → SUCCESS!** 🎉

---

## 🐛 Troubleshooting

### "py -3.12 not recognized"

**Problem:** Python 3.12 not in PATH

**Solutions:**
- Try: `python -3.12` instead of `py -3.12`
- Try: `python3.12`
- Reinstall Python and check "Add to PATH"

### "No module named 'pandas'"

**Problem:** Dependencies not installed

**Solution:**
```bash
py -3.12 -m pip install -r requirements.txt
```

### "Cannot find models"

**Problem:** Phase 3 not run

**Solution:** Run Phase 3 notebook to create models

### App shows "Error making prediction: The feature names should match..."

**Problem:** Old models from previous project

**Solution:** Delete `models/` folder and re-run Phase 3

### Jupyter won't start

**Solution:**
```bash
py -3.12 -m pip install jupyter notebook
py -3.12 -m notebook
```

### Terminal shows warnings about "deprecated"

**These are safe to ignore** - they're about Flet version updates

### Predictions are wrong (everything shows high risk)

**This should NOT happen in v2!**

**If it does:**
1. Delete `models/` folder
2. Re-run Phase 3 notebook
3. Restart app

---

## 🎓 Understanding the Pipeline

```
Raw Data (CSV files)
    ↓
Phase 2: Data Preprocessing
    ├── Handle missing values
    ├── Remove unnecessary columns
    ├── Split train/test (80/20)
    └── Save to data/processed/
    ↓
Phase 3: Model Training
    ├── Create scalers (with DataFrame column names)
    ├── Fit scalers on TRAINING data only
    ├── Transform both train and test data
    ├── Train Logistic Regression models
    ├── Evaluate on test data
    └── Save models and scalers
    ↓
App: Make Predictions
    ├── Load saved models and scalers
    ├── User enters health data
    ├── Convert to DataFrame (with column names)
    ├── Scale using saved scaler
    ├── Predict with saved model
    └── Show results to user
```

---

## 📚 Next Steps

**After setup works:**

1. **Explore the code** - understand how it works
2. **Customize UI** - change colors, add features
3. **Deploy** - share with friends (see deployment guide)
4. **Learn more ML** - try different algorithms

**Deployment Options:**
- Web: `flet publish app/main.py` (free flet hosting)
- Android: `flet build apk app/main.py`
- Desktop: `flet build windows app/main.py`

---

## 💡 Tips

- **Keep notebooks open** while developing - useful for quick tests
- **Check Phase 3 test predictions** - they verify everything works
- **Use version control** - git to track changes
- **Document changes** - if you modify the code

---

## 🆘 Still Having Issues?

If you're stuck:

1. **Check error messages carefully** - they usually tell you what's wrong
2. **Re-run from Phase 2** - fresh start often fixes issues
3. **Verify Python version** - must be 3.12
4. **Check file paths** - must run commands from project root

---

**Congratulations! You've built a working ML application!** 🎉

Ready to assess health risks? Run: `py -3.12 app/main.py`
