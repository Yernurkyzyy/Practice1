-- 1. Кестелерді құру
CREATE TABLE IF NOT EXISTS groups (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS contacts (
    id         SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name  VARCHAR(50),
    email      VARCHAR(100),
    birthday   DATE,
    group_id   INTEGER REFERENCES groups(id)
);

CREATE TABLE IF NOT EXISTS phones (
    id         SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone      VARCHAR(20)  NOT NULL,
    type       VARCHAR(10)  CHECK (type IN ('home', 'work', 'mobile'))
);

-- 2. Бастапқы топтар
INSERT INTO groups (name) VALUES ('Family'), ('Work'), ('Friends'), ('Other') ON CONFLICT DO NOTHING;

-- 3. Іздеу функциясы (Email, Name, Phones бойынша)
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (contact_id INT, full_name TEXT, contact_email VARCHAR, all_phones TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT c.id, 
           (c.first_name || ' ' || c.last_name) AS full_name, 
           c.email, 
           string_agg(p.phone, ', ') AS all_phones
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.first_name ILIKE '%' || p_query || '%' 
       OR c.last_name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%'
    GROUP BY c.id;
END;
$$ LANGUAGE plpgsql;

-- 4. Топқа жылжыту процедурасы
CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_group_id INT;
BEGIN
    INSERT INTO groups (name) VALUES (p_group_name) ON CONFLICT DO NOTHING;
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;
    UPDATE contacts SET group_id = v_group_id WHERE first_name = p_contact_name;
END;
$$;