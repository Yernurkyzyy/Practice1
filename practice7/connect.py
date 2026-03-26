import psycopg2
from config import params

def check_connection():

    try:
        conn = psycopg2.connect(**params)
        print("Successfully connected to PostgreSQL!")
        conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")

def get_connection():
   
    return psycopg2.connect(**params)


def initialize_db(command):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(command)
            conn.commit()
    print("Database initialized.")