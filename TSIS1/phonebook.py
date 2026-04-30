import psycopg2
import json
import csv
import os

def load_config():
    return {
        "host": "127.0.0.1",
        "database": "phonebook",
        "user": "macbookair",
        "password": "", 
        "port": 5432
    }

def get_connection():
    return psycopg2.connect(**load_config())

def setup_database():
    try:
        conn = get_connection()
        cur = conn.cursor()
        # Кестелерді құру және жаңарту (Критерий 3.1)
        cur.execute("CREATE TABLE IF NOT EXISTS groups (id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE NOT NULL);")
        cur.execute("CREATE TABLE IF NOT EXISTS contacts (id SERIAL PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50));")
        cur.execute("ALTER TABLE contacts ADD COLUMN IF NOT EXISTS email VARCHAR(100);")
        cur.execute("ALTER TABLE contacts ADD COLUMN IF NOT EXISTS birthday DATE;")
        cur.execute("ALTER TABLE contacts ADD COLUMN IF NOT EXISTS group_id INTEGER REFERENCES groups(id);")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phones (
                id SERIAL PRIMARY KEY,
                contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
                phone VARCHAR(20) NOT NULL,
                type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
            );
        """)
        # Іздеу функциясын құру (Критерий 3.4)
        cur.execute("""
            CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
            RETURNS TABLE (contact_id INT, full_name TEXT, contact_email VARCHAR, all_phones TEXT) AS $$
            BEGIN
                RETURN QUERY
                SELECT DISTINCT c.id, (c.first_name || ' ' || c.last_name) AS full_name, c.email, 
                       string_agg(p.phone, ', ') AS all_phones
                FROM contacts c
                LEFT JOIN phones p ON c.id = p.contact_id
                WHERE c.first_name ILIKE '%' || p_query || '%' 
                   OR c.last_name ILIKE '%' || p_query || '%'
                   OR c.email ILIKE '%' || p_query || '%'
                GROUP BY c.id;
            END; $$ LANGUAGE plpgsql;
        """)
        cur.execute("INSERT INTO groups (name) VALUES ('Family'), ('Work'), ('Other') ON CONFLICT DO NOTHING;")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ База қатесі: {e}")

# 3.3 Export to JSON
def export_to_json():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT c.first_name, c.last_name, c.email, CAST(c.birthday AS TEXT), g.name
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
        """)
        rows = cur.fetchall()
        data = [{"first_name": r[0], "last_name": r[1], "email": r[2], "birthday": r[3], "group": r[4]} for r in rows]
        with open('contacts.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("✅ Деректер contacts.json файлына сақталды!")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Қате: {e}")

# 3.2 Advanced Search (Email/Name)
def search_advanced():
    query = input("Іздеу (Есім немесе Email): ")
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM search_contacts(%s)", (query,))
        rows = cur.fetchall()
        if not rows: print("Ештеңе табылмады.")
        for r in rows: print(f"👤 {r[1]} | Email: {r[2]} | Phones: {r[3]}")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Қате: {e}")

# 3.2 Pagination
def view_paginated():
    limit, offset = 5, 0
    try:
        conn = get_connection()
        while True:
            cur = conn.cursor()
            cur.execute("SELECT first_name, last_name, email FROM contacts ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
            rows = cur.fetchall()
            print("\n--- Тізім ---")
            for r in rows: print(f"👤 {r[0]} {r[1]} | {r[2]}")
            cmd = input("\n[n] Next, [p] Prev, [q] Quit: ").lower()
            if cmd == 'n': offset += limit
            elif cmd == 'p': offset = max(0, offset - limit)
            elif cmd == 'q': break
            cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Қате: {e}")

def main():
    setup_database()
    while True:
        print("\n--- TSIS 1 Final PhoneBook ---")
        print("1. Тізімді көру (Pagination)")
        print("2. Іздеу (Search by Name/Email)")
        print("3. JSON-ға сақтау (Export)")
        print("4. Шығу")
        choice = input("Таңдаңыз: ")
        if choice == '1': view_paginated()
        elif choice == '2': search_advanced()
        elif choice == '3': export_to_json()
        elif choice == '4': break

if __name__ == "__main__":
    main()