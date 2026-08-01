import sqlite3
import os

DB_NAME = "database/profiles.db"

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    path TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


def get_connection():
    return sqlite3.connect(DB_NAME)


def add_profile(name, path):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO profiles(name, path) VALUES (?, ?)",
        (name, path)
    )
    conn.commit()
    conn.close()


def get_profiles():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, path FROM profiles ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_profile(profile_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM profiles WHERE id=?", (profile_id,))
    conn.commit()
    conn.close()
