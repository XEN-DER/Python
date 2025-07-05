import sqlite3

# Connect to database
db = sqlite3.connect("database.db")
cursorobj = db.cursor()

# New student records to insert
student_records = [
    ("GEORGE", 20, "B"),
    ("HELEN", 21, "A"),
    ("IVAN", 22, "C"),
    ("JULIA", 20, "B"),
    ("KEVIN", 19, "A"),
    ("LISA", 18, "B"),
    ("MIKE", 21, "C"),
    ("NINA", 22, "A"),
    ("OSCAR", 20, "B"),
    ("PAULA", 19, "C")
]

# Insert into table
cursorobj.executemany("INSERT INTO students(name, age, grade) VALUES (?, ?, ?)", student_records)

# Save changes
db.commit()
#delete an element from the table
cursorobj.execute("DELETE FROM students WHERE name = 'OSCAR'")
db.commit()
# modify an element in the table
cursorobj.execute("UPDATE students SET grade = 'A' WHERE name = 'HELEN'")
db.commit()

# Fetch and display all records
cursorobj.execute("SELECT * FROM students")
data = cursorobj.fetchall()

for i in data:
    print(i)

# Close connection
db.close()
