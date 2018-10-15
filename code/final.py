from image_processing import Image
from cnn import model
import imutils
import cv2
import numpy as np
from keras.models import load_model
from tkinter import Button
from tkinter import Tk
from tkinter import Frame
from tkinter import Canvas
from tkinter import NW
from tkinter import filedialog
from tkinter import *

import PIL.Image, PIL.ImageTk

class Final(object):
	"""docstring for GrayImage"""
	def __init__(self, image):
		super(Final, self).__init__()
		root = Tk()
		root.title("Final")
		root.geometry("600x600")
		root.resizable(0,0) 
		load_model = model()
		load_model.load_model("cnn1.h5")
		images=load_model.predict(image)
		height, width, no_channels = images["orignal_image"].shape
		frame= Frame(root, width = width, height = height, highlightthickness=1,highlightbackground="black")
		canvas = Canvas(frame, width = width, height = height)
		c_img=cv2.cvtColor(images["orignal_image"].copy(),cv2.COLOR_BGR2RGB)
		photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(c_img))
		image_on_canvas =canvas.create_image(0, 0, image=photo, anchor=NW)
		canvas.pack()
		frame.pack()
		frame1=Frame(root,width=350,height=30)
		frame1.pack()
		canvas1=Canvas(frame1,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,30*len(images["images"]),100))
		hbar=Scrollbar(frame1,orient=HORIZONTAL)
		hbar.pack(side=BOTTOM,fill=X)
		hbar.config(command=canvas1.xview)
		canvas1.config(width=300,height=300)
		canvas1.config(xscrollcommand=hbar.set)
		canvass=[]
		photo1=[]
		i=0
		for img in images["images"]:
			canvass.append(Canvas(canvas1, width = 28, height = 80))
			im = img["image"].copy()
			photo1.append(PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(im)))
			canvass[i].create_text(12,10,fill="darkblue",font="Times 20 italic bold",
                        text=img["output"])
			image_on_canvas =canvass[i].create_image(0, 30, image=photo1[i], anchor=NW)
			canvass[i].pack(side=LEFT)
			i+=1
		
		
		canvas1.pack(side=LEFT,expand=True,fill=BOTH)
		root.mainloop()
