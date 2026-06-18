import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customers", layout="wide")

CUSTOMERS_FILE = "data/customers.csv"

customers = pd.read_csv(CUSTOMERS_FILE)

st.title("👥 Customer Management System")

# =========================
# KPI CARDS
# =========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Total Customers", len(customers))

with col2:
    if "Age" in customers.columns:
        st.metric(
            "🎂 Average Age",
            f"{customers['Age'].mean():.0f}"
        )

with col3:
    st.metric(
        "🆔 Customer Records",
        len(customers)
    )

st.divider()

# =========================
# CRUD SECTION
# =========================

tab1, tab2 = st.tabs(
    ["➕ Add Customer", "🗑 Delete Customer"]
)

# =========================
# ADD CUSTOMER
# =========================

with tab1:

    st.subheader("Add New Customer")

    with st.form("customer_form"):

        customer_id = st.text_input("Customer ID")
        customer_name = st.text_input("Customer Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100
        )

        submit = st.form_submit_button(
            "Add Customer"
        )

        if submit:

            new_customer = pd.DataFrame({
                "Customer_ID": [customer_id],
                "Name": [customer_name],
                "Age": [age]
            })

            customers = pd.concat(
                [customers, new_customer],
                ignore_index=True
            )

            customers.to_csv(
                CUSTOMERS_FILE,
                index=False
            )

            st.success(
                "Customer added successfully!"
            )

# =========================
# DELETE CUSTOMER
# =========================

with tab2:

    st.subheader("Delete Customer")

    delete_customer = st.selectbox(
        "Select Customer",
        customers["Customer_ID"]
    )

    if st.button("Delete Customer"):

        customers = customers[
            customers["Customer_ID"]
            != delete_customer
        ]

        customers.to_csv(
            CUSTOMERS_FILE,
            index=False
        )

        st.success(
            "Customer deleted successfully!"
        )

st.divider()

# =========================
# SEARCH
# =========================

search = st.text_input(
    "🔍 Search Customer"
)

filtered = customers.copy()

if search:

    filtered = filtered[
        filtered.astype(str)
        .apply(
            lambda row:
            row.str.contains(
                search,
                case=False
            ).any(),
            axis=1
        )
    ]

# =========================
# CUSTOMER TABLE
# =========================

st.subheader("📋 Customer Records")

st.dataframe(
    filtered,
    use_container_width=True
)

# =========================
# DOWNLOAD
# =========================

csv = filtered.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "⬇ Download Customer Data",
    csv,
    "customers.csv",
    "text/csv"
)