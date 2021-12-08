import tkinter as tk 
from tkinter import *


window = tk.Tk()
entry1 = tk.Entry(window, borderwidth=3)
entry1.grid(row=3, column = 1, columnspan=2)
label1 = tk.Label(window,text="x")
label1.grid(row=3, column = 6, columnspan=2)
entry2 = tk.Entry(window, borderwidth=3)
entry2.grid(row=3, column = 11, columnspan=2)
label2 = tk.Label(window,text="=")
label2.grid(row=3, column = 16, columnspan=2)
entry3 = tk.Entry(window, borderwidth=3)
entry3.grid(row=3, column = 21, columnspan=2)



window.mainloop()
