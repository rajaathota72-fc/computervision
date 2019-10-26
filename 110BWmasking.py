#bitwise masking of images
import cv2
import numpy as np
square=np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-2)
cv2.imshow("Square",square)
cv2.waitKey(7000)
ellipse=np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("ellipse",ellipse)
cv2.waitKey(7000)
And=cv2.bitwise_and(square,ellipse)
cv2.imshow("and",And)
cv2.waitKey(7000)
cv2.destroyAllWindows()