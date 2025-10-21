import mysql.connector as mc

from password import PASSWORD

db = mc.connect(
    host="localhost",
    user="root",
    passwd=PASSWORD
)
print('Connected to MySQL server:', db)
cursor = db.cursor()
print("Cursor created:", cursor)
cursor.execute("CREATE DATABASE IF NOT EXISTS game_db")
cursor.execute("USE game_db")
cursor.execute("DROP TABLE IF EXISTS game_stats")
table_ddl = """
CREATE TABLE IF NOT EXISTS game_stats (
    player_name NVARCHAR(50) NOT NULL,
    score INT NOT NULL,
    level INT NOT NULL,
    rank_value NVARCHAR(20)
)"""
cursor.execute(table_ddl)
print("Table 'game_stats' created or already exists.")
cursor.close()
db.close()

db = mc.connect(
    host="localhost",
    user="root",
    passwd=PASSWORD,
    database="game_db"
)
cursor = db.cursor()
stats = [
    ('John', 1500, 10, 'Gold'),
    ('Tom', 1200, 8, None),
    ('Dick', 900, 5, 'Bronze'),
    ('Harry', 2000, 12, None)
]
insert_ddl = """
    INSERT INTO game_stats 
        (player_name, 
        score, 
        level, 
        rank_value)
    VALUES (%s, %s, %s, %s)
"""
cursor.executemany(insert_ddl, stats)
db.commit()
print(f"{cursor.rowcount} records inserted into 'game_stats' table.")
cursor.close()
db.close()



