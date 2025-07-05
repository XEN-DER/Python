import sqlite3

# Create the database or connect if it already exists
db = sqlite3.connect("database.db")
cursorobj = db.cursor()  # Create a cursor object to execute SQL commands

# Create table if it doesn't exist
cursorobj.execute('''
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')

# Save the changes
db.commit()

# Optional: close the database connection
db.close()
