import numpy as np
from PIL import Image

# Turn the picture into an array W x H

def main():
	image, image_arr = load_image("")
	# load picture into Python
	
	x_size, y_size = image.size
	# set image size into x and y
	
	image_E(image_arr, x_size, y_size)
	# set the first image E
	# we are going encrypting this image
	
	two_keys_decryption(image_arr, x_size, y_size, w1, w2)
	# set the two decrypt keys
	
	save_decrypt_image("", image)
	# save the decrypt image which call I
	
	pass
	
def decrypt_image(image_path, key1, key2, outpath = "")