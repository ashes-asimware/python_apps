import mysql-connector as mc

from password import PASSWORD

db = mc.connect(
    host="localhost",
    user="root",
    password=PASSWORD
)
print('Connected to MySQL server:', db)
cursor = db.cursor()
print("Cursor created:", cursor)

cursor.execute("create database test_db")
print("Database created.")
# cursor.use_database("test_db")
# table_ddl = """
# CREATE TABLE game_stats (
#     player_name NVARCHAR(50),
#     score INT,
#     level INT,
#     rank NVARCHAR(20)
# )"""

# cursor.execute(table_ddl)
