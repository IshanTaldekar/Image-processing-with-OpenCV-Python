import numpy as np
import cv2

img = cv2.imread('test_image.jpg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('processed_test_image.jpg', img)
