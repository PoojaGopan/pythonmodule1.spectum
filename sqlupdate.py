
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
# Example SQL query to create the 'mytables' table
create_table_query = """
CREATE TABLE IF NOT EXISTS MyTable (
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

# Example SQL query for inserting data into the 'mytables' table
insert_data_query = """
INSERT INTO MyTable (CustomerID, FirstName, LastName, Email, PhoneNumber)
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

# Example SQL query to select all rows from the 'mytables' table
select_all_query = "SELECT * FROM MyTable"

# Execute the select query
cursor.execute(select_all_query)

# Fetch all the rows
result = cursor.fetchall()

# Print the results
print("Data in mytables before update:")
for row in result:
    print(row)

# Example SQL query for updating data in the 'mytables' table
update_query = """
UPDATE MyTable
SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s
WHERE CustomerID = %s
"""

# Data to be updated
data_to_update = ("UpdatedFirstName", "UpdatedLastName", 'updated_email@gmail.com', '98765432', 22)

# Execute the update query
cursor.execute(update_query, data_to_update)

# Commit the changes to the database
conn.commit()

# Example SQL query to select all rows from the 'mytables' table after update
cursor.execute(select_all_query)
result_after_update = cursor.fetchall()

# Print the results after update
print("\nData in mytables after update:")
for row in result_after_update:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
