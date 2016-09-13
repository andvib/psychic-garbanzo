import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import misc


def convolution(image, kernel):
	fourier_image = np.fft.fft2(image)
	fourier_kernel = np.fft.fft2(kernel)
	fourier_convolved = fourier_image * fourier_kernel
	return np.fft.ifft2(fourier_convolved)





if __name__ == "__main__":
	image = misc.imread('./images/jelly-beans.tiff', True)
	image_size = len(image)
	
	kernel = (1.0 / 9) * np.ones((3,3))
	kernel_size = kernel.shape[0]
	padded_kernel = np.zeros((image_size,image_size))
	padded_kernel[(image_size/2)-(kernel_size/2):(image_size/2)+(kernel_size/2)+1,
			      (image_size/2)-(kernel_size/2):(image_size/2)+(kernel_size/2)+1] = kernel

	convolved_image = convolution(image, padded_kernel)
	print(convolved_image)
	_, ax = plt.subplots(1,2, figsize=(20,18))
	ax[0].imshow(image, cmap = plt.cm.Greys_r)
	ax[0].set_axis_off()
	ax[1].imshow(convolved_image, cmap = plt.cm.Greys_r)
	ax[1].set_axis_off()