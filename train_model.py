# scripts/train_model.py

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# 1. Generate synthetic dataset
X, y = make_classification(n_samples=1000, n_features=10, 
                           n_informative=6, n_classes=2, 
                           random_state=42)

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 4. Evaluate
y_pred = clf.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# 5. Save the trained model
os.makedirs("../models", exist_ok=True)
joblib.dump(clf, "../models/heatwave_predictor.pkl")
print("\n✅ Model saved as 'heatwave_predictor.pkl'")
