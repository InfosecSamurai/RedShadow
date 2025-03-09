import sqlite3
import logging

logging.basicConfig(filename="database.log", level=logging.INFO)
logging.info("Initializing database module...")

DB_PATH = "redshadow.db"

def init_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            timestamp TEXT,
                            module TEXT,
                            action TEXT,
                            result TEXT)''')
        conn.commit()
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error initializing database: {e}")
        raise
    finally:
        if conn:
            conn.close()

def log_event(module, action, result):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (timestamp, module, action, result) VALUES (DATETIME('now'), ?, ?, ?)",
                       (module, action, result))
        conn.commit()
        logging.info(f"Logged event: module={module}, action={action}, result={result}")
    except sqlite3.Error as e:
        logging.error(f"Error logging event: {e}")
        raise
    finally:
        if conn:
            conn.close()

def get_logs():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM logs")
        logs = cursor.fetchall()
        logging.info("Retrieved logs from the database.")
        return logs
    except sqlite3.Error as e:
        logging.error(f"Error retrieving logs: {e}")
        raise
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    init_db()