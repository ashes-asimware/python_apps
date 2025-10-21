import mysql.connector as mc
from password import PASSWORD
import dbconnection as dc

db = mc.connect(
    host="localhost",
    user="root",
    password=PASSWORD
)
print('Connected to MySQL server:', db)
cursor = db.cursor()
print("Cursor created:", cursor)
cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
cursor.execute("USE test_db")
cursor.execute("DROP TABLE IF EXISTS game_stats")
table_ddl = """
CREATE TABLE IF NOT EXISTS game_stats (
    player_name NVARCHAR(50) NOT NULL,
    score INT NOT NULL,
    level INT NOT NULL,
    rank_value NVARCHAR(20)
)"""
cursor.execute(table_ddl)
print("Table created.")
cursor.close()
db.close()

db = mc.connect(
    host="localhost",
    user="root",
    password=PASSWORD
)
cursor = db.cursor()
cursor.execute("USE test_db")
insert_ddl = """
INSERT INTO game_stats (
    player_name, 
    score, level, 
    rank_value)
    VALUES (%s, %s, %s, %s)
"""
stats = [
    ("Alice", 1000, 5, "Gold"),
    ("Bob", 1500, 7, "Platinum"),
    ("Charlie", 2000, 10, None)
]
cursor.executemany(insert_ddl, stats)
print("Data inserted.")
db.commit()
cursor.close()
db.close()