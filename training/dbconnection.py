import mysql.connector as mc
from password import PASSWORD

class DatabaseConnection:
    def __init__(self, host="localhost", port=3307, user="root", password=PASSWORD, database="test_db"):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self.database = database
        self.connection = None

    def connect(self):
        # Code to establish a database connection
        self.connection = mc.connect(
            host=self._host,
            port=self._port,
            user=self._user,
            password=self._password,
            database=self._database
        )

    def connect_no_db(self):
        self.connection = mc.connect(
            host=self._host,
            port=self._port,
            user=self.user,
            password=self.password
        )

    def disconnect(self):
        # Code to close the database connection
        if self.connection.cursor():
            self.connection.cursor().close()
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, qtype="ddl", params=None):
        # Code to execute a database query
        cursor = self.connection.cursor()
        if qtype == "ddl":
            cursor.execute(query)
        elif qtype == "dml":
            cursor.execute(query, params)
            cursor.commit()
        else:
            raise ValueError("Invalid query type")