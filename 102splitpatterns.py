#Splitting colour patterns in an image
import cv2
input = cv2.imread('/Users/rajaathota72/Desktop/UNTIL 2/pitures/001.JPG')
B,G,R=cv2.split(input)
cv2.imshow("Blue",B)
cv2.waitKey(1000)
cv2.imshow("Green",G)
cv2.waitKey(1000)
cv2.imshow("Red",R)
cv2.waitKey(1000)
merged=cv2.merge([B,G,R])
cv2.imshow("Merged",merged)
cv2.waitKey(5000)
merged=cv2.merge([B+100,G,R])
cv2.imshow("Merged with Blue Amplified",merged)
cv2.waitKey(5000)
cv2.destroyAllWindows()