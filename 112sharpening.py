#Sharpenig of image
import cv2
import numpy as np
image1 = cv2.imread("/Users/rajaathota72/Desktop/1-500x250-3.jpg")
k_sharpening=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
s=cv2.filter2D(image1,-1,k_sharpening)
cv2.imshow("sharpened_image",s)
cv2.waitKey(7000)
cv2.destroyAllWindows()