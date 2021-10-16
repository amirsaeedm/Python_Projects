from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('codemy.ico')
root.geometry("400x400")

def show():
	mylabel = Label(root,text=clicked.get()).pack()

options = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
clicked = StringVar()
clicked.set(options[0]) # Set value to dropdown Menu when prog starts

drop_down = OptionMenu(root,clicked,*options)
drop_down.pack()

mybtn = Button(root,text='Show selection',command=show).pack()

root.mainloop()