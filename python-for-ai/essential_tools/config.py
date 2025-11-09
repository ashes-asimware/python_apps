import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
database_url = os.getenv("DB_CONNECTION_STRING")

print(f"DATABASE_URL: {database_url}")
