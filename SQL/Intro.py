import sqlite3

db=sqlite3.connect("database.db")#create the database or connect if db file exists
c=db.cursor()#create a cursor object to execute SQL commands
