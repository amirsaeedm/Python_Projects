from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('codemy.ico')

frame = LabelFrame(root,text="This is a Frame", padx=50,pady=50)
frame.pack(padx=50,pady=50)

b = Button(frame,text="Click This, Ok Click This")
b2 = Button(frame,text="Click This, if you want")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)


root.mainloop()