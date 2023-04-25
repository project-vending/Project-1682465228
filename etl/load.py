python
import psycopg2
import csv

# Connect to Redshift
conn = psycopg2.connect(
    host='redshift-cluster-1.abcdef123456.us-west-2.redshift.amazonaws.com',
    dbname='my_database',
    user='my_user',
    password='my_password',
    port=5439
)

# Open a cursor
cur = conn.cursor()

# Load data from CSV into a temporary table
with open('data/sales.csv', 'r') as f:
    reader = csv.reader(f)
    cols = next(reader)
    cur.copy_from(f, 'temp_sales', sep=',', columns=cols)

# Insert data from temporary table into the production table
cur.execute('INSERT INTO sales SELECT * FROM temp_sales')

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
