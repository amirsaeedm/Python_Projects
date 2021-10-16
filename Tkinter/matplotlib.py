from tkinter import *
from PIL import ImageTk,Image
import numpy as np
from matplotlib import pyplot as plt 


root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap('codemy.ico')
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000,25000,5000) # normal(Avg Value, SD, number of data points)
    plt.hist(house_prices,50) # hist(data , number of bins)
    plt.show()

btn = Button(root,text='Graph',comman=graph)
btn.pack()
    
root.mainloop()