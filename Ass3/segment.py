import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import misc
import queue
from queue import Queue


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
	active_front = Queue()
	threshold = 100

	new_image = np.zeros((x,y,2))
	new_image[..., 0] = image
	print(seeds[0,1])
	for i in range(len(seeds)):
		print("seed: ", i)
		new_image[seeds[i, 0], seeds[i, 1], 1] = 255
		seed_x = seeds[i, 0]
		seed_y = seeds[i, 1]
		seed_value = new_image[seed_x, seed_y, 0]

		pulled_pixel = seeds[i]
		while any(pulled_pixel):
			for j in range(3):
				#print("j", j)
				for k in range(3):
					#print("k", k)
					if(seed_x+j-1 < 0 or seed_x+j-1 >= x):
						continue
					if(seed_y+j-1 < 0 or seed_y+j-1 >= y):
						continue

					pixel_value = new_image[seed_x+j-1, seed_y+k-1, 0]
					print(pixel_value - seed_value)
					homogeneity = abs(pixel_value - seed_value) < threshold
					label = new_image[seed_x+j-1, seed_y+k-1, 1]

					if(homogeneity and not label):
						new_image[seed_x+j-1, seed_y+k-1, 1] = 255
						active_front.put((seed_x+j-1, seed_y+k-1))
			
			try:
				pulled_pixel = active_front.get_nowait()
			except queue.Empty as e:
				break

	return new_image[..., 1]
				

def task2_1_a():
	image = misc.imread('./images/defective_weld.tif', True)
	x = len(image)
	y = len(image[0])
	t = thresholding(image, 150, 1)

	for i in range(x-1):
		for j in range(y-1):
			if image[i][j] > t:
				image[i][j] = 255
			else:
				image[i][j] = 0
				
	plt.figure()
	plt.imshow(image, cmap = plt.cm.Greys_r)
	plt.show()
	misc.imsave('task2_1_a.png', image)

def task2_1_b():
	image = misc.imread('./images/defective_weld.tif', True)
	x = len(image)
	y = len(image[0])
	seeds = np.array(((250,140),(1,8)))#,(2,8)))
	new_image = region_growing(image, seeds)

	plt.figure()
	plt.imshow(new_image, cmap = plt.cm.Greys_r)
	plt.show()

if __name__ == "__main__":
	#task2_1_a()
	task2_1_b()
