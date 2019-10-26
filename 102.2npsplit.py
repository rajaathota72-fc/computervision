# Color distributions in image
import cv2
from matplotlib import pyplot as plt
image=cv2.imread('/Users/rajaathota72/Desktop/Charlotteville-Trinidad-Tobago.jpg.image.750.563.low.jpg')
histogram=cv2.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),256,[0,256]);plt.show()
cv2.waitKey(2000)
color=('b','g','r')
for i,col in enumerate(color):
    histogram2=cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2,color=col)
    plt.xlim([0,256])
plt.show()
cv2.destroyAllWindows()

