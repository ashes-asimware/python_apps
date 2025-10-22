CONNECTED_NO_DB= 'Connected to MySQL server:'
CREATE_DB_DDL = "CREATE DATABASE IF NOT EXISTS game_db"
USE_DB_DDL = "USE game_db"
DROP_TBL_DDL = "DROP TABLE IF EXISTS game_stats"
CREATE_TBL_DDL = """
CREATE TABLE IF NOT EXISTS game_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_name NVARCHAR(50) NOT NULL,
    score INT NOT NULL,
    level INT NOT NULL,
    rank_value NVARCHAR(20)
)"""
CONNECTED_WITH_DB = "Connected to database 'game_db'"
TBL_CREATED = "Table 'game_stats' created or already exists."
INSERT_DML = """
    INSERT INTO game_stats 
        (player_name, 
        score, 
        level, 
        rank_value)
    VALUES (%s, %s, %s, %s)
"""
SELECT_ID_DDL = "SELECT id FROM game_stats WHERE player_name = %s"
FOUND_PLAYER = "Found player 'Harry' with id="
UPDATE_RANK_DML = "UPDATE game_stats SET rank_value = %s WHERE id = %s"
UPDATED_SUCCESSFUL = "Updated rank_value to 'Silver' for player 'Harry'."
UPDATED_NO_ROWS = "No rows were updated."
RECORD_NOT_FOUND = "Player 'Harry' not found; no update performed."
ERROR_SELECTING_UPDATING = "Error selecting/updating player:"

# Fetch and Delete related messages and SQL
SELECT_NULL_RANK_DDL = """
    SELECT id, player_name, score, level, rank_value 
    FROM game_stats 
    WHERE rank_value IS NULL
"""
FOUND_NULL_RANK = "Found {} player(s) with null rank_value:"
PLAYER_INFO = "ID: {}, Name: {}, Score: {}, Level: {}"
DELETE_BY_IDS_DML = "DELETE FROM game_stats WHERE id IN ({})"
DELETED_SUCCESSFUL = "Successfully deleted {} player(s)."
ERROR_DELETING = "Error deleting players:"
NO_NULL_RANK_PLAYERS = "No players found with null rank_value. Nothing to delete."
