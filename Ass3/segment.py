import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import misc


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
					#print("h")
					s1.append(image[i][j])
				else:
					#print("J)")
					s2.append(image[i][j])

		mean1 = np.average(s1)
		mean2 = np.average(s2)
		print(mean2)
		print(t)
		t_prev = t
		t = (0.5)*(mean1 + mean2)
		
	return t

def task2_1_a():
	image = misc.imread('./images/defective_weld.tif', True)
	x = len(image)
	y = len(image[0])
	print(x)
	print(y)
	t = thresholding(image, 40, 5)
	print(t)
	print(image)
	for i in range(x-1):
		for j in range(y-1):
			if image[i][j] > t:
				image[i][j] = 255
			else:
				image[i][j] = 0
				
	plt.figure()
	plt.imshow(image, cmap = plt.cm.Greys_r)
	plt.show()

if __name__ == "__main__":
	task2_1_a()