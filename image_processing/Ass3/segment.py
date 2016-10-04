import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import misc
import Queue


def thresholding(image, initial_threshold, delta_t):
	t_prev = 0
	t = initial_threshold
	x = len(image)
	y = len(image[0])

	while(abs(t - t_prev) > delta_t):
		s1 = []
		s2 = []
		
		for i in range(x-1):
			for j in range(y-1):
				if image[i][j] > t:
					s1.append(image[i][j])
				else:
					s2.append(image[i][j])

		mean1 = np.average(s1)
		mean2 = np.average(s2)
		t_prev = t
		t = (0.5)*(mean1 + mean2)
		
	return t

def region_growing(image, seeds):
	x = len(image)
	y = len(image[0])
	active_front = Queue.Queue()
	threshold = 10

	# Create a new image array with two channels. The first channels
	# contains the original intensity values, while the second is
	# contains the label used to track visited pixels.
	new_image = np.zeros((x,y,2))
	new_image[..., 0] = image
	
	# Loop iterating through all the pixels
	for i in range(len(seeds)):
		# Mark seed pixel as visited
		new_image[seeds[i, 0], seeds[i, 1], 1] = 255
		seed_x = seeds[i, 0]
		seed_y = seeds[i, 1]
		seed_value = new_image[seed_x, seed_y, 0]

		pulled_pixel = seeds[i]
		# Loop will continue until there are no new pixels in the active front
		while any(pulled_pixel):
			pulled_x = pulled_pixel[0]
			pulled_y = pulled_pixel[1]
			
			# 8-connectivity
			for j in range(3):
				for k in range(3):
					# Test if pixel is outside image frame
					if(pulled_x+j-1 < 0 or pulled_x+j-1 >= x):
						continue
					if(pulled_y+j-1 < 0 or pulled_y+j-1 >= y):
						continue

					# Test gomogeneity criteria and label
					pixel_value = new_image[pulled_x+j-1, pulled_y+k-1, 0]
					homogeneity = abs(pixel_value - seed_value) < threshold
					label = new_image[pulled_x+j-1, pulled_y+k-1, 1]

					if(homogeneity and not label):
						new_image[pulled_x+j-1, pulled_y+k-1, 1] = 255
						active_front.put((pulled_x+j-1, pulled_y+k-1))
			try:
				pulled_pixel = active_front.get_nowait()
			except Queue.Empty as e:
				break

	return new_image[..., 1]
				

def task2_1_a():
	image = misc.imread('./images/defective_weld.tif', True)
	x = len(image)
	y = len(image[0])
	t = thresholding(image, 150, 1)

	# Set pixels above threshold to 255, and below to 0
	for i in range(x-1):
		for j in range(y-1):
			if image[i][j] > t:
				image[i][j] = 255
			else:
				image[i][j] = 0
				
	# Plotting
	plt.figure()
	plt.imshow(image, cmap = plt.cm.Greys_r)
	plt.show()
	misc.imsave('task2_1_a.png', image)

def task2_1_b():
	image = misc.imread('./images/defective_weld.tif', True)
	x = len(image)
	y = len(image[0])
	
	# Initialize array of seed points
	seeds = np.array(((254,138),(251,296),(238,442),(236,402)))
	new_image = region_growing(image, seeds)

	# Plotting
	_, ax = plt.subplots(1,2, figsize=(10,8))
	ax[0].imshow(image, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(new_image, cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()
	plt.show()
	misc.imsave('task2_1_b.png', new_image)

if __name__ == "__main__":
	task2_1_a()
	task2_1_b()
