import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Books Inventory", layout="wide")

# =========================
# LOAD DATA
# =========================

from src.db_helper import get_books

books = get_books()

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
    low_stock_count = len(books[books["Stock"] < 20])
    st.metric("⚠ Low Stock Books", low_stock_count)

st.divider()

# =========================
# CRUD SECTION
# =========================

tab1, tab2, tab3 = st.tabs(
    ["➕ Add Book", "✏ Update Stock", "🗑 Delete Book"]
)

# =========================
# ADD BOOK
# =========================

with tab1:

    st.subheader("Add New Book")

    with st.form("add_book_form"):

        book_id = st.text_input("Book ID")
        title = st.text_input("Title")
        author = st.text_input("Author")
        category_input = st.text_input("Category")

        price = st.number_input(
            "Price",
            min_value=0
        )

        stock = st.number_input(
            "Stock",
            min_value=0
        )

        submitted = st.form_submit_button(
            "Add Book"
        )

        if submitted:

            new_book = pd.DataFrame({
                "Book_ID": [book_id],
                "Title": [title],
                "Author": [author],
                "Category": [category_input],
                "Price": [price],
                "Stock": [stock]
            })

            books = pd.concat(
                [books, new_book],
                ignore_index=True
            )

            books.to_csv(
                BOOKS_FILE,
                index=False
            )

            st.success(
                f"{title} added successfully!"
            )

# =========================
# UPDATE STOCK
# =========================

with tab2:

    st.subheader("Update Book Stock")

    selected_book = st.selectbox(
        "Select Book",
        books["Book_ID"]
    )

    new_stock = st.number_input(
        "New Stock",
        min_value=0
    )

    if st.button("Update Stock"):

        books.loc[
            books["Book_ID"] == selected_book,
            "Stock"
        ] = new_stock

        books.to_csv(
            BOOKS_FILE,
            index=False
        )

        st.success(
            "Stock updated successfully!"
        )

# =========================
# DELETE BOOK
# =========================

with tab3:

    st.subheader("Delete Book")

    delete_book = st.selectbox(
        "Choose Book to Delete",
        books["Book_ID"]
    )

    if st.button("Delete Book"):

        books = books[
            books["Book_ID"] != delete_book
        ]

        books.to_csv(
            BOOKS_FILE,
            index=False
        )

        st.success(
            "Book deleted successfully!"
        )

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
        ["All"] + sorted(
            books["Category"].unique().tolist()
        )
    )

# =========================
# PRICE FILTER
# =========================

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
        filtered["Title"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        filtered["Author"].str.contains(
            search,
            case=False,
            na=False
        )
        |
        filtered["Category"].str.contains(
            search,
            case=False,
            na=False
        )
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

category_count = (
    books["Category"]
    .value_counts()
    .reset_index()
)

category_count.columns = [
    "Category",
    "Count"
]

fig = px.pie(
    category_count,
    names="Category",
    values="Count",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# BOOK TABLE
# =========================

st.subheader("📖 Books List")

st.write(
    f"Showing **{len(filtered)}** books"
)

st.dataframe(
    filtered,
    use_container_width=True
)

# =========================
# LOW STOCK BOOKS
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

    st.success(
        "No low stock books found."
    )

# =========================
# DOWNLOAD
# =========================

csv = filtered.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "⬇ Download Filtered CSV",
    csv,
    "books_inventory.csv",
    "text/csv"
)