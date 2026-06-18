import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

books = pd.read_csv("data/books.csv")
customers = pd.read_csv("data/customers.csv")
sales = pd.read_csv("data/sales.csv")

merged = pd.merge(sales, books, on="Book_ID")
merged["Revenue"] = merged["Quantity"] * merged["Price"]

st.title("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Books", len(books))
col2.metric("Total Customers", len(customers))
col3.metric("Total Sales", len(sales))
col4.metric("Total Revenue", f"₹{merged['Revenue'].sum():,.0f}")

st.subheader("Revenue by Category")

category_revenue = merged.groupby("Category")["Revenue"].sum().reset_index()

fig = px.bar(category_revenue, x="Category", y="Revenue")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Top Selling Books")

top_books = merged.groupby("Title")["Quantity"].sum().reset_index()
top_books = top_books.sort_values(by="Quantity", ascending=False).head(10)

fig2 = px.bar(top_books, x="Title", y="Quantity")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Low Stock Books")

low_stock = books[books["Stock"] < 20]
st.dataframe(low_stock, use_container_width=True)