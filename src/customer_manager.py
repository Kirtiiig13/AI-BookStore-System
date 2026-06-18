import pandas as pd

CUSTOMER_FILE = "../data/customers.csv"


def view_customers():
    customers = pd.read_csv(CUSTOMER_FILE)
    print("\nCustomers List:")
    print(customers)


def add_customer():

    customers = pd.read_csv(CUSTOMER_FILE)

    customer_id = input("Customer ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    city = input("City: ")

    new_customer = pd.DataFrame({
        "Customer_ID": [customer_id],
        "Name": [name],
        "Age": [age],
        "Gender": [gender],
        "City": [city]
    })

    customers = pd.concat(
        [customers, new_customer],
        ignore_index=True
    )

    customers.to_csv(CUSTOMER_FILE, index=False)

    print("Customer Added Successfully")

def search_customer():

    customers = pd.read_csv(CUSTOMER_FILE)

    customer_id = input("Enter Customer ID: ")

    result = customers[
        customers["Customer_ID"] == customer_id
    ]

    if not result.empty:
        print(result)
    else:
        print("Customer Not Found")

def update_customer():

    customers = pd.read_csv(CUSTOMER_FILE)

    customer_id = input("Enter Customer ID: ")

    index = customers[
        customers["Customer_ID"] == customer_id
    ].index

    if len(index) > 0:

        new_city = input("New City: ")

        customers.loc[index, "City"] = new_city

        customers.to_csv(
            CUSTOMER_FILE,
            index=False
        )

        print("Customer Updated Successfully")

    else:
        print("Customer Not Found")

def delete_customer():

    customers = pd.read_csv(CUSTOMER_FILE)

    customer_id = input(
        "Enter Customer ID to Delete: "
    )

    customers = customers[
        customers["Customer_ID"] != customer_id
    ]

    customers.to_csv(
        CUSTOMER_FILE,
        index=False
    )

    print("Customer Deleted Successfully")

