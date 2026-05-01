import psycopg2
from config import db_config  # config.py-дан мәліметтерді шақыру

def get_connection():
    return psycopg2.connect(
        host=db_config["host"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"],
        port=db_config["port"]
    )

def save_game(username, score, level):
    conn = get_connection()
    cur = conn.cursor()
    # Ойыншыны қосу немесе ID алу
    cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO UPDATE SET username = EXCLUDED.username RETURNING id", (username,))
    p_id = cur.fetchone()[0]
    # Сессияны сақтау
    cur.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)", (p_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

def get_leaderboard():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.username, s.score, s.level_reached 
            FROM game_sessions s JOIN players p ON s.player_id = p.id 
            ORDER BY s.score DESC LIMIT 10
        """)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    except: return []