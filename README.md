# 📊 End-to-End A/B Testing Analysis

An end-to-end Product Analytics project that evaluates whether a new marketing strategy should be rolled out using statistical hypothesis testing, SQL, and Python.

---

## 📌 Business Problem

A company conducted an A/B test to compare two marketing strategies:

- **Control Group (ad):** Existing advertisement campaign
- **Treatment Group (psa):** Public Service Announcement (PSA)

The objective is to determine whether the new treatment should replace the current advertisement strategy based on user conversion performance.

---

## 🎯 Project Objectives

- Calculate conversion rates for control and treatment groups.
- Perform SQL-based KPI analysis.
- Validate results using statistical hypothesis testing.
- Check whether the experiment had sufficient sample size.
- Analyze user segments based on advertisement exposure.
- Provide a business recommendation supported by data.

---

## 📂 Dataset

**Dataset:** Marketing A/B Testing (Kaggle)

### Features

| Column | Description |
|---------|-------------|
| user id | Unique user identifier |
| test group | Control (ad) or Treatment (psa) |
| converted | Whether the user converted |
| total ads | Number of advertisements viewed |
| most ads day | Day with the highest ad exposure |
| most ads hour | Hour with the highest ad exposure |

---

# 🛠️ Tech Stack

- Python
- SQL (SQLite)
- Pandas
- Matplotlib
- SciPy
- Statsmodels

---

# 📁 Project Structure

```text
AB_Test_Project
│
├── data
│   └── marketing_AB.csv
│
├── outputs
│   ├── conversion_rate.png
│   ├── day_analysis.png
│   ├── hour_analysis.png
│   ├── segment_analysis.png
│   └── recommendation.txt
│
├── sql
│   ├── conversion_rate.sql
│   ├── day_analysis.sql
│   ├── hour_analysis.sql
│   ├── segment_analysis.sql
│   └── sample_size.sql
│
├── src
│   ├── analysis.py
│   ├── database.py
│   ├── report.py
│   ├── statistics.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔄 Project Workflow

```text
Marketing Dataset
        │
        ▼
SQLite Database
        │
        ▼
SQL Queries
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Statistical Testing
        │
        ▼
Power Analysis
        │
        ▼
Confidence Interval
        │
        ▼
User Segmentation
        │
        ▼
Business Recommendation
```

---

# 📈 SQL Analysis

The project performs SQL-based analysis to calculate:

- Conversion rate
- Total users
- Total conversions
- Day-wise conversion
- Hour-wise conversion
- User segmentation based on advertisement exposure

Example SQL Query:

```sql
SELECT
    "test group",
    COUNT(*) AS total_users,
    SUM(converted) AS conversions,
    ROUND(AVG(converted) * 100, 2) AS conversion_rate
FROM marketing
GROUP BY "test group";
```

---

# 📊 Statistical Analysis

The following statistical methods were used:

- Two-Proportion Z-Test
- Chi-Square Test
- Power Analysis (Sample Size Adequacy)
- 95% Confidence Interval
- Absolute Lift
- Relative Lift

---

# 📉 Results

### Conversion Rate

| Group | Conversion Rate |
|--------|----------------:|
| Ad (Control) | **2.55%** |
| PSA (Treatment) | **1.79%** |

---

### Lift Analysis

- **Absolute Lift:** -0.77%
- **Relative Lift:** -30.11%

---

### Statistical Tests

| Metric | Value |
|---------|-------|
| Z-Test | Significant |
| Chi-Square Test | Significant |
| Sample Size | Adequate |
| 95% Confidence Interval | [-0.94%, -0.60%] |

---

# 👥 User Segment Analysis

Users were grouped based on advertisement exposure:

- Low Exposure (≤10 ads)
- Medium Exposure (11–25 ads)
- High Exposure (>25 ads)

The analysis showed that the treatment performed substantially worse for users with high advertisement exposure, while differences for the low- and medium-exposure groups were comparatively small.

---

# 💡 Business Recommendation

## ❌ Do Not Ship the Treatment

### Reason

- The treatment reduced the conversion rate from **2.55%** to **1.79%**.
- Relative conversion decreased by **30.11%**.
- Statistical testing confirmed that the decrease is significant.
- The confidence interval remained entirely below zero, indicating a consistent negative effect.
- The experiment included over **588,000 users**, far exceeding the required sample size.

---

# 📷 Project Outputs

The project automatically generates:

- Conversion Rate Chart
- Day-wise Analysis
- Hour-wise Analysis
- User Segment Analysis
- Executive Recommendation Report

---

# 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/ab-testing-analysis.git
```

### Navigate to the project

```bash
cd ab-testing-analysis
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python3 main.py
```

---

# 📚 Key Learnings

- Designing and evaluating A/B tests
- Writing analytical SQL queries
- Statistical hypothesis testing
- Power analysis and confidence intervals
- Data visualization
- Translating statistical results into business recommendations

---

# 👤 Author

**Simran Kaur**

Electronics and Computer Engineering  
Thapar Institute of Engineering and Technology

---


