from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('codemy.ico')

r = IntVar()  # Tkinter Int Variable
r.set('2')
#s = StringVar()  # Tkinter Str Variable
#r.get()       # Get value of Tkinter Variable

MODES = [("Pepperoni","Pepperoni"),("Cheese","Cheese"),
		("Mushroom","Mushroom"),("Onion","Onion")]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
	Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def radiob(value):
	myLable = Label(root,text=value)
	myLable.pack()

# radio_button = Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda: radiob(r.get()))
# radio_button.pack()

# radio_button2 = Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda: radiob(r.get()))
# radio_button2.pack()

# myLable = Label(root,text=pizza.get())
# myLable.pack()

myButton = Button(root,text="Click Here",command=lambda: radiob(pizza.get()))
myButton.pack()

root.mainloop()