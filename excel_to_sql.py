import os
import pandas as pd

# do a "pip install pandas pymysql" first
#then pip install openpyxl
# Get the current working directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Replace this with your Excel file name
excel_file_name = "data.xlsx"

# Combine the current directory with the Excel file name
excel_file_path = os.path.join(current_directory, excel_file_name)

# Replace this with your table name
table_name = "your_table_name"

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Convert DataFrame to SQL insert statements
sql_statements = []
for index, row in df.iterrows():
    values = ','.join([f"'{str(value)}'" for value in row.values])
    sql_statements.append(f"INSERT INTO {table_name} VALUES ({values});")

# Write the SQL file
sql_file_path = os.path.join(current_directory, "output.sql")
with open(sql_file_path, 'w') as sql_file:
    sql_file.write('\n'.join(sql_statements))

print(f'Success! SQL file "{sql_file_path}" created.')
#then just run python excel_to_sql.py on command prompt in the directory