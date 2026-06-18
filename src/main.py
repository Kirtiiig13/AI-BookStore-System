from book_manager import *
from book_manager import *
from customer_manager import *
from sales_manager import *

while True:

    print("\n===== BOOK STORE MANAGEMENT =====")
    print("1. View Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. View Customers")
    print("7. Add Customer")
    print("8. Search Customer")
    print("9. Update Customer")
    print("10. Delete Customer")
    print("11. Record Sale")
    print("12. View Sales")
    print("13. Total Revenue")
    print("14. Best Selling Books")
    print("15. Exit")
    

    choice = input("Enter Choice: ")

    if choice == "1":
        view_books()

    elif choice == "2":
        add_book()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        view_customers()

    elif choice == "7":
        add_customer()

    elif choice == "8":
        search_customer()

    elif choice == "9":
        update_customer()

    elif choice == "10":
        delete_customer()

    elif choice == "11":
        record_sale()

    elif choice == "12":
        view_sales()

    elif choice == "13":
        total_revenue()

    elif choice == "14":
        best_selling_books()

    elif choice == "15":
        break

    else:
        print("Invalid Choice")