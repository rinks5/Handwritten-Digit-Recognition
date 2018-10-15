from pyzbar import pyzbar
import argparse
import cv2
import imutils
from image_processing import Image
from cnn import model
class Total(object):
	"""docstring for Total"""
	def __init__(self, image):
		super(Total, self).__init__()
		self.image = image

	def get_id(self):
		return pyzbar.decode(self.image)[0].data.decode("utf-8")
	
	def get_total(self):
		image = self.image.copy()
		image = imutils.resize(image,height=500)
		crop_imgs=[]
		crop_imgs.append(image[443:488,107:216])
		crop_imgs.append(image[443:488,220:323])
		crop_imgs.append(image[443:488,325:450])
		crop_imgs.append(image[443:488,451:604])
		section_and_total=[]
		total=0
		for crop_img in crop_imgs:
			img=crop_img.copy()
			im = Image(img)
			img=im.covert_to_gray()
			img=im.apply_gaussian_blur()
			img=im.apply_threshold()
			img=im.apply_canny()
			img=im.apply_morphology_close()
			con=im.find_contours()
			images=im.get_images(con)
			load_model = model()
			load_model.load_model("cnn1.h5")
			images=load_model.predict(images)
			output=""
			if len(images["images"]) == 1:
				output+=images["images"][0]["output"]
			else:
				if images["images"][0]["location"]["x"]<images["images"][1]["location"]["x"]:
					output+=images["images"][0]["output"]
					output+=images["images"][1]["output"]
				else:
					output+=images["images"][1]["output"]
					output+=images["images"][0]["output"]
			total+=int(output)
			section_and_total.append(int(output))
		section_and_total.append(total)
		return section_and_total

def main():
	to=Total(cv2.imread("s10.png"))
	section_and_total=to.get_total()
	print(section_and_total)
if __name__ == '__main__':
	main()