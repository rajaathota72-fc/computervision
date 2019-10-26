#Understanding the concept of Hue, saturation and value in images
import cv2
input = cv2.imread('/Users/rajaathota72/Desktop/UNTIL 2/pitures/001.JPG')
hsv_image=cv2.cvtColor(input,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image',hsv_image)
cv2.waitKey(10000)
cv2.imshow("Hue channel",hsv_image[:,:,0])
cv2.waitKey(10000)
cv2.imshow("Saturation channel",hsv_image[:,:,1])
cv2.waitKey(10000)
cv2.imshow("Value channel",hsv_image[:,:,2])
cv2.waitKey(10000)
cv2.destroyAllWindows()