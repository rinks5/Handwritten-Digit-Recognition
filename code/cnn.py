from keras.models import load_model
import imutils
import cv2
import numpy as np
class model(object):
	"""docstring for model"""
	def __init__(self):
		super(model, self).__init__()
		self.loaded_model=None

	def load_model(self,file_path):
		self.loaded_model=load_model(file_path)

	def predict(self,images):
		for image in images["images"]:
			t_img = image["image"].copy()
			batch = np.expand_dims(t_img,axis=0)
			batch = np.expand_dims(batch,axis=3)
			nbr = self.loaded_model.predict_classes(batch/255,batch_size=86)
			cv2.putText(images["orignal_image"], str(int(nbr[0])), (image["location"]["x"], image["location"]["y"]),cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 1)
			image["output"]=nbr[0]
		return images