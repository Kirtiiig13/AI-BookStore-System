import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Segmentation", layout="wide")

st.title("👥 Customer Segmentation")

try:
    segments = pd.read_csv("reports/customer_segments.csv")

    st.dataframe(segments, use_container_width=True)

    cluster = segments["Cluster"].value_counts().reset_index()
    cluster.columns = ["Cluster", "Count"]

    fig = px.pie(cluster, values="Count", names="Cluster")
    st.plotly_chart(fig, use_container_width=True)

except:
    st.warning("Run segmentation model first and save customer_segments.csv")