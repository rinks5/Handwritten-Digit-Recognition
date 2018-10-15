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
from tkinter import BOTH
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import page1
root=None
def next(root1,image):
	root1.destroy()
	page1w = page1.GrayImage(image)
def file_dialog():
	root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/kishan/Desktop/project/code",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	# print(root.filename)
	# image=cv2.imread("C:/Users/kishan/pqr4.jpg")
	# image = imutils.resize(image,width=320)
	# photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(image))
	# canvas.itemconfig(image_on_canvas , image=photo,tag=NORMAL)
	filename = root.filename
	root.destroy()
	root1 = Tk()
	root1.title("Image")
	root1.geometry("600x600")
	root1.resizable(0,0) 
	im = Image(filename)
	c_img=cv2.cvtColor(im.get_image().copy(),cv2.COLOR_BGR2RGB)
	height, width, no_channels = c_img.shape
	frame= Frame(root1, width = width, height = height, highlightthickness=1,highlightbackground="black")
	
	canvas = Canvas(frame, width = width, height = height)
	im = Image(filename)
	photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(c_img))
	image_on_canvas =canvas.create_image(0, 0, image=photo, anchor=NW)
	canvas.pack()
	frame.pack()
	redbutton = Button(root1, text = "Next",command=lambda:next(root1,im))
	redbutton.pack()
	root1.mainloop()    

	
	

def main():
	global image_on_canvas
	global root
	global canvas
	global frame
	# im = Image("pqr4.jpg")
	# img=im.covert_to_gray()
	# img=im.apply_gaussian_blur()
	# img=im.apply_threshold()
	# img=im.apply_canny()
	# img=im.apply_morphology_close()
	# con=im.find_contours()
	# images=im.get_images(con)
	# load_model = model()
	# load_model.load_model("cnn1.h5")
	# images=load_model.predict(images)
	# print(images["images"][1]["output"])
	# cv2.imshow('image',images["images"][1]["image"])
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	root = Tk()
	root.title("Main")
	root.geometry("200x200")
	
	root.resizable(0,0)
	redbutton = Button(root, text = "Upload Image",command=file_dialog)
	redbutton.pack()

	closebutton = Button(root, text = "Cancel",command=lambda : root.destroy())
	closebutton.pack()
	
	
	root.mainloop()    



if __name__ == '__main__':
	main()