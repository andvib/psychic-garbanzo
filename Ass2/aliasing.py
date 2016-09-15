import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import misc


def downsample(image):
	#Removes every second row and column
	return image[0::2,0::2]

def convolution(image, kernel):
	image_size = len(image)
	kernel_size = kernel.shape[0]

	#Add padding to both kernel and image. Padding size is twice the
	#image size to ensure enough padding.
	padded_kernel = np.zeros((2*image_size, 2*image_size))
	padded_kernel[(image_size)-(kernel_size/2):(image_size)+(kernel_size/2)+1,
			      (image_size)-(kernel_size/2):(image_size)+(kernel_size/2)+1] = kernel
	padded_image = np.zeros((2*image_size, 2*image_size))
	padded_image[image_size:3*image_size,image_size:3*image_size] = image

	#Fourier transform image and kernel
	fourier_image = np.fft.fft2(padded_image)
	fourier_kernel = np.fft.fft2(padded_kernel)
	
	#Convolution
	fourier_convolved = fourier_image * fourier_kernel
	image_convolved = np.fft.ifft2(fourier_convolved).real

	kernel_size = padded_kernel.shape[0]
	return image_convolved[:image_size, :image_size]


if __name__ == "__main__":
	image = misc.imread('./images/bricks.tiff', True)
	
	kernel_low = (1.0 / 9) * np.ones((3,3))
	smooth_image = downsample(convolution(image, kernel_low))
	down_image = downsample(image)
	
	_, ax = plt.subplots(1,3, figsize=(27,15))
	ax[0].imshow(image, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(smooth_image, cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()
	ax[2].imshow(down_image, cmap = plt.cm.Greys_r)
	ax[2].set_axis_off()
	plt.show()

	misc.imsave('task2_2/smoothened_image.png', smooth_image)
	misc.imsave('task2_2/downsized_image.png', down_image)