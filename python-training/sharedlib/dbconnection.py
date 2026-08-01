import mysql.connector as mc

class DatabaseConnection:
    def __init__(self, host="localhost", user="root"):
        self._host = host
        self._user = user
        self.connection = None

    def connect_no_db(self,password):
        import mysql.connector as mc
        self.connection = mc.connect(
            host=self._host,
            user=self._user,
            passwd=password
        )
        return self.connection
    
    def connect_with_db(self, password, database):
        self.connection = mc.connect(
            host=self._host,
            user=self._user,
            passwd=password,
            database=database
        )
        return self.connection
    
    def close(self):
        if self.connection:
            self.connection.cursor().close()
            self.connection.close()
            self.connection = None

    def execute(self, query, qtype="ddl", changeType="One", params=None):
        if not self.connection:
            raise Exception("Database connection is not established.")
        if qtype not in ["ddl", "dml"]:
            raise ValueError("qtype must be either 'ddl' or 'dml'.")
        elif qtype == "dml" and params is None:
            raise ValueError("Parameters must be provided for DML queries.")
        if changeType not in ["One", "Many"]:
            raise ValueError("changeType must be either 'One' or 'Many'.")
        elif changeType == "One":
            self.connection.cursor().execute(query, params or ())
        elif qtype == "dml" and changeType == "Many":
            self.connection.cursor().executemany(query, params or ())
        if qtype == "dml":
            self.connection.commit()

    def update(self, query, params=None):
        """Execute an UPDATE query with parameters."""
        if not self.connection:
            raise Exception("Database connection is not established.")
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor.rowcount
        finally:
            cursor.close()

    def fetch_all(self, query, params=None):
        """Execute a SELECT query and return all matching rows."""
        if not self.connection:
            raise Exception("Database connection is not established.")
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            return cursor.fetchall()
        finally:
            cursor.close()

    def delete(self, query, params=None):
        """Execute a DELETE query with parameters."""
        if not self.connection:
            raise Exception("Database connection is not established.")
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor.rowcount
        finally:
            cursor.close()

    