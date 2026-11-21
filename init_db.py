"""Creates users.db and inserts sample users (passwords are stored hashed)."""
import sqlite3
from werkzeug.security import generate_password_hash

con = sqlite3.connect("users.db")
con.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL)""")
for name, pwd in [("admin", "admin123"), ("student", "pass@123")]:
    con.execute("INSERT OR IGNORE INTO users (username, password_hash) VALUES (?, ?)",
                (name, generate_password_hash(pwd)))
con.commit()
con.close()
print("Database ready: users.db")
