import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import misc


def downsample(image):
	return image[0::2,0::2]


if __name__ == "__main__":
	image = misc.imread('./images/bricks.tiff', True)
	print(len(image[0]))
	new_image = downsample(image)
	print(len(new_image[1]))
	
	plt.figure()
	plt.imshow(new_image, cmap = plt.cm.Greys_r)
	plt.show()