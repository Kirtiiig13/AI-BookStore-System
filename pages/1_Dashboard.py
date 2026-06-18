import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

# =========================
# LOAD DATA
# =========================

books = pd.read_csv("data/books.csv")
customers = pd.read_csv("data/customers.csv")
sales = pd.read_csv("data/sales.csv")

# =========================
# DATA PREPARATION
# =========================

merged = pd.merge(sales, books, on="Book_ID")
merged["Revenue"] = merged["Quantity"] * merged["Price"]

# =========================
# TITLE
# =========================

st.title("📊 AI Book Store Analytics Dashboard")
st.markdown("Business Intelligence Dashboard for Sales, Inventory and Customer Insights")

# =========================
# FILTERS
# =========================

category_filter = st.selectbox(
    "📂 Filter Category",
    ["All"] + sorted(books["Category"].unique().tolist())
)

filtered = merged.copy()

if category_filter != "All":
    filtered = filtered[
        filtered["Category"] == category_filter
    ]

# =========================
# KPI CARDS
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📚 Books", len(books))

with col2:
    st.metric("👥 Customers", len(customers))

with col3:
    st.metric("🛒 Sales", len(filtered))

with col4:
    st.metric(
        "💰 Revenue",
        f"₹{filtered['Revenue'].sum():,.0f}"
    )

st.divider()

# =========================
# CHARTS ROW 1
# =========================

col1, col2 = st.columns(2)

with col1:

    st.subheader("💰 Revenue by Category")

    category_revenue = (
        filtered.groupby("Category")["Revenue"]
        .sum()
        .reset_index()
    )

    fig1 = px.pie(
        category_revenue,
        names="Category",
        values="Revenue",
        hole=0.4
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:

    st.subheader("📚 Top Selling Books")

    top_books = (
        filtered.groupby("Title")["Quantity"]
        .sum()
        .reset_index()
        .sort_values(
            by="Quantity",
            ascending=False
        )
        .head(10)
    )

    fig2 = px.bar(
        top_books,
        x="Quantity",
        y="Title",
        orientation="h"
    )

    st.plotly_chart(fig2, use_container_width=True)

# =========================
# CHARTS ROW 2
# =========================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📈 Revenue Trend")

    if "Date" in sales.columns:

        sales["Date"] = pd.to_datetime(
            sales["Date"]
        )

        trend = (
            sales.groupby("Date")["Quantity"]
            .sum()
            .reset_index()
        )

        fig3 = px.line(
            trend,
            x="Date",
            y="Quantity",
            markers=True
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )
    else:
        st.info("No Date column available.")

with col2:

    st.subheader("🏆 Top Customers")

    if "Customer_ID" in sales.columns:

        top_customers = (
            sales.groupby("Customer_ID")["Quantity"]
            .sum()
            .reset_index()
            .sort_values(
                by="Quantity",
                ascending=False
            )
            .head(10)
        )

        fig4 = px.bar(
            top_customers,
            x="Customer_ID",
            y="Quantity"
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

    else:
        st.info("Customer data unavailable.")

# =========================
# LOW STOCK ALERT
# =========================

st.subheader("⚠ Low Stock Alert")

low_stock = books[
    books["Stock"] < 20
]

if len(low_stock) > 0:
    st.dataframe(
        low_stock,
        use_container_width=True
    )
else:
    st.success("All books sufficiently stocked.")

# =========================
# CATEGORY REVENUE TABLE
# =========================

st.subheader("📋 Revenue Summary")

st.dataframe(
    category_revenue,
    use_container_width=True
)