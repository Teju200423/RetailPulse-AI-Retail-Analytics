# RetailPulse - AI Powered Retail Analytics

## Overview

RetailPulse is an AI-powered retail analytics project developed to analyze retail transaction data and generate business insights using data science and machine learning techniques. The project focuses on customer behavior analysis, sales forecasting, churn prediction, inventory optimization, and interactive dashboard visualization.

The project was implemented using Python, machine learning libraries, time-series forecasting techniques, and Streamlit dashboard technology.

---

# Objectives

* Analyze retail sales transaction data
* Perform exploratory data analysis (EDA)
* Identify customer purchasing patterns
* Segment customers using clustering algorithms
* Forecast future sales demand
* Predict customer churn behavior
* Optimize inventory planning using forecasted demand
* Build an interactive analytics dashboard

---

# Dataset Information

The dataset contains retail transaction information including:

* Invoice details
* Product information
* Customer details
* Quantity purchased
* Unit price
* Invoice date
* Country information

The dataset was cleaned and processed before analysis.

---

# Technologies Used

## Programming Language

* Python

## Data Processing

* Pandas
* NumPy

## Data Visualization

* Matplotlib
* Seaborn

## Machine Learning

* Scikit-learn
* XGBoost
* DBSCAN
* KMeans

## Time-Series Forecasting

* Prophet
* Statsmodels

## Explainable AI

* SHAP

## Dashboard

* Streamlit

## Deployment & DevOps

* Docker
* Kubernetes

---

# Project Workflow

## 1. Data Cleaning & Preprocessing

* Missing value handling
* Duplicate removal
* Data type conversion
* Feature engineering
* Revenue calculation

## 2. Exploratory Data Analysis (EDA)

* Sales trend analysis
* Country-wise sales analysis
* Correlation heatmap
* Distribution analysis
* Outlier detection

## 3. Customer Segmentation

* RFM Analysis
* KMeans Clustering
* DBSCAN Clustering

## 4. Demand Forecasting

* Time-series preparation
* Prophet forecasting model
* Sales trend prediction

## 5. Churn Prediction

* Customer churn analysis
* XGBoost classification model
* Feature importance analysis
* SHAP explainability

## 6. Inventory Optimization

* Forecast-based stock estimation
* Inventory recommendation analysis

## 7. Dashboard Development

* Interactive Streamlit dashboard
* Sales analytics visualization
* Customer analytics dashboard
* Correlation analysis

---

# Features

* Interactive retail analytics dashboard
* Customer segmentation analysis
* Demand forecasting system
* Churn prediction model
* Inventory optimization logic
* Feature importance analysis
* SHAP explainability
* Data visualization and reporting

---

# Project Structure

Retail Pulse Project/

├── EDA_RetailPulse.ipynb
├── cleaned_retail_data.csv
├── simple_dashboard.py
├── Dockerfile
├── deployment.yaml
├── requirements.txt
├── README.md

---

# How to Run the Project

## Step 1: Install Dependencies

pip install -r requirements.txt

## Step 2: Run Streamlit Dashboard

python -m streamlit run simple_dashboard.py

## Step 3: Upload Dataset

Upload the cleaned_retail_data.csv file inside the dashboard.

---

# Results

The project successfully identified customer purchasing patterns, generated future sales forecasts, predicted customer churn behavior, and provided inventory optimization insights using machine learning and data analytics techniques.

---

# Future Enhancements

* LSTM-based forecasting
* Real-time data streaming
* Cloud deployment on AWS/GCP
* CI/CD pipeline integration
* Advanced monitoring and alert systems
* Real-time inventory tracking

---

# Conclusion

RetailPulse demonstrates a complete end-to-end retail analytics pipeline integrating data science, machine learning, forecasting, customer analytics, and dashboard visualization. The project provides meaningful business insights that can support retail decision-making and operational optimization.
