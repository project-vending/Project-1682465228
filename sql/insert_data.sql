python
import os

sql_folder = 'sql'
insert_query = "INSERT INTO sales (id, date, amount) VALUES (1, '2022-01-01', 100);"

if not os.path.exists(sql_folder):
    os.mkdir(sql_folder)

insert_data_path = os.path.join(sql_folder, 'insert_data.sql')

with open(insert_data_path, 'w') as f:
    f.write(insert_query)
    print(f"{insert_data_path} file created with insert query: '{insert_query}'")
