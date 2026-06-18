import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Books Inventory", layout="wide")

# Load Data
books = pd.read_csv("data/books.csv")

# =========================
# PAGE TITLE
# =========================

st.title("📚 Books Inventory Dashboard")

# =========================
# KPI CARDS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Total Books", len(books))

with col2:
    st.metric("💰 Average Price", f"₹{books['Price'].mean():.0f}")

with col3:
    low_stock = len(books[books["Stock"] < 20])
    st.metric("⚠ Low Stock Books", low_stock)

st.divider()

# =========================
# FILTERS
# =========================

col1, col2 = st.columns(2)

with col1:
    search = st.text_input(
        "🔍 Search Book",
        placeholder="Search by Title, Author or Category"
    )

with col2:
    category = st.selectbox(
        "📂 Filter Category",
        ["All"] + sorted(books["Category"].unique().tolist())
    )

# Price Range Filter
price_range = st.slider(
    "💰 Price Range",
    int(books["Price"].min()),
    int(books["Price"].max()),
    (
        int(books["Price"].min()),
        int(books["Price"].max())
    )
)

# =========================
# FILTER LOGIC
# =========================

filtered = books.copy()

if search:
    filtered = filtered[
        filtered["Title"].str.contains(search, case=False, na=False)
        |
        filtered["Author"].str.contains(search, case=False, na=False)
        |
        filtered["Category"].str.contains(search, case=False, na=False)
    ]

if category != "All":
    filtered = filtered[
        filtered["Category"] == category
    ]

filtered = filtered[
    (filtered["Price"] >= price_range[0])
    &
    (filtered["Price"] <= price_range[1])
]

# =========================
# CATEGORY CHART
# =========================

st.subheader("📊 Category Distribution")

category_count = books["Category"].value_counts().reset_index()
category_count.columns = ["Category", "Count"]

fig = px.pie(
    category_count,
    names="Category",
    values="Count",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# BOOK TABLE
# =========================

st.subheader("📖 Books List")

st.write(f"Showing **{len(filtered)}** books")

st.dataframe(
    filtered,
    use_container_width=True
)

# =========================
# LOW STOCK SECTION
# =========================

st.subheader("⚠ Low Stock Books")

low_stock_books = books[
    books["Stock"] < 20
]

if len(low_stock_books) > 0:
    st.dataframe(
        low_stock_books,
        use_container_width=True
    )
else:
    st.success("No low stock books found.")

# =========================
# DOWNLOAD
# =========================

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Filtered CSV",
    csv,
    "books_inventory.csv",
    "text/csv"
)