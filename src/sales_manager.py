import pandas as pd

BOOK_FILE = "../data/books.csv"
SALES_FILE = "../data/sales.csv"


def record_sale():

    books = pd.read_csv(BOOK_FILE)
    sales = pd.read_csv(SALES_FILE)

    sale_id = input("Sale ID: ")
    book_id = input("Book ID: ")
    customer_id = input("Customer ID: ")
    quantity = int(input("Quantity: "))
    date = input("Date (YYYY-MM-DD): ")

    book = books[books["Book_ID"] == book_id]

    if book.empty:
        print("Book Not Found")
        return

    stock = book.iloc[0]["Stock"]

    if quantity > stock:
        print("Insufficient Stock")
        return

    books.loc[
        books["Book_ID"] == book_id,
        "Stock"
    ] -= quantity

    new_sale = pd.DataFrame({
        "Sale_ID": [sale_id],
        "Book_ID": [book_id],
        "Customer_ID": [customer_id],
        "Quantity": [quantity],
        "Date": [date]
    })

    sales = pd.concat(
        [sales, new_sale],
        ignore_index=True
    )

    sales.to_csv(SALES_FILE, index=False)
    books.to_csv(BOOK_FILE, index=False)

    print("Sale Recorded Successfully")

def view_sales():

    sales = pd.read_csv(SALES_FILE)

    print("\nSales History")
    print(sales)

def total_revenue():

    books = pd.read_csv(BOOK_FILE)
    sales = pd.read_csv(SALES_FILE)

    merged = pd.merge(
        sales,
        books,
        on="Book_ID"
    )

    merged["Revenue"] = (
        merged["Quantity"] *
        merged["Price"]
    )

    revenue = merged["Revenue"].sum()

    print(f"\nTotal Revenue: ₹{revenue}")

def best_selling_books():

    sales = pd.read_csv(SALES_FILE)

    result = sales.groupby(
        "Book_ID"
    )["Quantity"].sum()

    result = result.sort_values(
        ascending=False
    )

    print(result)

def best_selling_books():

    sales = pd.read_csv(SALES_FILE)

    result = sales.groupby(
        "Book_ID"
    )["Quantity"].sum()

    result = result.sort_values(
        ascending=False
    )

    print(result)

