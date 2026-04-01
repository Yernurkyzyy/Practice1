import psycopg2
from config import params

def get_connection():
    return psycopg2.connect(**params)

def initialize_db(command):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                conn.commit()
                print(" Database initialized (Table created).")
    except Exception as e:
        print(f" Error: {e}")