from tkinter import *

root = Tk()
root.geometry("300x150")

w=Label(root,text='Chocos And Icecreams', font="50")
w.pack()

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

b1_button = Button(frame, text="Choco", fg="red",bg="beige")
b1_button.pack(side=LEFT)

b2_button = Button(frame, text="Dark Choco", fg="green",bg="beige")
b2_button.pack(side=LEFT)

b3_button = Button(frame, text="White Choco", fg="blue",bg="beige")
b3_button.pack(side=LEFT)

b4_button = Button(bottomframe, text="Pastry", fg="red",bg="yellow")
b4_button.pack(side=BOTTOM)

b5_button = Button(bottomframe, text="Cake", fg="red",bg="pink")
b5_button.pack(side=BOTTOM)

b6_button = Button(bottomframe, text="Tiramisu", fg="red",bg="cyan")
b6_button.pack(side=BOTTOM)



root.mainloop()