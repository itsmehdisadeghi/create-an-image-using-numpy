import cv2
import numpy as np

im = [[[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 255],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 255 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]],
      [[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0],[0 , 0 , 0]]]


img = np.array(im , dtype=float)
cv2.imwrite('E:\higga.jpg' , img)
cv2.imshow("out" , img)
cv2.waitKey(0)