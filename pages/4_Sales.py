import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Management", layout="wide")

# =========================
# FILES
# =========================

SALES_FILE = "data/sales.csv"
BOOKS_FILE = "data/books.csv"
CUSTOMERS_FILE = "data/customers.csv"

# =========================
# LOAD DATA
# =========================

sales = pd.read_csv(SALES_FILE)
books = pd.read_csv(BOOKS_FILE)
customers = pd.read_csv(CUSTOMERS_FILE)

# =========================
# PAGE TITLE
# =========================

st.title("💰 Sales Management System")

# =========================
# KPI CARDS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🧾 Total Sales", len(sales))

with col2:
    st.metric("📚 Books Available", len(books))

with col3:
    st.metric("👥 Customers", len(customers))

st.divider()

# =========================
# RECORD NEW SALE
# =========================

st.subheader("➕ Record New Sale")

with st.form("sale_form"):

    customer_id = st.selectbox(
        "Customer",
        customers["Customer_ID"]
    )

    book_id = st.selectbox(
        "Book",
        books["Book_ID"]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        step=1
    )

    submit = st.form_submit_button(
        "Record Sale"
    )

    if submit:

        current_stock = books.loc[
            books["Book_ID"] == book_id,
            "Stock"
        ].values[0]

        if quantity > current_stock:

            st.error(
                f"Only {current_stock} books available."
            )

        else:

            # Generate Sale ID
            sale_id = f"S{len(sales)+1:03d}"

            # Current Date
            sale_date = pd.Timestamp.today().strftime(
                "%Y-%m-%d"
            )

            new_sale = pd.DataFrame({
                "Sale_ID": [sale_id],
                "Customer_ID": [customer_id],
                "Book_ID": [book_id],
                "Quantity": [quantity],
                "Date": [sale_date]
            })

            # Add Sale
            sales = pd.concat(
                [sales, new_sale],
                ignore_index=True
            )

            sales.to_csv(
                SALES_FILE,
                index=False
            )

            # Reduce Stock
            books.loc[
                books["Book_ID"] == book_id,
                "Stock"
            ] -= quantity

            books.to_csv(
                BOOKS_FILE,
                index=False
            )

            st.success(
                "Sale recorded successfully!"
            )

st.divider()

# =========================
# SALES TABLE
# =========================

st.subheader("📋 Sales Records")

sales["Date"] = pd.to_datetime(
    sales["Date"]
)

st.dataframe(
    sales.sort_values(
        "Date",
        ascending=False
    ),
    use_container_width=True
)

# =========================
# MONTHLY SALES TREND
# =========================

st.subheader("📈 Monthly Sales Trend")

monthly = (
    sales.groupby(
        sales["Date"].dt.to_period("M")
    )["Quantity"]
    .sum()
)

monthly.index = monthly.index.astype(str)

st.line_chart(monthly)

# =========================
# TOP SELLING BOOKS
# =========================

st.subheader("🏆 Top Selling Books")

top_books = (
    sales.groupby("Book_ID")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_books)

# =========================
# DOWNLOAD SALES REPORT
# =========================

csv = sales.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "⬇ Download Sales Report",
    csv,
    "sales_report.csv",
    "text/csv"
)