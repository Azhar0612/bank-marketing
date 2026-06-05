# 📊 Bank Marketing EDA & Dashboard

## 🔍 Project Overview

This project focuses on performing **Data Cleaning, Exploratory Data Analysis (EDA), and building an Interactive Dashboard** using the Bank Marketing dataset.

The goal is to analyze customer data and identify patterns that influence whether a client subscribes to a term deposit.

---

## 📁 Dataset

* Dataset: Bank Marketing Dataset
* Source: UCI Machine Learning Repository
* Records: 45,000+ customer entries
* Target Variable: `y` (Subscription: Yes/No)

---

## ⚙️ Tools & Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit (for dashboard)

---

## 🧹 Data Cleaning

* Replaced `"unknown"` values with `"Unknown"` for better handling
* Converted categorical target variable into numeric format
* Verified missing values and ensured data consistency

---

## 📊 Exploratory Data Analysis (EDA)

### Key Visualizations:

* 📌 Subscription Count (Yes/No)
* 📌 Age Distribution
* 📌 Job vs Subscription
* 📌 Balance vs Subscription (Boxplot)
* 📌 Education vs Subscription
* 📌 Monthly Trends
* 📌 Correlation Heatmap

---

## 📈 Key Insights

* Customers with higher account balance tend to subscribe more
* Certain job categories show higher subscription rates
* Subscription trends vary across months
* Age distribution shows most customers are middle-aged

---

## 🖥️ Interactive Dashboard

An interactive dashboard was built using **Streamlit** to simulate a **Power BI–style experience**.

### Features:

* 📊 KPI Metrics (Total Customers, Subscription Rate)
* 🔍 Filters (Job-based filtering)
* 📈 Multiple charts in grid layout
* 🔥 Real-time interaction

---

## 📂 Project Structure

```bash
task_2/
│
├── data/
│   └── bank-full.csv
│
├── output/
│   ├── charts (EDA outputs)
│
├── main.py          # EDA & Visualization
├── dashboard.py     # Streamlit Dashboard
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install pandas matplotlib seaborn streamlit
```

### 2. Run EDA

```bash
python main.py
```

### 3. Run Dashboard

```bash
streamlit run dashboard.py
```

---

## 🎯 Conclusion

This project demonstrates how raw data can be transformed into meaningful insights through **data cleaning, analysis, and visualization**, and how those insights can be presented using an interactive dashboard.

---

## 👤 Author

Ajju

---

## 🚀 Future Improvements

* Add more filters (education, loan, etc.)
* Deploy dashboard online
* Integrate machine learning prediction model
