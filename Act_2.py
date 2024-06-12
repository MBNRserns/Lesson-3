from tkinter import *

root = Tk()
root.geometry("300x400")

w=Label(root,text='FOOD ITEMS', font="50")
w.pack()

listbox =Listbox(root, height=10,width=15,bg="gray",activestyle='dotbox',font="Helvetica",fg="yellow")
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

listbox.pack()



root.mainloop()