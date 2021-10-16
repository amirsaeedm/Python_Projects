from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('codemy.ico')
root.geometry("400x600")

def save_rec():
	conn = sqlite3.connect('address_book.db')
	cur = conn.cursor()

	record_id=delete_box.get()

	cur.execute("""UPDATE address SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		zipcode = :zipcode

		WHERE oid = :oid""",
		{
		'first':f_name_e.get(),
		'last':l_name_e.get(),
		'address':address_e.get(),
		'city':city_e.get(),
		'state':state_e.get(),
		'zipcode':zipcode_e.get(),
		'oid':record_id
		})

	conn.commit()
	conn.close()

	f_name_e.delete(0,END)
	l_name_e.delete(0,END)
	address_e.delete(0,END)
	city_e.delete(0,END)
	state_e.delete(0,END)
	zipcode_e.delete(0,END)

	top.destroy()

def edit_rec():
	global top
	top = Tk()
	top.title('Codemy.com - Learn To Code!')
	top.iconbitmap('codemy.ico')
	top.geometry("400x200")
	
	global f_name_e
	global l_name_e
	global address_e
	global city_e
	global state_e
	global zipcode_e

	f_name_e = Entry(top,width=30)
	f_name_e.grid(row=0,column=1,padx=20,pady=(10,0)) 
	l_name_e = Entry(top,width=30)
	l_name_e.grid(row=1,column=1,padx=20)
	address_e = Entry(top,width=30)
	address_e.grid(row=2,column=1,padx=20)
	city_e = Entry(top,width=30)
	city_e.grid(row=3,column=1,padx=20)
	state_e = Entry(top,width=30)
	state_e.grid(row=4,column=1,padx=20)
	zipcode_e = Entry(top,width=30)
	zipcode_e.grid(row=5,column=1,padx=20)

	f_name_label = Label(top,text="First Name")
	f_name_label.grid(row=0,column=0,pady=(10,0)) 
	l_name_label = Label(top,text="Last Name")
	l_name_label.grid(row=1,column=0)
	address_label = Label(top,text="Address")
	address_label.grid(row=2,column=0)
	city_label = Label(top,text="City")
	city_label.grid(row=3,column=0)
	state_label = Label(top,text="State")
	state_label.grid(row=4,column=0)
	zipcode_label = Label(top,text="Zip Code")
	zipcode_label.grid(row=5,column=0)

	save_btn = Button(top,text='Save Record',command=save_rec)
	save_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=145)
	
	conn = sqlite3.connect('address_book.db')
	cur = conn.cursor()
	record_id = delete_box.get()

	cur.execute("SELECT * FROM address WHERE oid= "+record_id)
	records = cur.fetchall()

	for rec in records:
		f_name_e.insert(0, rec[0])
		l_name_e.insert(0, rec[1])
		address_e.insert(0, rec[2])
		city_e.insert(0, rec[3])
		state_e.insert(0, rec[4])
		zipcode_e.insert(0, rec[5])

	conn.commit()
	conn.close()

def delete_rec():
	conn = sqlite3.connect('address_book.db')
	cur = conn.cursor()

	cur.execute("DELETE from address WHERE oid = " + delete_box.get())

	conn.commit()
	conn.close()	

def submit():
	conn = sqlite3.connect('address_book.db')
	cur = conn.cursor()

	# Table addess created in last program
	conn.execute("INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
				{
					'f_name': f_name.get(),
					'l_name': l_name.get(),
					'address': address.get(),
					'city': city.get(),
					'state': state.get(),
					'zipcode': zipcode.get()
				})
	
	conn.commit()
	conn.close()

	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)

def query():
	conn = sqlite3.connect('address_book.db')
	cur = conn.cursor()

	# oid is primary key in DB
	cur.execute("SELECT *,oid FROM address")

	#cur.fetchone()
	#cur.fetchmany(50)
	records = cur.fetchall() # DB fetched as List of tuples, each tuple is a row

	# show all tuples in DB per line 
	# print_rec = ""
	# for rec in records:
	# 	print_rec += str(rec) + "\n"

	# show Names in DB per line 
	print_rec = ""
	for rec in records:
		print_rec += str(rec[0])+" "+str(rec[1])+"\t"+str(rec[6])+"\n"
	
	query_label = Label(root,text=print_rec)
	query_label.grid(row=12,column=0,columnspan=2)
	conn.commit()
	conn.close()

# Make sure to define Grid in next line, otherwise code will give error, that .get() is not available 
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0)) # Pady only to top, not to bottom
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
address = Entry(root,width=30)
address.grid(row=2,column=1,padx=20)
city = Entry(root,width=30)
city.grid(row=3,column=1,padx=20)
state = Entry(root,width=30)
state.grid(row=4,column=1,padx=20)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)
delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,padx=20,pady=5)

f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0)) # Pady only to top, not to bottom
l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label = Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label = Label(root,text="City")
city_label.grid(row=3,column=0)
state_label = Label(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label = Label(root,text="Zip Code")
zipcode_label.grid(row=5,column=0)
delete_label = Label(root,text="Select oid #")
delete_label.grid(row=9,column=0,pady=5)

submit_btn = Button(root,text='Add to DB',command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=146)

query_btn = Button(root,text='Show Records',command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

delete_btn = Button(root,text='Delete Record',command=delete_rec)
delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=136)

update_btn = Button(root,text='Edit Record',command=edit_rec)
update_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=143)


root.mainloop()