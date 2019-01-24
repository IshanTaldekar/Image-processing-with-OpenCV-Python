import numpy as np
import math
import cv2


#Write
#Use HSV color space for object detection

class shape_recognition():
    def __init__(self, img):
        self.img = img

    def pre_prossessing(self):
        lower = np.array([0, 0, 0], dtype=np.uint8)
        upper = np.array([15, 15, 15], dtype=np.uint8)
        mask = cv2.inRange(self.img, lower, upper)
        cv2.imshow("mask", mask)

        (flags, contours, h) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        return contours



img = cv2.imread("test_shapes.jpg")
obj1 = shape_recognition(img)
contours = shape_recognition.pre_prossessing(obj1)

cv2.imshow("Image", img)
keystroke = cv2.waitKey(0)

if keystroke == 27:
    cv2.destroyAllWindows()
if keystroke == ord('s'):
    cv2.imwrite('shape_detection_output.png', img)
