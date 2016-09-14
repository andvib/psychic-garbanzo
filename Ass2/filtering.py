import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import misc


def convolution(image, kernel):
	image_size = len(image)
	kernel_size = kernel.shape[0]

	padded_kernel = np.zeros((image_size,image_size))
	padded_kernel[(image_size/2)-(kernel_size/2):(image_size/2)+(kernel_size/2)+1,
			      (image_size/2)-(kernel_size/2):(image_size/2)+(kernel_size/2)+1] = kernel
	
	fourier_image = np.fft.fft2(image)
	fourier_kernel = np.fft.fft2(padded_kernel)
	fourier_convolved = fourier_image * fourier_kernel
	image_convolved = np.fft.ifft2(fourier_convolved).real

	kernel_size = padded_kernel.shape[0]
	return np.roll(np.roll(image_convolved, -(kernel_size//2), axis=-1),
											-(kernel_size//2), axis=-2)
											
def hybrid(image1, image2):
	kernel_low = (1.0 / 4) * np.ones((3,3))
	
	#kernel_low = np.array([[0,(1/8),0],
	#				   [(1/8),(1/2),(1/8)],
	#				   [0,(1/8),0]])
	
	low_image = convolution(image1, kernel_low)
	high_image = convolution(image2, (1-kernel_low))
	
	_, ax = plt.subplots(1,3, figsize=(27,15))
	ax[0].imshow(high_image+low_image, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(high_image, cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()
	ax[2].imshow(low_image, cmap = plt.cm.Greys_r)
	ax[2].set_axis_off()
	plt.show()
	
	return high_image + low_image
	
def task_2_1_a():
	image = misc.imread('./images/lake.tiff', True)
	image_size = len(image)
	
	kernel_low = (1.0 / 9) * np.ones((3,3))
	kernel_high = np.array([[0,-1,0],
					   [-1,4,-1],
					   [0,-1,0]])

	convolved_low = convolution(image, kernel_low)
	convolved_high = convolution(image, kernel_high)
	
	_, ax = plt.subplots(1,3, figsize=(27,15))
	ax[0].imshow(image, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(convolved_low, cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()
	ax[2].imshow(convolved_high, cmap = plt.cm.Greys_r)
	ax[2].set_axis_off()
	#plt.show()

	image_amp = np.absolute(np.fft.fft2(image).real)
	convolved_amp_low = np.absolute(np.fft.fft2(convolved_low).real)
	convolved_amp_high = np.absolute(np.fft.fft2(convolved_high).real)
	
	_, ax = plt.subplots(1,3, figsize=(27,15))
	ax[0].imshow(np.fft.fftshift(image_amp), cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(np.fft.fftshift(convolved_amp_low), cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()
	ax[2].imshow(np.fft.fftshift(convolved_amp_high), cmap = plt.cm.Greys_r)
	ax[2].set_axis_off()
	#plt.show()
	
	misc.imsave('task2_1_a/filtered/original.png', image)
	misc.imsave('task2_1_a/filtered/low_pass.png', convolved_low)
	misc.imsave('task2_1_a/filtered/high_pass.png', convolved_high)
	
	misc.imsave('task2_1_a/amp/original_amp.png', image_amp)
	misc.imsave('task2_1_a/amp/low_pass_amp.png', convolved_amp_low)
	misc.imsave('task2_1_a/amp/high_pass_amp.png', convolved_amp_high)
	
def task_2_1_b():
	image = misc.imread('./images/lake.tiff', True)
	image_size = len(image)
	
	kernel_high = np.array([[0,-1,0],
							[-1,4,-1],
							[0,-1,0]])
	
	convolved_image = convolution(image, kernel_high)
	sharpened_image = image + convolved_image
	
	_, ax = plt.subplots(1,2, figsize=(27,15))
	ax[0].imshow(image, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(sharpened_image, cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()
	#plt.show()
	
	misc.imsave('task_2_1_b_original.png', image)
	misc.imsave('task_2_1_b.png', sharpened_image)
	
def task_2_1_c():
	image1 = misc.imread('./images/bush.tiff', True)
	image2 = misc.imread('./images/clinton.tiff', True)
	
	hybrid_image = hybrid(image1, image2)
	
	plt.figure()
	plt.imshow(hybrid_image, cmap = plt.cm.Greys_r)
	#plt.show()
	
if __name__ == "__main__":
	#task_2_1_a()
	#task_2_1_b()
	task_2_1_c()