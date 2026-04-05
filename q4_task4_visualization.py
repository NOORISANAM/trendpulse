import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("C:/Users/HP/Documents/GitHub/Data/trends_analysed.csv")
os.makedirs("outputs", exist_ok=True)

# CHART 1
top10 = df.nlargest(10, 'score').copy()
top10['short_title'] = top10['title'].str[:50]
plt.figure(figsize=(10, 6))
plt.barh(top10['short_title'], top10['score'], color='steelblue')
plt.xlabel("Score")
plt.title("Top 10 Stories by Score")
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()
print("Chart 1 saved!")

# CHART 2
cat = df['category'].value_counts()
colors = ['red','blue','green','orange','purple','brown']
plt.figure(figsize=(8, 5))
plt.bar(cat.index, cat.values, color=colors[:len(cat)])
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Stories per Category")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()
print("Chart 2 saved!")

# CHART 3
popular = df[df['is_popular'] == True]
not_popular = df[df['is_popular'] == False]
plt.figure(figsize=(8, 5))
plt.scatter(not_popular['score'], not_popular['score'], color='gray', label='Not Popular', alpha=0.5)
plt.scatter(popular['score'], popular['score'], color='red', label='Popular', alpha=0.7)
plt.xlabel("Score")
plt.ylabel("Score")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()
print("Chart 3 saved!")

# DASHBOARD
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("TrendPulse Dashboard")
axes[0].barh(top10['short_title'], top10['score'], color='steelblue')
axes[0].set_title("Top 10 Stories")
axes[1].bar(cat.index, cat.values, color=colors[:len(cat)])
axes[1].set_title("Stories per Category")
axes[2].scatter(not_popular['score'], not_popular['score'], color='gray', alpha=0.5)
axes[2].scatter(popular['score'], popular['score'], color='red', alpha=0.7)
axes[2].set_title("Score vs Comments")
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()
print("Dashboard saved!")