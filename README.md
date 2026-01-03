# Data-Science---Final_Project
# EDA Project – UPI Transactions Analysis

## Project Overview
This project performs a complete **Exploratory Data Analysis (EDA)** on the UPI transaction dataset to uncover trends, growth patterns, and insights. The analysis includes data cleaning, transformation, visualization, probability analysis, basic modeling (K-Means clustering), and an interactive dashboard using Plotly Dash.

The goal is to make complex UPI transaction data **easy to understand**, even for non-technical users, and provide actionable insights.

## Dataset
- **File:** `upi_data_enhanced.csv`
- **Description:** UPI transaction data including the number of banks live on UPI, transaction volume, transaction value, average transaction value, and month-on-month growth metrics.
- **Source:** Provided for the final project (college dataset).

## Folder Structure

EDA_UPI_PROJECT/
├── data/ # Original dataset
│ └── upi_data_enhanced.csv
├── modules/ # Python modules for EDA workflow
│ ├── data_import.py
│ ├── data_cleaning.py
│ ├── transformation.py
│ ├── stats_analysis.py
│ ├── basic_visualization.py
│ ├── advanced_visualization.py
│ ├── probability_analysis.py
│ ├── modeling.py
│ └── interactive_visualization.py
├── outputs/ # Cleaned data and generated outputs
│ └── upi_cleaned_data.csv
├── main.py # Main script to run entire EDA project
└── README.md # Project documentation (this file) 

## Steps Performed

1. **Import Data**
   - Loaded dataset into Python
   - Displayed first few rows and checked structure

2. **Data Cleaning**
   - Removed duplicates and handled missing values
   - Detected and removed outliers

3. **Data Transformation**
   - Normalization and standardization of numeric columns

4. **Descriptive Statistics**
   - Calculated mean, median, mode, standard deviation, etc.
   - Summarized key patterns

5. **Basic Visualization**
   - Line plots, bar charts, histograms

6. **Advanced Visualization**
   - Pair plots, heatmaps, violin plots
   - Correlation and covariance analysis

7. **Probability Analysis**
   - Visualized probability distributions

8. **Modeling**
   - K-Means clustering to segment transactions
   - Basic insights from clusters

9. **Interactive Dashboard**
   - Developed using Plotly Dash
   - Users can select columns from dropdown to explore trends
   - Visualizes:
     - Number of Banks live on UPI
     - Transaction Volume & Value
     - Month-on-Month growth
     - Cluster distribution
   - Allows dynamic trend analysis

## Key Insights

- UPI transactions **volume and value are increasing** steadily.
- Month-on-month growth shows **short-term fluctuations**.
- Most banks are steadily live on UPI, indicating **widespread adoption**.
- Clustering revealed **distinct behavioral patterns** in transactions.
- The interactive dashboard makes analysis accessible even to **non-technical users**.

## How to Run

1. Make sure **Python** and required libraries are installed:
   pip install pandas matplotlib seaborn plotly dash scikit-learn
2.Open VS Code or terminal and navigate to project folder:
    cd EDA_UPI_PROJECT
3.Run the main script:
    python main.py
4.For the interactive dashboard:
    Open the link printed in terminal (default: http://127.0.0.1:8050) in a browser.

## Tools & Libraries
Python 3
Pandas
Matplotlib
Seaborn
Plotly & Plotly Dash
Scikit-learn (for K-Means clustering)

## Author
S.Dhavanithi
MCA Student
Final Project: EDA on UPI Transaction Dataset

