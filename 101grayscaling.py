# Gray scaling of images ,Saving the images in different formats
#ref:
import cv2
import numpy as np
input = cv2.imread('/Users/rajaathota72/Desktop/UNTIL 2/pitures/001.JPG') # for reading the image
cv2.imshow("firstpicture",input) # shows the image in the output
cv2.waitKey(1000)
grey_image=cv2.cvtColor(input,cv2.COLOR_BGR2GRAY) # converts color to greyscale
cv2.imshow('Grayscale',grey_image) # shows the greyscale image
cv2.waitKey(1000)
height=np.size(input,0) # height of the image
width=np.size(input,1) #width of the image
print(height)
print(width)
x=cv2.imwrite('firstpic.jpg',input) #writing the edited image to system in jpg format
y=cv2.imwrite('firstpic.png',input) #writing the edited image to system in png format
print(y)
print(x)
B,G,R = input[10][90]
print(B,G,R)
print(grey_image.shape)
print(grey_image[10][98])
cv2.destroyAllWindows()
