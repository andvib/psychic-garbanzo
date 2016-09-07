import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


def transform(image):
	new_image = np.zeros((512,512))
	for i in range(512):
		for j in range(512):
			new_image[i][j] = 255 - image[i][j]
	return new_image
	
def gamma_transform(image, gamma):
	c = 1
	new_image = np.zeros((512,512))
	for i in range(512):
		for j in range(512):
			new_image[i][j] = c * math.pow((image[i][j]/255), gamma)
	return new_image
	
def grey(image):
	new_image = np.zeros((512,512))
	for i in range(512):
		for j in range(512):
			new_value = np.average(image[i][j])
			new_image[i][j] = new_value
	return new_image
	
def main():
	image = misc.imread('./images/lake.tiff')

	grey_image = grey(image)
	grey_trans = transform(grey_image)
	grey_gamma_trans = gamma_transform(grey_image, 1)
	
	_, ax = plt.subplots(1,3, figsize=(20,18))
	ax[0].imshow(grey_image, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(grey_trans, cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()
	ax[2].imshow(grey_gamma_trans, cmap = plt.cm.Greys_r)
	ax[2].set_axis_off()
	plt.show()

	
	
if __name__ == "__main__":
	main()