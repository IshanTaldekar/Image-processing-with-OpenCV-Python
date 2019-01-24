import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test_image.jpg')

kernel_2dconv = np.ones((5, 5), np.float32)/25
output_2dconv = cv2.filter2D(img, -1, kernel_2dconv)

cv2.imshow('output', output_2dconv)
cv2.waitKey(0)
cv2.destroyAllWindows()
