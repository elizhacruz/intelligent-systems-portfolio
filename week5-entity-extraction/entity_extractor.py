# entity_extractor.py
import pandas as pd
import spacy

# Load the spaCy English language model
# Make sure you ran: python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# 1. Load the anomalies dataset from Week 4
input_file = "anomalies_detected_evidence.csv"
df = pd.read_csv(input_file)

extracted_data = []

# 2. Iterate through rows and extract entities from the 'message' column
for index, row in df.iterrows():
  text = str(row.get("message", ""))
  doc = nlp(text)
  for ent in doc.ents:
    extracted_data.append(
        {
            "row_index": index,
            "timestamp": row.get("timestamp"),
            "event_type": row.get("event_type"),
            "entity_text": ent.text,
            "entity_label": ent.label_,
        }
    )

# 3. Create a DataFrame from the extracted entities and save to CSV
entities_df = pd.DataFrame(extracted_data)
output_file = "extracted_entities.csv"
entities_df.to_csv(output_file, index=False)

print(
    f"Entity extraction complete. Found {len(entities_df)} entities. Saved to"
    f" '{output_file}'."
)
if not entities_df.empty:
  print("\nSample extracted entities:")
  print(entities_df.head())

  