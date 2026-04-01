params = {
    "host": "localhost",
    "database": "phonebook",
    "user": "postgres",
    "password": "123"
}

CREATE_TABLE_COMMAND = """
CREATE TABLE IF NOT EXISTS contacts (
    contact_id SERIAL PRIMARY KEY,
    contact_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL UNIQUE
);
"""