#cropping an image
import cv2
image = cv2.imread("/Users/rajaathota72/Desktop/Charlotteville-Trinidad-Tobago.jpg.image.750.563.low.jpg")
height,width= image.shape[:2]
start_row,start_col=int(height*0.25),int(width*0.25)
end_row,end_col=int(height*0.75),int(width*0.75)
cropped=image[start_row:end_row,start_col:end_col]
cv2.imshow("original image",image)
cv2.waitKey(6000)
cv2.imshow('cropped',cropped)
cv2.waitKey(6000)
cv2.destroyAllWindows()