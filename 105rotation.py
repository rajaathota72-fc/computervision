#Rotating image
import cv2
import numpy as np
image = cv2.imread("/Users/rajaathota72/Desktop/Charlotteville-Trinidad-Tobago.jpg.image.750.563.low.jpg")
height,width = image.shape[:2]
rotation_matrix=cv2.getRotationMatrix2D((height/2,width/2),45,1)
image_rotation=cv2.warpAffine(image,rotation_matrix,(width,height))
cv2.imshow("rotated_image",image_rotation)
cv2.waitKey(5000)
cv2.destroyAllWindows()