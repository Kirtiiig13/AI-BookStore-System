import pandas as pd

BOOK_FILE = "../data/books.csv"


def view_books():
    books = pd.read_csv(BOOK_FILE)
    print("\nAvailable Books:")
    print(books)


def add_book():
    books = pd.read_csv(BOOK_FILE)

    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    new_book = pd.DataFrame({
        "Book_ID": [book_id],
        "Title": [title],
        "Author": [author],
        "Category": [category],
        "Price": [price],
        "Stock": [stock]
    })

    books = pd.concat([books, new_book], ignore_index=True)

    books.to_csv(BOOK_FILE, index=False)

    print("Book Added Successfully")

def search_book():
    books = pd.read_csv(BOOK_FILE)

    book_id = input("Enter Book ID: ")

    result = books[books["Book_ID"] == book_id]

    if not result.empty:
        print(result)
    else:
        print("Book Not Found")

def delete_book():
    books = pd.read_csv(BOOK_FILE)

    book_id = input("Enter Book ID to Delete: ")

    books = books[books["Book_ID"] != book_id]

    books.to_csv(BOOK_FILE, index=False)

    print("Book Deleted Successfully")

def update_book():
    books = pd.read_csv(BOOK_FILE)

    book_id = input("Enter Book ID: ")

    index = books[books["Book_ID"] == book_id].index

    if len(index) > 0:

        new_stock = int(input("New Stock: "))
        new_price = float(input("New Price: "))

        books.loc[index, "Stock"] = new_stock
        books.loc[index, "Price"] = new_price

        books.to_csv(BOOK_FILE, index=False)

        print("Book Updated Successfully")

    else:
        print("Book Not Found")

    