import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


def grey_one(image):
	new_image = np.zeros((512,512))
	for i in range(512):
		for j in range(512):
			new_value = np.average(image[i][j])
			new_image[i][j] = new_value
	return new_image

def grey_two(image):
	new_image = np.zeros((512,512))
	for i in range(512):
		for j in range(512):
			new_image[i][j] = 0.2126*image[i][j][0] + 0.7152*image[i][j][1]\
													+ 0.0722*image[i][j][2]
	return new_image

def main():
	image = misc.imread('./images/lake.tiff')

	grey_image1 = grey_one(image)
	grey_image2 = grey_two(image)

	_, ax = plt.subplots(1,2, figsize=(10,8))
	ax[0].imshow(grey_image1, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(grey_image2, cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()
	plt.show()
	
	misc.imsave('task21a-average.png', grey_image1)
	misc.imsave('task21a-weighted.png', grey_image2)

if __name__ == "__main__":
	main()