
import os

# Define the project folder structure
folders = ['data', 'etl', 'sql', 'streamlit']

# Create folders if they do not exist
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f'{folder} folder created')

# Create empty files in each folder
data_files = ['sales.csv', 'customers.csv', 'orders.csv']
etl_files = ['extract.py', 'transform.py', 'load.py']
sql_files = ['create_tables.sql', 'insert_data.sql']
streamlit_files = ['dashboard.py']

for folder in folders:
    if folder == 'data':
        for file in data_files:
            file_path = os.path.join(folder, file)
            open(file_path, 'w').close()
            print(f'{file} created in {folder} folder')
    elif folder == 'etl':
        for file in etl_files:
            file_path = os.path.join(folder, file)
            open(file_path, 'w').close()
            print(f'{file} created in {folder} folder')
    elif folder == 'sql':
        for file in sql_files:
            file_path = os.path.join(folder, file)
            open(file_path, 'w').close()
            print(f'{file} created in {folder} folder')
    elif folder == 'streamlit':
        for file in streamlit_files:
            file_path = os.path.join(folder, file)
            open(file_path, 'w').close()
            print(f'{file} created in {folder} folder')
