from password import PASSWORD
import dbconnection as dc

dbconn = dc.DatabaseConnection(
    host="localhost",
    user="root"
)

# Create database
dbconn.connect_no_db(PASSWORD)
print('Connected to MySQL server:', dbconn.connection)
dbconn.execute("CREATE DATABASE IF NOT EXISTS game_db") #DDL

dbconn.execute("USE game_db") #DDL

# Cleanup table and create table
dbconn.execute("DROP TABLE IF EXISTS game_stats") #DDL
table_ddl = """
CREATE TABLE IF NOT EXISTS game_stats (
    player_name NVARCHAR(50) NOT NULL,
    score INT NOT NULL,
    level INT NOT NULL,
    rank_value NVARCHAR(20)
)"""
dbconn.execute(table_ddl) #DDL
print("Table 'game_stats' created or already exists.")

dbconn.close()

# Insert records
dbconn.connect_with_db(PASSWORD, "game_db")
game_stats = [
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
dbconn.execute(insert_ddl,"dml","Many",game_stats)
print("Data inserted")

dbconn.close()