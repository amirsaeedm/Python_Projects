from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('codemy.ico')
root.geometry("400x400")

# Create or connect to DB, if thgis DB does not exist it will be created
conn = sqlite3.connect('address_book.db')

# Create cursor
cur = conn.cursor()

#Create Table
cur.execute(""" CREATE TABLE address (
			first_name text,
			last_name text,
			address text,
			city text,
			state text,
			zipcode integer
			)
			""")

# Commit Changes
conn.commit()

# Close Connection
conn.close()


root.mainloop()