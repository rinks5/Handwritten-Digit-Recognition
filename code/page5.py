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
import PIL.Image, PIL.ImageTk
import page6
def next(root,image):
	root.destroy()
	page6w = page6.Segmentation(image)

class MorphologyClose(object):
	"""docstring for GrayImage"""
	def __init__(self, image):
		super(MorphologyClose, self).__init__()
		root = Tk()
		root.title("MorphologyClose")
		root.geometry("600x600")
		root.resizable(0,0) 
		im = image.apply_morphology_close()
		height, width = im.shape
		frame= Frame(root, width = width, height = height, highlightthickness=1,highlightbackground="black")
		canvas = Canvas(frame, width = width, height = height)
		
		photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(im))
		image_on_canvas =canvas.create_image(0, 0, image=photo, anchor=NW)
		canvas.pack()
		frame.pack()
		redbutton = Button(root, text = "Next",command=lambda:next(root,image))
		redbutton.pack()
		root.mainloop()
