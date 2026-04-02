import sqlite3
import csv
import os

# Базаға қосылу (PostgreSQL орнына SQLite)
def get_connection():
    return sqlite3.connect("phonebook.db")

# Кестені құру
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonebook(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            phone TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

# Консольдан қосу
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO phonebook (username, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()
    print(f"Contact {name} added.")

# Барлық контактіні көрсету
def show_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phonebook")
    rows = cursor.fetchall()
    conn.close()
    print("\n--- Phonebook Contacts ---")
    if not rows:
        print("No contacts found.")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")

# Атын өшіру
def delete_contact():
    name = input("Enter name to delete: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM phonebook WHERE username = ?", (name,))
    conn.commit()
    conn.close()
    print(f"Contact {name} deleted.")

if __name__ == "__main__":
    create_table()
    while True:
        print("\n--- MENU ---")
        print("1. Add from console")
        print("2. Show all contacts")
        print("3. Delete contact")
        print("4. Exit")
        choice = input("Select option: ")
        
        if choice == "1": insert_from_console()
        elif choice == "2": show_contacts()
        elif choice == "3": delete_contact()
        elif choice == "4": break
        else: print("Invalid choice!")