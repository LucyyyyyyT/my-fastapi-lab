import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create users table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        age INTEGER NOT NULL
    )
''')

# Create messages table
c.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# Seed some test data so your / route has something to display
c.execute("INSERT OR IGNORE INTO users (username, age) VALUES ('alice', 30)")
c.execute("INSERT OR IGNORE INTO users (username, age) VALUES ('bob', 25)")
c.execute("INSERT OR IGNORE INTO users (username, age) VALUES ('carol', 22)")

c.execute("INSERT OR IGNORE INTO messages (text, user_id) VALUES ('Hello world!', 1)")
c.execute("INSERT OR IGNORE INTO messages (text, user_id) VALUES ('FastAPI is awesome', 2)")
c.execute("INSERT OR IGNORE INTO messages (text, user_id) VALUES ('Loving this project!', 3)")

conn.commit()
conn.close()
print("Database created successfully!")