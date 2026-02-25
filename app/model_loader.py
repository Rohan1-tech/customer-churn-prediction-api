import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_PATH = os.path.join(BASE_DIR, "artifacts")

model = joblib.load(os.path.join(ARTIFACT_PATH, "final_churn_model.joblib"))
scaler = joblib.load(os.path.join(ARTIFACT_PATH, "scaler.joblib"))
threshold = joblib.load(os.path.join(ARTIFACT_PATH, "threshold.joblib"))
feature_order = joblib.load(os.path.join(ARTIFACT_PATH, "feature_order.pkl"))