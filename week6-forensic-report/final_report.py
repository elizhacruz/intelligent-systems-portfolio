import os
import matplotlib.pyplot as plt
import pandas as pd

anomalies_df = pd.read_csv("anomalies_detected_evidence.csv")
entities_df = pd.read_csv("extracted_entities.csv")

event_counts = anomalies_df["event_type"].value_counts()

plt.figure(figsize=(8, 6))
event_counts.plot(kind="bar", color="skyblue")
plt.title("Distribution of Event Types (Anomalies)")
plt.xlabel("Event Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()

image_filename = "event_distribution.png"
plt.savefig(image_filename)
plt.close()

report_content = f"""# Forensic Investigation Report

## Executive Summary
This report summarizes the findings from the digital forensic investigation. Over the course of the analysis, evidence was acquired, analyzed for anomalies, and processed for key entities to reconstruct the case narrative.

## Methodology
The investigation utilized a complete forensic workflow:
1. Data acquisition and preprocessing (`raw_evidence.csv` to `cleaned_evidence.csv`)[cite: 1].
2. Feature engineering and anomaly detection (`anomalies_detected_evidence.csv`)[cite: 1].
3. Named entity recognition on textual evidence (`extracted_entities.csv`)[cite: 1].
4. Automated reporting and visualization generation via Python and Matplotlib.

## Key Findings
- Total anomalies detected: {len(anomalies_df)}
- Total extracted entities: {len(entities_df)}
- Unique event types recorded: {", ".join(event_counts.index.tolist())}
- The event distribution chart below highlights the frequency of event types observed during the investigation timeline.

## Visualizations
![Event Distribution]({image_filename})
"""

with open("forensic_report.md", "w") as f:
  f.write(report_content)

print(
    "Successfully generated event_distribution.png and forensic_report.md for"
    " Week 6!"
)