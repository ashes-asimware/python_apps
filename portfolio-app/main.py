import pyodbc

# Connection details
server = "ashes.database.windows.net"
database = "trading"
driver = "ODBC Driver 17 for SQL Server"


def connect_to_sql_server():
    # Connect to Azure SQL Database using Azure AD Interactive authentication
    conn_str = (
        f"Driver={{{driver}}};"
        f"Server=tcp:{server},1433;"
        f"Database={database};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
        f"Authentication=ActiveDirectoryInteractive;"
    )

    try:
        print("🔄 Connecting to Azure SQL Database...")
        print("(A browser window may open for Azure login)")

        conn = pyodbc.connect(conn_str)
        print("✅ Connected successfully!")
        return conn

    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\n📋 Troubleshooting:")
        print("1. Check your Azure AD permissions for the SQL database")
        print("2. Verify server/database names are correct")
        print("3. Ensure your IP is allowed in SQL Server firewall")
        print("4. Make sure you complete the browser login process")
        raise


def main():
    """Main function to demonstrate database operations"""
    conn = None
    try:
        # Connect to the database
        conn = connect_to_sql_server()

        # Create a cursor
        cursor = conn.cursor()

        # Test query - get database info
        # Example: Run a custom query (uncomment and modify as needed)
        cursor.execute("select top 10 * from portfolio;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        # Clean up
        if conn:
            conn.close()
            print("🔐 Database connection closed")


if __name__ == "__main__":
    main()
