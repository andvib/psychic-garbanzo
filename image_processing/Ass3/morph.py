import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import misc
from scipy.ndimage.morphology import binary_opening, binary_closing, binary_erosion, binary_dilation


def noise_removal(image):
	# Generate disc-matrix
	y,x = np.ogrid[-7: 7+1, -7: 7+1]
	mask = x**2+y**2 <= 7**2
	
	# Remove noise
	temp = binary_opening(image, mask)
	filtered_image = binary_closing(temp, mask)

	return filtered_image

def task2_2_a():
	image = misc.imread('./images/noisy.tiff', True)
	filtered_image = noise_removal(image)
	
	# Plotting
	_, ax = plt.subplots(1,2, figsize=(10,5))
	ax[0].imshow(image, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(filtered_image, cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()
	plt.show()
	misc.imsave('task2_2_a.png', filtered_image)
	
def task2_2_b():
	image = misc.imread('./images/noisy.tiff', True)
	filtered_image = noise_removal(image)
	x = len(image)
	y = len(image[0])
	
	# Image to store number of iterations
	distance = np.zeros((x,y))
	
	# Generate structure element
	se = np.ones((3,3))
	
	i = 0
	nonzero = 1
	while nonzero:
		prev = filtered_image
		filtered_image = binary_erosion(filtered_image, se)
	
		# Check which pixels have changed value
		for j in range(x):
			for k in range(y):
				if prev[j,k] != 0 and filtered_image[j,k] == 0:
					distance[j,k] = i
		
		# Check if any nonzero pixels left in image
		nonzero = np.count_nonzero(filtered_image)
		i += 1
		
	plt.figure()
	plt.imshow(distance, cmap = plt.cm.Greys_r)
	plt.show()
	misc.imsave('task2_2_b.png', distance)
	
def task2_2_c():
	image = misc.imread('./images/noisy.tiff', True)
	filtered_image = noise_removal(image)
	
	eroded = binary_erosion(filtered_image)
	boundary = filtered_image - eroded
	
	plt.figure()
	plt.imshow(boundary, cmap = plt.cm.Greys_r)
	plt.show()
	misc.imsave('boundary.png', boundary)
	
if __name__ == "__main__":
	task2_2_a()
	task2_2_b()
	task2_2_c()