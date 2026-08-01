import os

PASSWORD = os.environ.get("MYSQL_PASSWORD")
if not PASSWORD:
    raise RuntimeError("MYSQL_PASSWORD environment variable is not set")