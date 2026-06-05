# Task 02: Data Cleaning & Advanced EDA
# Name: Ajju

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style
plt.style.use('dark_background')
sns.set_style("darkgrid")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/bank-full.csv", sep=';')

# ---------------- CLEANING ----------------
# Replace 'unknown' with safe string
df.replace("unknown", "Unknown", inplace=True)

# Convert target to numeric
df['y_numeric'] = df['y'].map({'yes': 1, 'no': 0})

# ---------------- BASIC INFO ----------------
print("Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

# ---------------- KPI ----------------
print("\nKPI Metrics:")
print("Total Customers:", len(df))
print("Subscribed:", df['y'].value_counts()['yes'])
print("Not Subscribed:", df['y'].value_counts()['no'])
print("Subscription Rate:", round(df['y_numeric'].mean()*100, 2), "%")

# ---------------- VISUALIZATIONS ----------------

# 1. Subscription Count
plt.figure()
sns.countplot(x='y', data=df)
plt.title("Subscription Count")
plt.savefig("output/1_subscription.png", dpi=300)
plt.close()

# 2. Age Distribution
plt.figure()
sns.histplot(df['age'], bins=30)
plt.title("Age Distribution")
plt.savefig("output/2_age.png", dpi=300)
plt.close()

# 3. Job vs Subscription
plt.figure(figsize=(12,6))
sns.countplot(x='job', hue='y', data=df)
plt.xticks(rotation=45)
plt.title("Job vs Subscription")
plt.savefig("output/3_job.png", dpi=300)
plt.close()

# 4. Balance vs Subscription
plt.figure()
sns.boxplot(x='y', y='balance', data=df)
plt.title("Balance vs Subscription")
plt.savefig("output/4_balance.png", dpi=300)
plt.close()

# 5. Education vs Subscription
plt.figure()
sns.countplot(x='education', hue='y', data=df)
plt.title("Education vs Subscription")
plt.savefig("output/5_education.png", dpi=300)
plt.close()

# 6. Month vs Subscription
plt.figure(figsize=(10,5))
sns.countplot(x='month', hue='y', data=df)
plt.title("Month vs Subscription")
plt.savefig("output/6_month.png", dpi=300)
plt.close()

# 7. Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes(include=['int64','float64']).corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("output/7_heatmap.png", dpi=300)
plt.close()

print("🔥 EDA Completed Successfully!")