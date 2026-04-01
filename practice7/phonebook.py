import psycopg2
import csv
from config import params, CREATE_TABLE_COMMAND
from connect import initialize_db, get_connection

# 1. INSERT (from Console)
def insert_contact(name, phone):
    sql = "INSERT INTO contacts(contact_name, phone_number) VALUES(%s, %s) ON CONFLICT DO NOTHING;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (name, phone))
            conn.commit()

# 2. INSERT (from CSV)
def upload_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header
        for row in reader:
            insert_contact(row[0], row[1])
    print(" CSV data imported.")

# 3. UPDATE (Name or Phone)
def update_contact(name, new_phone):
    sql = "UPDATE contacts SET phone_number = %s WHERE contact_name = %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (new_phone, name))
            conn.commit()
    print(f" Contact {name} updated.")

# 4. QUERY (Filters: Name or Phone prefix)
def search_contacts(query):
    sql = "SELECT * FROM contacts WHERE contact_name ILIKE %s OR phone_number LIKE %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (f"%{query}%", f"{query}%"))
            for row in cur.fetchall():
                print(row)

# 5. DELETE
def delete_contact(identifier):
    sql = "DELETE FROM contacts WHERE contact_name = %s OR phone_number = %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (identifier, identifier))
            conn.commit()
    print(f" Contact {identifier} deleted.")

if __name__ == "__main__":
    initialize_db(CREATE_TABLE_COMMAND)
    # Осы жерден функцияларды шақырып тексеруге болады