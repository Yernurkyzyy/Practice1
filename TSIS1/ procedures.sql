-- Телефон қосу
CREATE OR REPLACE PROCEDURE add_phone(p_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE v_id INT;
BEGIN
    SELECT id INTO v_id FROM contacts WHERE first_name = p_name LIMIT 1;
    IF v_id IS NOT NULL THEN
        INSERT INTO phones (contact_id, phone, type) VALUES (v_id, p_phone, p_type);
    END IF;
END; $$;

-- Топқа ауыстыру
CREATE OR REPLACE PROCEDURE move_to_group(p_name VARCHAR, p_group VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE v_g_id INT;
BEGIN
    INSERT INTO groups (name) VALUES (p_group) ON CONFLICT (name) DO NOTHING;
    SELECT id INTO v_g_id FROM groups WHERE name = p_group;
    UPDATE contacts SET group_id = v_g_id WHERE first_name = p_name;
END; $$;

-- Кеңейтілген іздеу (Email мен телефонды қоса)
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(id INT, name TEXT, email VARCHAR, phones TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, (c.first_name || ' ' || c.last_name), c.email, string_agg(p.phone, ', ')
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.first_name ILIKE '%' || p_query || '%' 
       OR c.email ILIKE '%' || p_query || '%' 
       OR p.phone ILIKE '%' || p_query || '%'
    GROUP BY c.id;
END; $$ LANGUAGE plpgsql;