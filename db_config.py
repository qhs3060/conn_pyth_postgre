# db_config.py
import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_db_connection():
    """Function to create and return a database connection."""
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    return conn