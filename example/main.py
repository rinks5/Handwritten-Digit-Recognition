from image_processing import Image
from cnn import model
import imutils
import cv2
import numpy as np
from keras.models import load_model
from tkinter import Button
from tkinter import Tk
from tkinter import Frame
from tkinter import Canvas,Toplevel,Label
from tkinter import NW,N,S,W,E
from tkinter import BOTH
from tkinter import filedialog
from tkinter.ttk import Treeview
import PIL.Image, PIL.ImageTk
from total import Total
import sqlite3
def file_dialog(root,tv):
	filename =  filedialog.askopenfilename(initialdir = "C:/Users/kishan/Desktop/project/example",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
	to=Total(cv2.imread(filename))
	sid=to.get_id()
	section_and_total=to.get_total()
	print(section_and_total)
	print(sid)
	conn = sqlite3.connect('student.db')
	conn.execute(f"INSERT INTO STUDENT VALUES ({sid}, {section_and_total[0]},{section_and_total[1]},\
					 {section_and_total[2]}, {section_and_total[3]},{section_and_total[4]} )");
	tv.insert('', 'end', text=f"{sid}", values=(f'{section_and_total[0]}',f'{section_and_total[1]}',\
					 f'{section_and_total[2]}', f'{section_and_total[3]}',f'{section_and_total[4]}'))
	conn.commit()
	conn.close()
def main():
	root=Tk()
	frame1=Frame(root, width = 600, height = 500)
	frame= Frame(frame1, width = 600, height = 400)
	tv=Treeview(frame)
	redbutton = Button(frame1, text = "Upload Image",command=lambda : file_dialog(root,tv))
	redbutton.pack()
	tv["column"]=('q1','q2','q3','q4','t')
	tv.heading("#0", text='Id', anchor='w')
	tv.column("#0", anchor="w")
	width=70
	tv.heading('q1', text='Question 1')
	tv.column('q1', anchor='center', width=width)
	tv.heading('q2', text='Question 2')
	tv.column('q2', anchor='center', width=width)
	tv.heading('q3', text='Question 3')
	tv.column('q3', anchor='center', width=width)

	tv.heading('q4', text='Question 4')
	tv.column('q4', anchor='center', width=width)

	tv.heading('t', text='Total')
	tv.column('t', anchor='center', width=width)
	tv.grid(sticky = (N,S,W,E))
	conn = sqlite3.connect('student.db')
	cursor = conn.execute("SELECT * from STUDENT")
	for row in cursor:
		tv.insert('', 'end', text=f"{row[0]}", values=(f'{row[1]}',f'{row[2]}',\
					  f'{row[3]}',f'{row[4]}',f'{row[5]}'))
	conn.close()

	frame.pack()
	frame1.pack()
	root.mainloop()	
if __name__ == '__main__':
	main()