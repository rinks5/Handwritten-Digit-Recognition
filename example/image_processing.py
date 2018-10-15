import imutils
import cv2
import numpy as np
from keras.models import load_model

class Image(object):
	"""dfile_pathtring for Image"""
	def __init__(self,image):
		super(Image, self).__init__()
		self.image = image
		self.orignal_image=self.image.copy()
		self.temp_image=None
		self.temp_image1=None

	def get_image(self):
		return self.image
	def makeSquare(self,not_square):
		BLACK = [0,0,0]
		img_dim = not_square.shape
		height = img_dim[0]
		width = img_dim[1]
		if height == width:
			return not_square
		else:
			doublesize=cv2.resize(not_square,(2*width,2*height),interpolation = cv2.INTER_CUBIC)
			height=height*2
			width=width*2
			if height>width:
				pad=int((height-width)/2)
				doublesize_square = cv2.copyMakeBorder(doublesize,0,0,pad,pad,cv2.BORDER_CONSTANT,value=BLACK)
			else:
				pad=int((width-height)/2)
				doublesize_square = cv2.copyMakeBorder(doublesize,pad,pad,0,0,cv2.BORDER_CONSTANT,value=BLACK)
		doublesize_square_dm=doublesize_square.shape
		return doublesize_square

	def resize_to_pixel(self,dimensions,image):
		buffer_pix=4
		dimensions=dimensions-buffer_pix
		squared=image
		r=float(dimensions)/squared.shape[1]
		dim=(dimensions,int(squared.shape[0]*r))
		resized=cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
		img_dim2=resized.shape
		height_r=img_dim2[0]
		width_r=img_dim2[1]
		BLACK=[0,0,0]
		if(height_r>width_r):
			resized=cv2.copyMakeBorder(resized,0,0,0,1,cv2.BORDER_CONSTANT,value=BLACK)
		if(height_r<width_r):
			resized=cv2.copyMakeBorder(resized,1,0,0,0,cv2.BORDER_CONSTANT,value=BLACK)
		p=2
		ReSizeImg = cv2.copyMakeBorder(resized,p,p,p,p,cv2.BORDER_CONSTANT,value=BLACK)
		return ReSizeImg
	def covert_to_gray(self):
		self.image=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
		return self.image

	def apply_gaussian_blur(self):
		self.image=cv2.GaussianBlur(self.image,(3,3),0)
		self.temp_image1=self.image.copy()
		return self.image

	def apply_threshold(self):
		# _,self.image=cv2.threshold(self.image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		self.image=cv2.adaptiveThreshold(self.image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,15,12)
		self.temp_image=self.image.copy()
		return self.image

	def apply_canny(self):
		self.image =cv2.Canny(self.temp_image1,40,90)
		return self.image

	def apply_morphology_close(self):
		self.image=cv2.morphologyEx(self.image,cv2.MORPH_CLOSE,np.ones((2,2),np.uint8))
		return self.image

	def find_contours(self):
		_ ,contours, hier = cv2.findContours(self.image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		return contours

	def get_images(self,contours):
		images={"orignal_image":None,"images":None}
		imgs=[]
		orignal_img=self.orignal_image.copy()
		for c in contours:
			(x,y,w,h) = cv2.boundingRect(c)
			if w>=2 and h>=13 and w<=35 and h<=30:	
				roi = self.temp_image[y:y+h,x:x+w]
				# ret,roi = cv2.threshold(roi,127,255,cv2.THRESH_BINARY_INV)
				squared=self.makeSquare(roi)
				final=self.resize_to_pixel(28,squared)
				final=np.array(final)
				imgs.append({"image":final,"location":{"x":x,"y":y},"output":None})
				cv2.rectangle(orignal_img,(x,y),(x+w,y+h),(0,0,255),2)
		images["orignal_image"]=orignal_img
		images["images"]=imgs
		return images

def main():
	im = Image("pqr4.jpg")
	img=im.covert_to_gray()
	img=im.apply_gaussian_blur()
	img=im.apply_threshold()
	img=im.apply_canny()
	img=im.apply_morphology_close()
	con=im.find_contours()
	images=im.get_images(con)
	cv2.imshow('image',images["orignal_image"])
	cv2.waitKey(0)
	cv2.destroyAllWindows()
if __name__ == '__main__':
	main()