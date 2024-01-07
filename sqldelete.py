import mysql.connector

# Replace with your database credentials
host = "localhost"
user = "root"
password = "poojaSQL123!"
database = "poojagopan"

# Establish a connection
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor
cursor = conn.cursor()

# Example SQL query to create the 'mytable' table
create_table_query = """
CREATE TABLE IF NOT EXISTS mytables (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255),
    PhoneNumber VARCHAR(20)
)
"""

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes to the database
conn.commit()

# Example SQL query for inserting data into the 'mytable' table
insert_data_query = """
INSERT INTO mytables (CustomerID, FirstName, LastName, Email, PhoneNumber)
VALUES (%s, %s, %s, %s, %s)
"""

# Data to be inserted
data_to_insert = [
    (21, "Jiji", "Gomez", 'jiji@gmail.com', '46765587'),
    (22, "liji", "Gomez", 'liji@gmail.com', '46765587'),
    (23, "Jiji", "Gomez", 'jiji@gmail.com', '46765587'),
    (24, "liji", "Gomez", 'liji@gmail.com', '46765587')
]

# Execute the insert queries
for data in data_to_insert:
    cursor.execute(insert_data_query, data)

# Commit the changes to the database
conn.commit()

# Example SQL query to select all rows from the 'mytable' table
select_all_query = "SELECT * FROM mytables"

# Execute the select query
cursor.execute(select_all_query)

# Fetch all the rows
result = cursor.fetchall()

# Print the results
print("Data in mytable before deletion:")
for row in result:
    print(row)

# Example SQL query for deleting data from the 'mytable' table
delete_query = "DELETE FROM mytables WHERE CustomerID = %s"

# Data to be deleted
data_to_delete = (21,)#comma required

# Execute the delete query
cursor.execute(delete_query, data_to_delete)

# Commit the changes to the database
conn.commit()

# Example SQL query to select all rows from the 'mytable' table after deletion
cursor.execute(select_all_query)
result_after_deletion = cursor.fetchall()

# Print the results after deletion
print("\nData in mytable after deletion:")
for row in result_after_deletion:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
