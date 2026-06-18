import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="AI Book Store",
    page_icon="📚",
    layout="wide"
)

# ========================
# HERO SECTION
# ========================

st.title("📚 AI Powered Book Store Management System")

st.markdown(
    """
    ### 🚀 Welcome to your Smart Book Store Dashboard  
    Manage books, customers, sales and AI insights in one place.
    """
)

st.divider()

# ========================
# QUICK STATS UI (STATIC HOME UI)
# ========================

col1, col2, col3 = st.columns(3)

col1.metric("📚 Modules", "6")
col2.metric("🤖 AI Features", "2")
col3.metric("📊 Dashboards", "1")

st.divider()

# ========================
# FEATURES SECTION
# ========================

st.subheader("✨ System Features")

st.markdown("""
- 📊 Business Analytics Dashboard  
- 📚 Book Inventory Management  
- 👥 Customer Management  
- 💰 Sales Tracking  
- 🤖 AI Recommendation System  
- 👥 Customer Segmentation (ML)  
""")

st.divider()

# ========================
# GUIDE SECTION
# ========================

st.subheader("👉 How to Use")

st.info("""
Use the sidebar on the left to navigate:
- Dashboard → Analytics
- Books → Inventory system
- Customers → Customer data
- Sales → Sales trends
- Recommendations → AI book suggestions
- Segmentation → ML customer grouping
""")

st.success("Your system is running successfully 🎉")