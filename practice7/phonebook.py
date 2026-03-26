#1
def insert_contact(name, phone):
    sql = "INSERT INTO contacts(contact_name, phone_number) VALUES(%s, %s);"
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (name, phone))
    print(f"Contact {name} added successfully!")

#2
def insert_many_from_csv(file_path):
    sql = "INSERT INTO contacts(contact_name, phone_number) VALUES(%s, %s);"
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # тақырыбын аттап өту
        data = [row for row in reader]
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, data) # Бірден бірнешеуін қосады

#3
def insert_safe(name, phone):
    sql = "INSERT INTO contacts(contact_name, phone_number) VALUES(%s, %s) ON CONFLICT (phone_number) DO NOTHING;"
    

