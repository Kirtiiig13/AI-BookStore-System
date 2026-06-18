import streamlit as st
import pandas as pd

st.set_page_config(page_title="Books", layout="wide")

# Load Data
books = pd.read_csv("data/books.csv")

# Title
st.title("📚 Books Inventory")

# Metrics
st.metric("Total Books", len(books))

# Search Box
search = st.text_input(
    "🔍 Search Book",
    placeholder="Search by Title, Author, or Category"
)

# Start with full dataset
filtered = books.copy()

# Search Logic
if search:
    filtered = filtered[
        filtered["Title"].str.contains(search, case=False, na=False)
        |
        filtered["Author"].str.contains(search, case=False, na=False)
        |
        filtered["Category"].str.contains(search, case=False, na=False)
    ]

# Category Filter
category = st.selectbox(
    "📂 Filter Category",
    ["All"] + sorted(books["Category"].unique().tolist())
)

if category != "All":
    filtered = filtered[filtered["Category"] == category]

# Show Results Count
st.write(f"📖 Showing {len(filtered)} books")

# Display Data
st.dataframe(filtered, use_container_width=True)

# Download Button
csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name="filtered_books.csv",
    mime="text/csv"
)