from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('codemy.ico')

def open():
	global my_image
	top = Toplevel()
	top.title('Another Window')
	top.iconbitmap('codemy.ico')
	lbl = Label(top,text="Hello").pack()
	my_image = ImageTk.PhotoImage(Image.open('images/aspen.png'))
	my_label = Label(top,image=my_image).pack()
	btn2 = Button(top,text="close window",command=top.destroy).pack()

btn = Button(root,text="show 2nd window",command=open).pack()
btn3 = Button(root,text="close main window",command=root.destroy).pack()

root.mainloop()