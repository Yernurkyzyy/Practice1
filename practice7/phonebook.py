import psycopg2
import csv
from config import params, CREATE_TABLE_COMMAND, CSV_FILE_PATH
from connect import initialize_db

# 1
def insert_contact(name, phone):
    sql = "INSERT INTO contacts(contact_name, phone_number) VALUES(%s, %s) ON CONFLICT DO NOTHING;"
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (name, phone))
    print(f"Contact {name} saved.")

def upload_csv():
    with open(CSV_FILE_PATH, 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            insert_contact(row[0], row[1])

# 2
def search_contact(query):
    sql = "SELECT * FROM contacts WHERE contact_name ILIKE %s OR phone_number LIKE %s;"
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (f"%{query}%", f"%{query}%"))
            results = cur.fetchall()
            for r in results:
                print(f"ID: {r[0]} | Name: {r[1]} | Phone: {r[2]}")

#3 
def update_phone(name, new_phone):
    sql = "UPDATE contacts SET phone_number = %s WHERE contact_name = %s;"
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (new_phone, name))
            print(f"{name}'s phone updated.")

def delete_contact(name):
    sql = "DELETE FROM contacts WHERE contact_name = %s;"
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (name,))
            print(f"Contact {name} deleted.")

# MAIN PROGRAM
if __name__ == "__main__":
    initialize_db(CREATE_TABLE_COMMAND) 
    
    upload_csv()
    
    print("\nSearch results for 'Ali':")
    search_contact("Ali")