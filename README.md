# 🏥 Health Risk Predictor

AI-powered health risk assessment for diabetes and hypertension using machine learning.

## 📋 Overview

This application uses trained Logistic Regression models to predict health risks based on user-provided health parameters. It provides:

- **Diabetes Risk Assessment** (6-feature model)
- **Hypertension Risk Assessment** (12-feature model)
- Risk levels: Low 🟢 | Moderate 🟡 | High 🔴
- Personalized health recommendations
- Educational content about each condition

## ✨ Features

- ✅ Clean, intuitive UI with Flet framework
- ✅ Real-time risk prediction
- ✅ Scientifically-based recommendations
- ✅ Optional fields (uses population averages for unknown values)
- ✅ Cross-platform (Web, Desktop, Mobile)
- ✅ Privacy-focused (all processing done locally)

## 🎯 Model Performance

**Diabetes Model:**
- Features: 6 (Pregnancies, Glucose, Blood Pressure, BMI, Family History, Age)
- Expected Accuracy: 75-82%
- Expected Recall: 70-80%

**Hypertension Model:**
- Features: 12 (Gender, Age, Smoking, Cholesterol, BP, BMI, Heart Rate, Glucose, etc.)
- Expected Accuracy: 78-85%
- Expected Recall: 75-83%

## 📁 Project Structure

```
health-risk-predictor-v2/
├── data/
│   ├── raw/                    # Original datasets
│   └── processed/              # Cleaned data (created by Phase 2)
├── notebooks/
│   ├── 02_data_preprocessing.ipynb   # Data cleaning
│   └── 03_model_training.ipynb       # Model training
├── models/                     # Trained models (created by Phase 3)
│   ├── diabetes_model.pkl
│   ├── hypertension_model.pkl
│   ├── scaler_diabetes.pkl
│   └── scaler_hypertension.pkl
├── app/
│   ├── main.py                # App entry point
│   ├── prediction_engine.py   # ML prediction logic
│   ├── ui_components.py       # UI screens
│   └── utils.py               # Helper functions
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── SETUP_GUIDE.md            # Detailed setup instructions
└── QUICKSTART.md             # Fast setup for experienced users
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12 installed
- Git (optional)

### Installation

1. **Install dependencies:**
```bash
py -3.12 -m pip install -r requirements.txt
```

2. **Run Phase 2 (Data Preprocessing):**
```bash
py -3.12 -m notebook
# Open notebooks/02_data_preprocessing.ipynb
# Run all cells
```

3. **Run Phase 3 (Model Training):**
```bash
# In Jupyter, open notebooks/03_model_training.ipynb
# Run all cells
```

4. **Run the app:**
```bash
py -3.12 app/main.py
```

## 📊 Testing

Test the app with these profiles:

**Healthy Profile (Should show LOW RISK):**
- Diabetes: Glucose=80, BP=70, BMI=22, Age=25
- Hypertension: Age=25, BP=110/70, BMI=21, Non-smoker

**High Risk Profile (Should show HIGH RISK):**
- Diabetes: Glucose=180, BP=90, BMI=35, Age=55
- Hypertension: Age=65, BP=160/95, BMI=32, Smoker

## 🔧 Troubleshooting

**Issue: "No module named 'flet'"**
- Solution: Install dependencies with `py -3.12 -m pip install -r requirements.txt`

**Issue: "Cannot find models"**
- Solution: Run Phase 2 and Phase 3 notebooks first to create models

**Issue: Models loaded but predictions are always high risk**
- Solution: This should NOT happen in v2 (we fixed this!)
- If it does, re-run Phase 3 to recreate models

**Issue: Jupyter won't start**
- Solution: `py -3.12 -m pip install jupyter notebook`

## 📚 Documentation

- **SETUP_GUIDE.md** - Detailed setup instructions for beginners
- **QUICKSTART.md** - Fast track for experienced users

## ⚠️ Important Notes

- This app is for **educational purposes only**
- **NOT a substitute for professional medical advice**
- Always consult healthcare providers for medical decisions
- Data is processed locally (privacy-focused)

## 🎨 Key Improvements in v2

✅ Fixed DataFrame/array mismatch (no more feature name warnings)
✅ Proper scaler creation (fitted on DataFrames with column names)
✅ Consistent Python 3.12 throughout
✅ Radio buttons for Yes/No questions (not toggles)
✅ Optional fields with smart defaults
✅ Comprehensive testing in Phase 3
✅ Better documentation

## 📖 Learn More

- Scikit-learn: https://scikit-learn.org/
- Flet Framework: https://flet.dev/
- PIMA Indians Diabetes Dataset: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
- Framingham Heart Study: https://www.framinghamheartstudy.org/

## 👨‍💻 Developer

Built as a beginner ML project with focus on:
- Clean code architecture
- Proper ML practices
- User-friendly interface
- Educational value

## 📄 License

This project is for educational purposes.

---

**Ready to assess your health risks? Run `py -3.12 app/main.py` to get started!** 🚀
