import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customers", layout="wide")

# Load Data
customers = pd.read_csv("data/customers.csv")

# =========================
# TITLE
# =========================

st.title("👥 Customer Analytics Dashboard")

# =========================
# KPI CARDS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Total Customers", len(customers))

with col2:
    if "Age" in customers.columns:
        st.metric("🎂 Average Age", f"{customers['Age'].mean():.0f}")

with col3:
    if "Gender" in customers.columns:
        top_gender = customers["Gender"].mode()[0]
        st.metric("🚻 Majority Gender", top_gender)

st.divider()

# =========================
# FILTERS
# =========================

col1, col2 = st.columns(2)

with col1:
    search = st.text_input(
        "🔍 Search Customer",
        placeholder="Search by Customer Name"
    )

with col2:
    if "Gender" in customers.columns:
        gender = st.selectbox(
            "🚻 Filter Gender",
            ["All"] + sorted(customers["Gender"].unique().tolist())
        )
    else:
        gender = "All"

# =========================
# FILTER LOGIC
# =========================

filtered = customers.copy()

if search and "Name" in customers.columns:
    filtered = filtered[
        filtered["Name"].astype(str).str.contains(
            search,
            case=False,
            na=False
        )
    ]

if gender != "All":
    filtered = filtered[
        filtered["Gender"] == gender
    ]

# =========================
# CHARTS
# =========================

col1, col2 = st.columns(2)

with col1:
    if "Gender" in customers.columns:
        st.subheader("🚻 Gender Distribution")

        gender_count = (
            customers["Gender"]
            .value_counts()
            .reset_index()
        )

        gender_count.columns = ["Gender", "Count"]

        fig = px.pie(
            gender_count,
            names="Gender",
            values="Count",
            hole=0.4
        )

        st.plotly_chart(fig, use_container_width=True)

with col2:
    if "Age" in customers.columns:
        st.subheader("🎂 Age Distribution")

        fig = px.histogram(
            customers,
            x="Age",
            nbins=10
        )

        st.plotly_chart(fig, use_container_width=True)

# =========================
# CUSTOMER TABLE
# =========================

st.subheader("📋 Customer Records")

st.write(f"Showing **{len(filtered)}** customers")

st.dataframe(
    filtered,
    use_container_width=True
)

# =========================
# DOWNLOAD CSV
# =========================

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Customer Data",
    csv,
    "customers.csv",
    "text/csv"
)