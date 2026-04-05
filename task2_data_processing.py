import pandas as pd

# STEP 1 - Load JSON
df = pd.read_json("trends_2026004.json")
print(f"Loaded {len(df)} stories from trends_2026004.json")

# STEP 2 - Clean Data
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

df["score"] = df["score"].astype(int)

df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

df["title"] = df["title"].str.strip()

# STEP 3 - Save CSV
df.to_csv("trends_clean.csv", index=False)
print(f"Saved {len(df)} rows to trends_clean.csv")

print("\nStories per category:")
print(df["category"].value_counts())