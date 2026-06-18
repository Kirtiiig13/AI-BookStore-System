import streamlit as st
import pandas as pd

st.set_page_config(page_title="Books", layout="wide")

books = pd.read_csv("data/books.csv")

st.title("📚 Books Inventory")

search = st.text_input("Search Book")

filtered = books.copy()

if search:
    filtered = filtered[filtered["Title"].str.contains(search, case=False, na=False)]

category = st.selectbox("Filter Category", ["All"] + list(books["Category"].unique()))

if category != "All":
    filtered = filtered[filtered["Category"] == category]

st.dataframe(filtered, use_container_width=True)

csv = filtered.to_csv(index=False)

st.download_button("Download CSV", csv, "books.csv", "text/csv")