from password import PASSWORD
import messages as msg
from sharedlib import DatabaseConnection

dbconn = DatabaseConnection(
    host="localhost",
    user="root"
)

# Create database
dbconn.connect_no_db(PASSWORD)
print(msg.CONNECTED_NO_DB, dbconn.connection)
dbconn.execute(msg.CREATE_DB_DDL) #DDL
dbconn.execute(msg.USE_DB_DDL) #DDL

# Cleanup table and create table
dbconn.execute(msg.DROP_TBL_DDL) #DDL
dbconn.execute(msg.CREATE_TBL_DDL) #DDL
print(msg.TBL_CREATED)

dbconn.close()

# Insert records
dbconn.connect_with_db(PASSWORD, "game_db")
print(msg.CONNECTED_WITH_DB)
game_stats = [
    ('John', 1500, 10, 'Gold'),
    ('Tom', 1200, 8, None),
    ('Dick', 900, 5, 'Bronze'),
    ('Harry', 2000, 12, None)
]

dbconn.execute(msg.INSERT_DML,"dml","Many",game_stats)
print("Data inserted")

dbconn.close()

dbconn.connect_with_db(PASSWORD,'game_db')
print(msg.CONNECTED_WITH_DB)

# Get records for player 'Harry'
try:
    rows = dbconn.fetch_all(msg.SELECT_ID_DDL, ('Harry',))
    if rows and len(rows) > 0:
        player_id = rows[0][0]  # Get the id from the first row
        print(f"{msg.FOUND_PLAYER}{player_id}")
        # Update rank_value to 'Silver'
        rows_updated = dbconn.update(
            msg.UPDATE_RANK_DML, ('Silver', player_id))
        if rows_updated > 0:
            print(msg.UPDATED_SUCCESSFUL)
        else:
            print(msg.UPDATED_NO_ROWS)
    else:
        print(msg.RECORD_NOT_FOUND)
except Exception as e:
    print(msg.ERROR_SELECTING_UPDATING, e)

# First fetch and show players with null rank_value, then delete them by ID
try:
    # Get all players with null rank_value
    null_rank_players = dbconn.fetch_all(msg.SELECT_NULL_RANK_DDL)
    if null_rank_players:
        print(msg.FOUND_NULL_RANK.format(len(null_rank_players)))
        # Extract IDs and show player info
        player_ids = []
        for player in null_rank_players:
            player_ids.append(str(player[0]))  # Convert ID to string for join
            print(msg.PLAYER_INFO.format(player[0], player[1], player[2], player[3]))
        
        # Create parameterized DELETE query with exact number of placeholders
        delete_query = msg.DELETE_BY_IDS_DML.format(','.join(['%s'] * len(player_ids)))
        rows_deleted = dbconn.delete(delete_query, player_ids)
        print(msg.DELETED_SUCCESSFUL.format(rows_deleted))
    else:
        print(msg.NO_NULL_RANK_PLAYERS)
except Exception as e:
    print(msg.ERROR_DELETING, e)
