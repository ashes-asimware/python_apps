import pyodbc
from config import read_dbconnstring

conn_str = read_dbconnstring()
# Connect to the database
conn = pyodbc.connect(conn_str)

# Create a cursor object to execute queries
cursor = conn.cursor()

# Define the query string
query = 'SELECT TOP 10 * FROM DAILYMARKETQUOTE'

# Execute the query and fetch the results
cursor.execute(query)
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
conn.close()
