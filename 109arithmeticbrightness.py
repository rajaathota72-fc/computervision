#Arithmetic operations on images
import cv2
import numpy as np
image1 = cv2.imread("/Users/rajaathota72/Desktop/1-500x250-3.jpg")
image2=cv2.imread("/Users/rajaathota72/Desktop/2-500x250-2.jpg")
m=np.ones(image1.shape,dtype="uint8")
added=cv2.add(image1,image2)
cv2.imshow("add",added)
cv2.waitKey(4000)
subtract=cv2.subtract(image1,image2)
cv2.imshow("subtract",subtract)
cv2.waitKey(4000)
add_weighted=cv2.addWeighted(image1,0.5,image2,0.4,0)
cv2.imshow("addweight",add_weighted)
cv2.waitKey(4000)
added1=cv2.add(image1,m)
cv2.imshow("add",added1)
cv2.waitKey(4000)
cv2.destroyAllWindows()