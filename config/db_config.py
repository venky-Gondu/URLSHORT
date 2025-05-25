import psycopg2
from psycopg2 import Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        connection=psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),  # Default to localhost if not set
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT", "5432")  # Default PostgreSQL port is 5432


        )
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        print("✅ Connection test passed! Database is accessible.")
        conn.close()
    else:
        print("❌ Connection test failed!")