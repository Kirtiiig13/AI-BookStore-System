import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Recommendations", layout="wide")

books = pd.read_csv("data/books.csv")

def recommend(book_title):
    data = books.copy()

    data["features"] = (
        data["Title"].fillna("") + " " +
        data["Author"].fillna("") + " " +
        data["Category"].fillna("")
    )

    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform(data["features"])

    similarity = cosine_similarity(matrix)

    try:
        idx = data[data["Title"] == book_title].index[0]
    except:
        return []

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    results = []
    for i in scores[1:6]:
        results.append(data.iloc[i[0]]["Title"])

    return results

st.title("🤖 AI Book Recommendation System")

book = st.selectbox("Choose Book", books["Title"].dropna())

if st.button("Recommend"):
    recs = recommend(book)

    if recs:
        st.success("Recommended Books")
        for r in recs:
            st.write("📖", r)
    else:
        st.warning("No recommendations found")