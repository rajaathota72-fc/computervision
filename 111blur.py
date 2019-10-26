#blurring of image
import cv2
import numpy as np
image1 = cv2.imread("/Users/rajaathota72/Desktop/1-500x250-3.jpg")
kernel_3x3=np.ones((3,3),np.float32)/9
blur1=cv2.filter2D(image1,-1,kernel_3x3)
cv2.imshow("blur1",blur1)
cv2.waitKey(5000)
kernel_7x7=np.ones((7,7),np.float32)/49
blur2=cv2.filter2D(image1,-1,kernel_7x7)
cv2.imshow("blur2",blur2)
cv2.waitKey(5000)
denoising = cv2.fastNlMeansDenoisingColored(image1,None,6,6,7,21)
cv2.imshow("denoised_image",denoising)
cv2.waitKey(7000)
cv2.destroyAllWindows()