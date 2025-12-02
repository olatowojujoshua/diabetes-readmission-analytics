# Diabetes Readmission Analytics

This project integrates survival analysis of diabetic patient readmissions with sentiment analysis of hospital reviews using a cloud-based pipeline on Databricks.

## Features
- Spark-based data processing
- Kaplan–Meier survival analysis
- NLP sentiment classification using TF-IDF + Logistic Regression
- Visualization dashboards (KM curve, sentiment pie chart, wordcloud)
- Clean, modular code structure

## Technology Stack
- Databricks (Spark)
- Python (Pandas, scikit-learn, lifelines)
- NLP (TF-IDF, Logistic Regression)
- Matplotlib / Seaborn

## How to Run
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Open notebooks in Jupyter or Databricks
4. Run cells in order

## Data
Datasets are NOT included. See data/README-data.md.
