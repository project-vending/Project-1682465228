python
import pandas as pd

# Load the data
sales_df = pd.read_csv('../data/sales.csv')
customers_df = pd.read_csv('../data/customers.csv')
orders_df = pd.read_csv('../data/orders.csv')

# Merge the data
merged_df = pd.merge(sales_df, customers_df, on='customer_id')
merged_df = pd.merge(merged_df, orders_df, on='order_id')

# Transform the data
transformed_df = merged_df.groupby(['date', 'region', 'product_id']).agg(
    total_sales=('revenue', 'sum'),
    total_orders=('order_id', 'nunique'),
    total_customers=('customer_id', 'nunique')
).reset_index()

# Save the transformed data to disk
transformed_df.to_csv('../data/transformed_sales.csv', index=False)
