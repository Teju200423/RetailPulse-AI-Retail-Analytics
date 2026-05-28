import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="RetailPulse Dashboard", layout="wide")

st.title("🛍️ RetailPulse - AI Powered Retail Analytics")

uploaded_file = st.file_uploader("Upload Cleaned Retail Dataset")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.sidebar.title("Navigation")

    option = st.sidebar.radio(
        "Go To",
        [
            "Dataset Overview",
            "Sales Analytics",
            "Customer Segmentation",
            "Churn Analysis",
            "Correlation Analysis"
        ]
    )

    # DATASET OVERVIEW
    if option == "Dataset Overview":

        st.subheader("Dataset Preview")
        st.write(df.head())

        st.subheader("Dataset Shape")
        st.write(df.shape)

        st.subheader("Dataset Columns")
        st.write(df.columns)

    # SALES ANALYTICS
    elif option == "Sales Analytics":

        st.subheader("Top 10 Countries by Sales")

        country_sales = df.groupby('Country')['TotalAmount'].sum().sort_values(ascending=False).head(10)

        fig, ax = plt.subplots(figsize=(10,5))

        country_sales.plot(kind='bar', ax=ax)

        plt.title("Top Countries by Sales")
        plt.xlabel("Country")
        plt.ylabel("Sales")

        st.pyplot(fig)

        st.subheader("Monthly Sales Trend")

        monthly_sales = df.groupby('Month')['TotalAmount'].sum()

        fig2, ax2 = plt.subplots(figsize=(10,5))

        monthly_sales.plot(marker='o', ax=ax2)

        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Sales")

        st.pyplot(fig2)

    # CUSTOMER SEGMENTATION
    elif option == "Customer Segmentation":

        st.subheader("Top Customers")

        top_customers = df.groupby('CustomerID')['TotalAmount'].sum().sort_values(ascending=False).head(10)

        fig3, ax3 = plt.subplots(figsize=(10,5))

        top_customers.plot(kind='bar', ax=ax3)

        plt.title("Top Customers")
        plt.xlabel("Customer ID")
        plt.ylabel("Sales")

        st.pyplot(fig3)

    # CHURN ANALYSIS
    elif option == "Churn Analysis":

        st.subheader("Customer Purchase Distribution")

        fig4, ax4 = plt.subplots(figsize=(10,5))

        df['TotalAmount'].hist(bins=30, ax=ax4)

        plt.title("Purchase Distribution")

        st.pyplot(fig4)

    # CORRELATION ANALYSIS
    elif option == "Correlation Analysis":

        st.subheader("Correlation Heatmap")

        corr = df[['Quantity','UnitPrice','TotalAmount']].corr()

        fig5, ax5 = plt.subplots(figsize=(8,5))

        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax5)

        st.pyplot(fig5)

    st.success("RetailPulse Dashboard Loaded Successfully!")