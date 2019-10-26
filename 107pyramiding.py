#Pyradiming as alternate for resizing
import cv2
image = cv2.imread("/Users/rajaathota72/Desktop/Charlotteville-Trinidad-Tobago.jpg.image.750.563.low.jpg")
smaller=cv2.pyrDown(image)
larger=cv2.pyrUp(smaller)
cv2.imshow('orginal',image)
cv2.imshow('smaller',smaller)
cv2.imshow('larger',larger)
cv2.waitKey(1000)
cv2.destroyAllWindows()