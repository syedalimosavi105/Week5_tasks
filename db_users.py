import sqlite3
from sqlite3 import Connection

DB_FILE = "users.db"

def get_conn(db_file: str) -> Connection:
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row  # enable name-based access to columns
    return conn

def setup_db(conn: Connection):
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER
            )
        """)

def insert_users(conn: Connection, users):
    with conn:
        conn.executemany(
            "INSERT OR IGNORE INTO users (name, email, age) VALUES (?, ?, ?)",
            users
        )

def fetch_all_users(conn: Connection):
    cur = conn.execute("SELECT id, name, email, age FROM users ORDER BY id")
    return cur.fetchall()

def main():
    # sample users to insert
    users_to_add = [
        ("Aisha Khan", "aisha.khan@example.com", 20),
        ("Omar Qureshi", "omar.qureshi@example.com", 22),
        ("Sara Ali", "sara.ali@example.com", 21),
    ]

    conn = get_conn(DB_FILE)
    setup_db(conn)
    insert_users(conn, users_to_add)

    rows = fetch_all_users(conn)

    print("\n--- Users in database ---")
    for r in rows:
        print(f"ID: {r['id']}\tName: {r['name']}\tEmail: {r['email']}\tAge: {r['age']}")
    print(f"Total users: {len(rows)}\n")

    conn.close()

if __name__ == "__main__":
    main()
