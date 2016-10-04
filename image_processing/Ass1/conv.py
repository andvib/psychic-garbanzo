import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import misc


def convolution(image, kernel):
	image_dim = len(image[0])
	kernel_dim = len(kernel[0])
	padding_dim = (int)(kernel_dim/2)
	
	padded_image = padding(image, kernel_dim)
	
	new_image = np.zeros((image_dim,image_dim))
	
	for i in range(padding_dim, image_dim-padding_dim):
		for j in range(padding_dim, image_dim-padding_dim):
			new_value = 0
			for k in range(kernel_dim):
				for l in range(kernel_dim):
					new_value += (int)(kernel[k][l] * padded_image[i-padding_dim+k][j-padding_dim+l])
			new_image[i-padding_dim][j-padding_dim] = (int)(new_value)
	print("se det")
	return new_image
	
def convolution_color(image, kernel):
	image_dim = len(image[0])
	
	r = convolution(image[..., 0],kernel)  # Equivalent to image[:, :, 0]
	g = convolution(image[..., 1],kernel)
	b = convolution(image[..., 2],kernel)

	new_image = np.zeros_like(image)
	new_image[:,:,0] = r
	new_image[:,:,1] = g
	new_image[:,:,2] = b
	
	#new_image[:,:,2] = convolution(image[:,:,0], kernel)
	#new_image[:,:,1] = convolution(image[:,:,1], kernel)
	#new_image[:,:,0] = convolution(image[:,:,2], kernel)
	#print(new_image)
	return new_image
	
def padding(image, kernel_size):
	padding_dim = (int)(kernel_size/2)
	image_dim = len(image[0])
	new_dim = image_dim + padding_dim*2
	new_image = np.zeros((new_dim,new_dim))

	for i in range(image_dim):
		for j in range(image_dim):
			new_image[i+padding_dim][j+padding_dim] = image[i][j]
	return new_image

			
def grey(image):
	image_dim = len(image[0])
	new_image = np.zeros((image_dim,image_dim))
	for i in range(image_dim):
		for j in range(image_dim):
			new_value = np.average(image[i][j])
			new_image[i][j] = new_value	
	return new_image		

if __name__ == "__main__":
	image = misc.imread('./images/lake.tiff')
	
	#n = 0.11111111
	kernel = np.array(([1,0,-1],
			[2,0,-2],
			[1,0,-1]),
			dtype=np.float32)
	kernel2 = np.array(([1,2,1],
			[0,0,0],
			[-1,-2,-1]),
			dtype=np.float32)
	#kernel = np.array(([0.00390625,0.015625,0.0234375,0.015625,0.00390625],
	#				   [0.015625,0.0625,0.09375,0.0625,0.015625],
	#				   [0.0234375,0.09375,0.140625,0.09375,0.0234375],
	#				[0.015625,0.0625,0.09375,0.0625,0.015625],
	#				[0.00390625,0.015625,0.0234375,0.015625,0.00390625]),
	#				   dtype=np.float32)
						
	grey_image = grey(image)
	#print(grey_image)
	new_image = convolution(grey_image,kernel2)
	new_image2 = convolution(grey_image,kernel)
	new_image3 = np.zeros_like(image)
	new_image3 = np.sqrt(np.square(new_image)+np.square(new_image2))
	#new_image = convolution_color(image, kernel)
	_, ax = plt.subplots(1,2, figsize=(20,18))
	ax[0].imshow(new_image3, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	#ax[1].imshow(new_image2, cmap = plt.cm.Greys_r)
	#ax[1].set_axis_off()
	#ax[0].imshow(image)
	#ax[0].set_axis_off()
	#ax[1].imshow(new_image)
	#ax[1].set_axis_off()
	
		
	
	plt.show()
