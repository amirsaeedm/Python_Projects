from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('codemy.ico')


def Open():
	global my_image
	root_filename = filedialog.askopenfilename(initialdir='D:/Python_Projects/Tkinter',
	title='Select a File',
	filetypes=(('png Files','*.png'),('All Files','*.*')))

	my_label = Label(root,text=root_filename).pack()
	my_image = ImageTk.PhotoImage(Image.open(root_filename))
	photo_label = Label(root,image=my_image).pack()



btn = Button(root,text='Open File',command=Open).pack()


root.mainloop()