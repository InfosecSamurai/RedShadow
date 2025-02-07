import sqlite3

DB_PATH = "redshadow.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT,
                        module TEXT,
                        action TEXT,
                        result TEXT)''')
    conn.commit()
    conn.close()

def log_event(module, action, result):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (timestamp, module, action, result) VALUES (DATETIME('now'), ?, ?, ?)",
                   (module, action, result))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()