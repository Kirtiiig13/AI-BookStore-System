# AI Book Store Project

## Overview
This repository contains an AI-powered book store management system with Streamlit dashboards for inventory, customer analytics, sales, recommendations, and segmentation.

## Project Pages
The Streamlit app uses the `pages` directory to separate each feature page:

- `pages/1_Dashboard.py`
  - Main analytics dashboard for sales, revenue, top books, and category insights.
- `pages/2_Books.py`
  - Books inventory dashboard with search, filtering, and category charts.
- `pages/3_Customers.py`
  - Customer analytics dashboard with customer search, gender distribution, and age insights.
- `pages/4_Sales.py`
  - Sales data page showing raw sales records and monthly sales trend.
- `pages/5_Recommendations.py`
  - AI book recommendation engine using TF-IDF and cosine similarity.
- `pages/6_Segmentation.py`
  - Customer segmentation page displaying saved segment clusters from `reports/customer_segments.csv`.

## Key Files
- `app.py` - Streamlit landing page and navigation overview for the project.
- `requirements.txt` - Python dependencies for running the app.
- `data/books.csv`, `data/customers.csv`, `data/sales.csv` - Core datasets used by the dashboards.
- `reports/customer_segments.csv` - Generated segmentation results displayed by the segmentation page.
- `src/book_manager.py` - Book management utilities and logic.
- `src/customer_manager.py` - Customer analytics utility functions.
- `src/sales_manager.py` - Sales processing and aggregation helpers.
- `src/main.py` - Main backend orchestration script, if used for dataset preparation or utilities.

## Data Files
- `data/books.csv` - Book inventory, pricing, categories, and stock levels.
- `data/customers.csv` - Customer profiles, demographics, and segmenting attributes.
- `data/sales.csv` - Sales transactions, quantities, dates, and book references.

## How to Run
1. Create or activate your Python environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   streamlit run app.py
   ```
4. Use the sidebar to navigate to Dashboard, Books, Customers, Sales, Recommendations, and Segmentation.

## Notes
- The segmentation page requires `reports/customer_segments.csv` to exist. If not present, the page will show a warning.
- The recommendations page uses book metadata (`Title`, `Author`, `Category`) to generate similar book suggestions.