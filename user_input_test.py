import numpy as np
import cv2

img = cv2.imread('test_image.jpg', 0)

cv2.imshow('image', img)
user_input = cv2.waitKey(0)

if user_input == 27: #wait for esc key to exit
    cv2.destroyAllWindows()
elif user_input == ord('s'):
    cv2.imwrite('processed_test_image.jpg')
    cv2.destroyAllWindows()
    
