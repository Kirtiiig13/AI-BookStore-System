import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customers", layout="wide")

customers = pd.read_csv("data/customers.csv")

st.title("👥 Customers")

st.dataframe(customers, use_container_width=True)