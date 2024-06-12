from tkinter import *

root = Tk()
root.geometry("150x200")

w=Label(root,text='Listbox', font="50")
w.pack()

scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT,fill=Y)

mylist = Listbox(root,yscrollcommand=scroll_bar.set)

mylist.insert(END, "Minecraft")
mylist.insert(END, "Fortnite")
mylist.insert(END, "Rocket League")
mylist.insert(END, "Valorant")
mylist.insert(END, "Brawl Stars")
mylist.insert(END, "Overwatch")
mylist.insert(END, "Mario Kart")
mylist.insert(END, "Fall Guys")
mylist.insert(END, "FIFA")
mylist.insert(END, "Splatoon")
mylist.insert(END, "Minecraft")
mylist.insert(END, "Fortnite")
mylist.insert(END, "Rocket League")
mylist.insert(END, "Valorant")
mylist.insert(END, "Brawl Stars")
mylist.insert(END, "Overwatch")
mylist.insert(END, "Mario Kart")
mylist.insert(END, "Fall Guys")
mylist.insert(END, "FIFA")
mylist.insert(END, "Splatoon")
mylist.insert(END, "Minecraft")
mylist.insert(END, "Fortnite")
mylist.insert(END, "Rocket League")
mylist.insert(END, "Valorant")
mylist.insert(END, "Brawl Stars")
mylist.insert(END, "Overwatch")
mylist.insert(END, "Mario Kart")
mylist.insert(END, "Fall Guys")
mylist.insert(END, "FIFA")
mylist.insert(END, "Splatoon")

mylist.pack(side=LEFT,fill=BOTH)

scroll_bar.config(command=mylist.yview)

root.mainloop()