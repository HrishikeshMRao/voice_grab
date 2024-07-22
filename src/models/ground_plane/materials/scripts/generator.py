import os

import cv2
import numpy as np

for i in range(2,3):
	image = cv2.imread('/home/fiend/.gazebo/models/ground_plane/materials/texture/'+str(i)+'.png',cv2.IMREAD_GRAYSCALE)
	image = cv2.bitwise_not(image)

	filter_size = 18
	filter_kernel = np.ones((filter_size, filter_size), dtype=np.uint8)

	# Perform convolution
	filtered_image = cv2.filter2D(image, -1, filter_kernel)
	filtered_image = cv2.bitwise_not(filtered_image)

	# Threshold the image
	_, thresholded_image = cv2.threshold(filtered_image, 254, 255, cv2.THRESH_BINARY)

	cv2.imwrite('/home/fiend/.gazebo/models/ground_plane/materials/texture/'+str(i)+'.png', thresholded_image)
