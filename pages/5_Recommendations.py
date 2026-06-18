import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Recommendations", layout="wide")

# =========================
# LOAD DATA
# =========================

from src.db_helper import get_books

books = get_books()

# =========================
# RECOMMENDATION FUNCTION
# =========================

@st.cache_data
def generate_similarity():
    data = books.copy()

    data["features"] = (
        data["Title"].fillna("") + " " +
        data["Author"].fillna("") + " " +
        data["Category"].fillna("")
    )

    tfidf = TfidfVectorizer(stop_words="english")
    matrix = tfidf.fit_transform(data["features"])

    similarity = cosine_similarity(matrix)

    return data, similarity

data, similarity = generate_similarity()

def recommend(book_title):
    try:
        idx = data[data["Title"] == book_title].index[0]
    except:
        return pd.DataFrame()

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommended_indices = [i[0] for i in scores[1:6]]

    return data.iloc[recommended_indices]

# =========================
# PAGE TITLE
# =========================

st.title("🤖 AI Book Recommendation Engine")
st.markdown("Get intelligent recommendations based on book title, author, and category.")

# =========================
# KPI CARDS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Total Books", len(books))

with col2:
    st.metric("📂 Categories", books["Category"].nunique())

with col3:
    st.metric("✍ Authors", books["Author"].nunique())

st.divider()

# =========================
# BOOK SELECTION
# =========================

selected_book = st.selectbox(
    "📖 Select a Book",
    sorted(books["Title"].unique())
)

# Show Selected Book Details
selected_data = books[books["Title"] == selected_book]

if not selected_data.empty:
    st.subheader("Selected Book")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info(f"📖 {selected_data.iloc[0]['Title']}")

    with c2:
        st.info(f"✍ {selected_data.iloc[0]['Author']}")

    with c3:
        st.info(f"📂 {selected_data.iloc[0]['Category']}")

    with c4:
        st.info(f"💰 ₹{selected_data.iloc[0]['Price']}")

# =========================
# RECOMMEND BUTTON
# =========================

if st.button("🚀 Generate Recommendations"):

    recommendations = recommend(selected_book)

    if not recommendations.empty:

        st.success("Top Recommended Books")

        st.dataframe(
            recommendations[
                ["Title", "Author", "Category", "Price", "Stock"]
            ],
            use_container_width=True
        )

    else:
        st.warning("No recommendations found.")