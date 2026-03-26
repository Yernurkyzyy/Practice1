#1
# config.py - Database connection parameters
params = {
    "host": "localhost",
    "database": "phonebook_db",
    "user": "postgres",
    "password": "your_password" 
}


CREATE_TABLE_COMMAND = """
CREATE TABLE IF NOT EXISTS contacts (
    contact_id SERIAL PRIMARY KEY,
    contact_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL UNIQUE
);
"""


CSV_FILE_PATH = "contacts.csv"


