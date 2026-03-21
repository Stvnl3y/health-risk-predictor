# 🚀 Android Deployment Guide

Complete guide for deploying Health Risk Checker to Android APK and Web.

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Prerequisites](#prerequisites)
3. [Option A: Android APK Build](#option-a-android-apk-build)
4. [Option B: Web Deployment](#option-b-web-deployment)
5. [Testing Strategy](#testing-strategy)
6. [Troubleshooting](#troubleshooting)

---

## ⚡ Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Test locally first
flet run app/main.py

# Build for Android (takes 10-20 minutes)
flet build apk app/main.py

# OR deploy to web (instant)
flet publish app/main.py
```

---

## 📦 Prerequisites

### For Android Build:

1. **Java JDK 17** (required for Android build)
   ```bash
   # Download from: https://www.oracle.com/java/technologies/downloads/
   # Or use OpenJDK: https://adoptium.net/
   ```

2. **Android SDK** (installed automatically by Flet on first build)

3. **Environment Variables:**
   ```bash
   # Windows - Add to System Properties > Environment Variables
   JAVA_HOME=C:\Program Files\Java\jdk-17
   ANDROID_HOME=C:\Users\<YourName>\AppData\Local\Android\Sdk
   ```

4. **Flet (latest version):**
   ```bash
   pip install --upgrade flet
   ```

### For Web Deployment:

1. **Flet account** (free)
   ```bash
   flet login
   ```

2. **No additional setup required**

---

## 📱 Option A: Android APK Build

### Step 1: Verify Setup

```bash
# Check Java installation
java -version

# Check Flet version
flet --version

# Should be 0.23.0 or higher
```

### Step 2: Configure flet.json

Already created! Edit these values in `flet.json`:

```json
{
  "android": {
    "package_name": "com.healthrisk.checker",
    "version": "1.0.0",
    "min_sdk": 21,
    "target_sdk": 33
  }
}
```

**Note:** `min_sdk: 21` = Android 5.0+ (covers 95% of devices)

### Step 3: Create App Icons (Optional but Recommended)

Create `assets/` folder with:

```
assets/
├── icon.png        # 1024x1024 px app icon
└── splash.png      # 1920x1080 px splash screen
```

### Step 4: Build APK

```bash
# Navigate to project root
cd C:\Users\Johnson\health-risk-predictor-v2

# Build release APK (first time takes 10-20 minutes)
flet build apk app/main.py

# Build debug APK (faster, for testing)
flet build apk --debug app/main.py
```

### Step 5: Find Your APK

After successful build:

```
build/
└── android/
    └── app/
        └── build/
            └── outputs/
                └── apk/
                    └── release/
                        └── app-release.apk    ← Your APK!
```

### Step 6: Install & Test

**On Android device:**

1. Transfer APK to phone
2. Enable "Install from Unknown Sources"
3. Install APK
4. Open "Health Risk Checker"

**Or use ADB:**
```bash
adb install build/android/app/build/outputs/apk/release/app-release.apk
```

### Step 7: Publish to Google Play (Optional)

1. **Create Google Play Console account** ($25 one-time fee)

2. **Build Android App Bundle (AAB) instead of APK:**
   ```bash
   flet build appbundle app/main.py
   ```

3. **Upload AAB to Google Play Console**

4. **Fill out store listing:**
   - Title: "Health Risk Checker"
   - Description: "AI-powered health assessment for diabetes & hypertension"
   - Category: Health & Fitness
   - Content Rating: Everyone

5. **Submit for review** (typically 2-7 days)

---

## 🌐 Option B: Web Deployment (RECOMMENDED FOR FAST DEPLOYMENT)

### Why Web First?

✅ Instant deployment (no build time)
✅ No Android SDK/Java setup needed
✅ Works on all devices (iOS, Android, Desktop)
✅ Easy to share and test
✅ Free hosting via Flet

### Step 1: Login to Flet

```bash
flet login
```

This opens browser for authentication.

### Step 2: Publish App

```bash
# Publish to Flet's cloud (free)
flet publish app/main.py
```

### Step 3: Get Your URL

After publishing, you'll receive a URL like:
```
https://your-app-name.flet.dev
```

### Step 4: Share & Test

- Share URL with anyone
- Works on mobile browsers
- Can be added to home screen (PWA-like)

### Step 5: Custom Domain (Optional)

1. Buy domain (e.g., healthriskchecker.com)
2. Configure DNS to point to Flet
3. Update publish settings

---

## 🧪 Testing Strategy

### Phase 1: Unit Testing (Desktop)

Test prediction engine before building:

```python
# test_predictions.py
from app.prediction_engine import PredictionEngine

engine = PredictionEngine()

# Test 1: Healthy diabetes profile (should be LOW RISK)
healthy_diabetes = {
    'Pregnancies': 0,
    'Glucose': 80,
    'BloodPressure': 70,
    'BMI': 22,
    'DiabetesPedigreeFunction': 0.1,
    'Age': 25
}
result = engine.predict_diabetes(healthy_diabetes)
assert result['risk_level'] == 'Low', f"Expected Low, got {result['risk_level']}"
print("✓ Healthy diabetes test passed")

# Test 2: High risk diabetes profile
high_risk_diabetes = {
    'Pregnancies': 6,
    'Glucose': 180,
    'BloodPressure': 90,
    'BMI': 35,
    'DiabetesPedigreeFunction': 0.8,
    'Age': 55
}
result = engine.predict_diabetes(high_risk_diabetes)
assert result['risk_level'] == 'High', f"Expected High, got {result['risk_level']}"
print("✓ High risk diabetes test passed")

# Test 3: Healthy hypertension profile
healthy_hyper = {
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
result = engine.predict_hypertension(healthy_hyper)
assert result['risk_level'] == 'Low', f"Expected Low, got {result['risk_level']}"
print("✓ Healthy hypertension test passed")

# Test 4: High risk hypertension profile
high_risk_hyper = {
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
result = engine.predict_hypertension(high_risk_hyper)
assert result['risk_level'] == 'High', f"Expected High, got {result['risk_level']}"
print("✓ High risk hypertension test passed")

print("\n✅ All prediction tests passed!")
```

Run tests:
```bash
python test_predictions.py
```

### Phase 2: UI Testing (Desktop)

```bash
# Run app in debug mode
flet run app/main.py

# Test all user flows:
# 1. Welcome screen → Selection → Diabetes form → Results
# 2. Welcome screen → Selection → Hypertension form → Results
# 3. Test error handling (invalid inputs)
# 4. Test back navigation
# 5. Test educational content
```

### Phase 3: Mobile Testing (Android Emulator)

```bash
# Install Android Studio for emulator
# https://developer.android.com/studio

# Create virtual device (Pixel 6, Android 13)

# Install and test APK
adb install build/android/app/build/outputs/apk/release/app-release.apk

# Run app
adb shell am start -n com.healthrisk.checker/.MainActivity
```

### Phase 4: Real Device Testing

Test on at least 2 physical devices:
- 1 low-end device (Android 5.0-7.0)
- 1 modern device (Android 10+)

**Checklist:**
- [ ] App installs successfully
- [ ] No crash on startup
- [ ] Models load correctly
- [ ] All forms work
- [ ] Predictions display correctly
- [ ] Navigation works smoothly
- [ ] Text is readable on small screens
- [ ] Buttons are tappable
- [ ] Loading indicators show during prediction

### Phase 5: Performance Testing

**Target metrics:**
- App startup: < 3 seconds
- Model loading: < 2 seconds
- Prediction time: < 1 second
- APK size: < 50 MB

```bash
# Check APK size
ls -lh build/android/app/build/outputs/apk/release/app-release.apk

# If > 50MB, consider:
# - Using Android App Bundle (AAB)
# - Removing unused dependencies
# - Optimizing model files
```

---

## 🐛 Troubleshooting

### Issue: "Java not found" or "JAVA_HOME not set"

**Solution:**
```bash
# Windows - Set environment variable
setx JAVA_HOME "C:\Program Files\Java\jdk-17"

# Verify
echo %JAVA_HOME%
java -version
```

### Issue: "Android SDK not found"

**Solution:**
Flet downloads SDK automatically on first build. Wait 5-10 minutes.

Or manually set:
```bash
setx ANDROID_HOME "%LOCALAPPDATA%\Android\Sdk"
```

### Issue: Build freezes at "Packaging Python app"

**This was the original issue! Solutions:**

1. **Ensure pandas is removed from requirements.txt** ✅ (Done)

2. **Clean build cache:**
   ```bash
   # Delete build folder
   rmdir /s build
   
   # Rebuild
   flet build apk app/main.py
   ```

3. **Use --debug flag for faster iteration:**
   ```bash
   flet build apk --debug app/main.py
   ```

4. **If still stuck, use Web deployment instead** ✅ (Recommended)

### Issue: "Module not found: prediction_engine"

**Solution:**
Ensure you're running from project root:
```bash
cd C:\Users\Johnson\health-risk-predictor-v2
flet run app/main.py
```

### Issue: Models not loading on Android

**Solution:**
Models must be in correct path. Check:
```
health-risk-predictor-v2/
└── models/
    ├── diabetes_model.pkl
    ├── hypertension_model.pkl
    ├── scaler_diabetes.pkl
    └── scaler_hypertension.pkl
```

In `prediction_engine.py`, the path is:
```python
self.models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
```

### Issue: APK is too large (> 50MB)

**Solutions:**

1. **Use Android App Bundle (AAB):**
   ```bash
   flet build appbundle app/main.py
   ```
   AAB is 30-40% smaller than APK.

2. **Build separate APKs per CPU architecture:**
   ```bash
   flet build apk --target-arch arm64-v8a app/main.py
   ```

3. **Compress model files:**
   ```python
   # In notebook, retrain with smaller model
   # Or use model compression techniques
   ```

### Issue: App crashes on startup

**Debug:**
```bash
# Check logs
adb logcat | grep -i python

# Look for error messages
```

Common causes:
- Missing model files
- Incorrect file paths
- Dependency issues

---

## 📊 Deployment Comparison

| Feature | Android APK | Web (Flet) |
|---------|-------------|------------|
| Build Time | 10-20 min | Instant |
| Setup Complexity | High | Low |
| Distribution | Manual/Play Store | URL sharing |
| Updates | Require rebuild | Instant |
| Offline Support | ✅ Yes | ❌ No |
| Device Access | ✅ Full | ⚠️ Limited |
| Cost | Free (Play Store: $25) | Free |
| iOS Support | ❌ No | ✅ Yes |

---

## ✅ Pre-Launch Checklist

### For Android:

- [ ] All unit tests pass
- [ ] App runs on desktop
- [ ] APK builds successfully
- [ ] APK installs on test devices
- [ ] All predictions work correctly
- [ ] UI is responsive on different screen sizes
- [ ] Error handling works
- [ ] App icon and splash screen added
- [ ] Privacy policy created (required for Play Store)
- [ ] Medical disclaimer visible in app

### For Web:

- [ ] All unit tests pass
- [ ] App runs locally
- [ ] Published to Flet cloud
- [ ] URL works on mobile browser
- [ ] URL works on desktop browser
- [ ] All features functional
- [ ] Loading times acceptable

---

## 🎯 Recommended Deployment Path

**Phase 1: Quick Validation (Day 1)**
```bash
# Deploy to web first
flet publish app/main.py

# Share URL with stakeholders
# Get feedback quickly
```

**Phase 2: Android Build (Day 2-3)**
```bash
# After web validation, build Android APK
flet build apk app/main.py

# Test on multiple devices
# Fix any issues
```

**Phase 3: Production Release (Week 2)**
```bash
# Build AAB for Google Play
flet build appbundle app/main.py

# Submit to Play Store
# Wait for approval (2-7 days)
```

---

## 📞 Support Resources

- **Flet Documentation:** https://flet.dev/docs/
- **Flet Discord:** https://discord.gg/d74AqFp3Dx
- **Android Developers:** https://developer.android.com/
- **Google Play Console:** https://play.google.com/console

---

## 🎉 Success!

You now have a deployable health risk assessment app!

**Next Steps:**
1. Test thoroughly
2. Gather user feedback
3. Iterate and improve
4. Consider adding more health conditions
5. Add user history/saving features
6. Implement data export

**Good luck with your deployment!** 🚀
