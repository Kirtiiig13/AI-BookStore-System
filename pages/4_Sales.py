import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales", layout="wide")

sales = pd.read_csv("data/sales.csv")

st.title("💰 Sales Data")

sales["Date"] = pd.to_datetime(sales["Date"])

st.dataframe(sales, use_container_width=True)

monthly = sales.groupby(sales["Date"].dt.to_period("M"))["Quantity"].sum()
monthly.index = monthly.index.astype(str)

st.subheader("Monthly Sales Trend")
st.line_chart(monthly)