# Task 02: Dashboard (Final Fixed Version)
# Name: Ajju

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Bank Dashboard", layout="wide")

st.title("📊 Bank Marketing Dashboard")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/bank-full.csv", sep=';')

# ---------------- CLEANING ----------------
df.replace("unknown", "Unknown", inplace=True)
df['y_numeric'] = df['y'].map({'yes': 1, 'no': 0})

# ---------------- KPI ----------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("Subscribed", df['y'].value_counts()['yes'])
col3.metric("Subscription Rate", f"{round(df['y_numeric'].mean()*100,2)}%")

# ---------------- FILTER ----------------
st.sidebar.header("🔍 Filters")

job_filter = st.sidebar.multiselect(
    "Select Job",
    sorted(df['job'].unique())
)

# Apply filter safely
if len(job_filter) > 0:
    df = df[df['job'].isin(job_filter)]

# ---------------- CHARTS ----------------

# Row 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("Subscription Count")
    fig, ax = plt.subplots()
    sns.countplot(x='y', data=df, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['age'], bins=30, ax=ax)
    st.pyplot(fig)

# Row 2
col3, col4 = st.columns(2)

with col3:
    st.subheader("Job vs Subscription")
    fig, ax = plt.subplots()
    sns.countplot(x='job', hue='y', data=df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col4:
    st.subheader("Balance vs Subscription")
    fig, ax = plt.subplots()
    sns.boxplot(x='y', y='balance', data=df, ax=ax)
    st.pyplot(fig)

# Row 3
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10,5))
sns.heatmap(df.select_dtypes(include=['int64','float64']).corr(), annot=True, ax=ax)
st.pyplot(fig)

st.success("🔥 Dashboard Running Successfully!")