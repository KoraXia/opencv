#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np 

imgName = "image.jpg"

def downSample(img):
	row, col, channel=img.shape
	#print "row "+str(row)+"col "+str(col)
	sizeofimage=(row/2, col/2, channel)
	r=cv2.resize(img, None, fx=0.5, fy=0.5)
	return r

def main():
	#Gaussian Pyramid
	img = cv2.imread(imgName, 1)
	level = 4
	#kernel summarize to 1
	kernel =np.array([[1/16.0], [4/16.0], [6/16.0], [4/16.0], [1/16.0]]) 
	print kernel
	cv2.imshow("level 1", img)
	for l in range(level):
		#gaussian blur
		gauss=cv2.sepFilter2D(img, -1, kernel, kernel)
		#down sample
		img=downSample(gauss)
 
		new_ImgName = 'Gaussian level '+str(l)
		cv2.imshow(new_ImgName, img)

	key = cv2.waitKey()
	if key== ord("n"):
		cv2.destroyAllWindows()

	#Laplace Pyramid
	img = cv2.imread(imgName, 1)

	for k in range(level):

		src=cv2.sepFilter2D(img, -1, kernel, kernel)
		
		dst=img-src

		new_ImgName = 'Laplace level '+str(k)
		cv2.imshow(new_ImgName, dst)
		img=src

	key = cv2.waitKey()
	if key== ord("n"):
		cv2.destroyAllWindows()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
