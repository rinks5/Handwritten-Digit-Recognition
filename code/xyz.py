from tkinter import *
root=Tk()
frame=Frame(root,width=300,height=300)
frame.grid(row=0,column=0)
canvas=Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()