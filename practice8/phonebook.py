import sqlite3
import csv
import os

def get_connection():
    return sqlite3.connect("phonebook.db")


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("--- Database initialized successfully! ---")


def insert_from_console():
    username = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (?, ?)", (username, phone))
    conn.commit()
    conn.close()
    print(f"Contact {username} added.")


def insert_from_csv():
    if not os.path.exists("contacts.csv"):
        print("Error: contacts.csv file not found!")
        return
    conn = get_connection()
    cur = conn.cursor()
    count = 0
    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                cur.execute("INSERT INTO phonebook (username, phone) VALUES (?, ?)", (row[0], row[1]))
                count += 1
    conn.commit()
    conn.close()
    print(f"{count} contacts imported from CSV.")


def query_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print("\n--- Phonebook Contacts ---")
    if not rows:
        print("No contacts found.")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
    conn.close()


def search_pattern():
    pattern = input("Enter search pattern (name or phone): ")
    conn = get_connection()
    cur = conn.cursor()
   
    cur.execute("SELECT * FROM phonebook WHERE username LIKE ? OR phone LIKE ?", 
                ('%'+pattern+'%', '%'+pattern+'%'))
    rows = cur.fetchall()
    print("\n--- Search Results ---")
    if not rows:
        print("Nothing found.")
    for row in rows:
        print(row)
    conn.close()


    name = input("Enter username: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cur = conn.cursor()
   
    cur.execute("SELECT id FROM phonebook WHERE username = ?", (name,))
    if cur.fetchone():
        cur.execute("UPDATE phonebook SET phone = ? WHERE username = ?", (phone, name))
        print(f"Contact {name} updated.")
    else:
        cur.execute("INSERT INTO phonebook (username, phone) VALUES (?, ?)", (name, phone))
        print(f"New contact {name} inserted.")
    conn.commit()
    conn.close()

def paginated_query():
    try:
        limit = int(input("How many records per page (Limit): "))
        offset = int(input("How many records to skip (Offset): "))
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook LIMIT ? OFFSET ?", (limit, offset))
        rows = cur.fetchall()
        print(f"\n--- Results (Limit {limit}, Offset {offset}) ---")
        for row in rows:
            print(row)
        conn.close()
    except ValueError:
        print("Please enter a valid number.")


def delete_contact():
    value = input


if __name__ == "__main__":
    create_table() 
    while True:
        print("\n=== Phonebook Application (Practice 8) ===")
        print("1. Add from console")
        print("2. Add from CSV")
        print("3. Show all contacts")
        print("6. Search by pattern (LIKE)")
        print("7. Upsert user (Update/Insert)")
        print("8. Pagination (Limit/Offset)")
        print("9. Delete contact")
        print("10. Bulk insert (Loop)")
        print("11. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1": insert_from_console()
        elif choice == "2": insert_from_csv()
        elif choice == "3": query_all()
        elif choice == "6": search_pattern()
        elif choice == "7": upsert_user()
        elif choice == "8": paginated_query()
        elif choice == "9": delete_contact()
        elif choice == "10": bulk_insert()
        elif choice == "11": 
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")