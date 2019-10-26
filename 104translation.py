#Translation of images in plane
import cv2
import numpy as np
image = cv2.imread("/Users/rajaathota72/Desktop/Charlotteville-Trinidad-Tobago.jpg.image.750.563.low.jpg")
height,width = image.shape[:2]
quarter_height,quarter_width=height/4,width/4
T=np.float32([[1,0,quarter_width],[0,1,quarter_height]])
image_translation=cv2.warpAffine(image,T,(width,height))
cv2.imshow("translated_image",image_translation)
cv2.waitKey(5000)
cv2.destroyAllWindows()