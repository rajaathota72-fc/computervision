#Resizing the image
import cv2
image = cv2.imread("/Users/rajaathota72/Desktop/Charlotteville-Trinidad-Tobago.jpg.image.750.563.low.jpg")
image_resized=cv2.resize(image,None,fx=0.75,fy=0.75)
cv2.imshow("resized_image",image_resized)
cv2.waitKey(4000)
image_resized1=cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("cubic interpolated image",image_resized1)
cv2.waitKey(4000)
image_resized2=cv2.resize(image,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow("interpolated image",image_resized2)
cv2.waitKey(4000)
cv2.destroyAllWindows()