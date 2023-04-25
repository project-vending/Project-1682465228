python
import streamlit as st
import pandas as pd
import psycopg2

# Establish a connection with your Redshift cluster
connection = psycopg2.connect(
    host="YOUR_REDSHIFT_HOSTNAME",
    port="YOUR_REDSHIFT_PORT",
    dbname="YOUR_REDSHIFT_DBNAME",
    user="YOUR_REDSHIFT_USERNAME",
    password="YOUR_REDSHIFT_PASSWORD"
)

# Define a function to fetch data from Redshift and return it as a pandas dataframe
def fetch_data(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return pd.DataFrame(data, columns=columns)

# Define your Streamlit app
def run():
    st.set_page_config(page_title='Redshift Dashboard', page_icon=':bar_chart:')
    st.title('Redshift Dashboard')
    
    # Display a dropdown menu of table names to choose from
    table_name = st.selectbox('Select a table', ['sales', 'customers', 'orders'])
    
    # Construct a query to fetch data from the selected table and display it in a table
    query = f'SELECT * FROM {table_name};'
    df = fetch_data(query)
    st.write(df)

if __name__ == '__main__':
    run()
