import cv2 as cv
import numpy as np
im = cv.imread("/Users/rajaathota72/Desktop/14641803629337874.jpg")
gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (5, 5), 0)
_, bin = cv.threshold(gray,120,255,1) # inverted threshold (light obj on dark bg)
bin = cv.dilate(bin, None) # fill some holes
bin = cv.dilate(bin, None)
bin = cv.erode(bin, None) # dilate made our shape larger, revert that
bin = cv.erode(bin, None)
contours, hierarchy = cv.findContours(bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
rc = cv.minAreaRect(contours[0])
box = cv.boxPoints(rc)
for p in box:
    pt = (p[0],p[1])
    print(pt)
    cv.circle(im,pt,5,(200,0,0),2)
cv.imshow("plank", im)
cv.waitKey(3000)
point_A=np.float32([[182.5,73.5],[53,607],[619,41],[748.5,170.5]])
point_B=np.float32([[0,0],[420,0],[0,594],[420,594]])
M=cv.getPerspectiveTransform(point_A,point_B)
warped=cv.warpPerspective(im,M,(420,594))
cv.imshow("warped",warped)
cv.waitKey(10000)
cv.destroyAllWindows()