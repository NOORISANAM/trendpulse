import pandas as pd
import numpy as np

# STEP 1 - Load CSV
df = pd.read_csv("C:/Users/HP/Documents/GitHub/Data/data/data/data/trends_clean.csv")
print("First 5 rows:")
print(df.head())

print(f"\nLoaded data: {df.shape}")
print(f"Average score   : {df['score'].mean():.0f}")

# STEP 2 - NumPy Stats
scores = np.array(df['score'])

print("\n--- NumPy Stats ---")
print(f"Mean score   : {np.mean(scores):.0f}")
print(f"Median score : {np.median(scores):.0f}")
print(f"Std deviation: {np.std(scores):.0f}")
print(f"Max score    : {np.max(scores)}")
print(f"Min score    : {np.min(scores)}")

top_category = df['category'].value_counts().idxmax()
top_count = df['category'].value_counts().max()
print(f"\nMost stories in: {top_category} ({top_count} stories)")

# STEP 3 - New Columns
df['engagement'] = df['score'] / (df['score'] + 1)
df['is_popular'] = df['score'] > df['score'].mean()

# STEP 4 - Save CSV
df.to_csv("trends_analysed.csv", index=False)
print("\nSaved to trends_analysed.csv")