import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

dogphoto = PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
label.grid(row=1,column=1,sticky = NW)


#Text Box Labels
label1 = tk.Label(window,text="Client Database")
label1.grid(row=1,column=3)
label2 = tk.Label(window,text="Name")
label2.grid(row=2,column=1)
label3 = tk.Label(window,text="Type")
label3.grid(row=2,column=2)
label4 = tk.Label(window,text="Breed")
label4.grid(row=2,column=3)
label5 = tk.Label(window,text="Owner")
label5.grid(row=2,column=4)
label5 = tk.Label(window,text="Birthdate")
label5.grid(row=2,column=5)
label5 = tk.Label(window,text="Search By Name")
label5.grid(row=1,column=4, sticky = N)


# Text boxes
e1 = tk.Entry(window)
e1.grid(row=3,column=1)
e2 = tk.Entry(window)
e2.grid(row=3,column=2)
e3 = tk.Entry(window)
e3.grid(row=3,column=3)
e4 = tk.Entry(window)
e4.grid(row=3,column=4)
e5 = tk.Entry(window)
e5.grid(row=3,column=5)
e6 = tk.Entry(window)
e6.grid(row=1,column=5,sticky = N)


#Buttons

b1 = tk.Button(window,text="<Previous")
b1.grid(row=4,column=1,sticky = SW)
b2 = tk.Button(window,text="Save Entry")
b2.grid(row=4,column=3,sticky = S)
b3 = tk.Button(window,text= "Next>")
b3.grid(row=4, column=5,sticky = SE)













window.mainloop()