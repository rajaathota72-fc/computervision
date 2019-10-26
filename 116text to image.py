import cv2
import numpy as np
image = np.zeros((512,512,3))
cv2.putText(image,"Helloworld",(75,290),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0),5)
cv2.imshow("helloworld",image)
cv2.waitKey(4000)
cv2.destroyAllWindows()