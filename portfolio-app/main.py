# import for connecting to a Sql Server database
import sqlalchemy

# connect to SQL Server database using sqlalchemy
# use connecting string that uses a managed identity

engine = sqlalchemy.create_engine(
    "mssql+pyodbc://your_server_name/your_database_name?driver=ODBC+Driver+17+for+SQL+Server&Authentication=ActiveDirectoryManagedIdentity"
)
# establish a connection to the database
conn = engine.connect()
# create a cursor object to interact with the database
cursor = conn.cursor()
# execute a simple query to fetch data from a table
cursor.execute("SELECT TOP 10 * FROM your_table_name")
# fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row)
