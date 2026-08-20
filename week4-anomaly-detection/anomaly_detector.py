# anomaly_detector.py
import pandas as pd
from sklearn.ensemble import IsolationForest

# 1. Load the feature-engineered dataset from Week 3
input_file = "feature_engineered_evidence.csv"
df = pd.read_csv(input_file, parse_dates=["timestamp"])

# 2. Select numeric features for the Isolation Forest model
# We use hour_of_day and convert is_weekend to int (0 or 1)
features = ["hour_of_day"]
df["is_weekend_int"] = df["is_weekend"].astype(int)
features.append("is_weekend_int")

X = df[features]

# 3. Initialize and fit the Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
df["is_anomaly"] = model.fit_predict(X)

# Drop the temporary integer column if clean export is preferred, or keep it
df = df.drop(columns=["is_weekend_int"])

# 4. Save the results to the required output file
output_file = "anomalies_detected_evidence.csv"
df.to_csv(output_file, index=False)

print(f"Anomaly detection complete. Results saved to '{output_file}'.")
print("Anomaly distribution (-1 indicates anomaly, 1 indicates normal):")
print(df["is_anomaly"].value_counts())