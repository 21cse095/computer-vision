import cv2
import numpy as np
def enhance_brightness(image,alpha=1.5,beta=30):
    enhanced_image=cv2.convertScaleAbs(image,alpha=alpha,beta=beta)
    return enhanced_image
input_image=cv2.imread("C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot 2023-11-05 221141.png")
brightened_image=enhance_brightness(input_image)
cv2.imshow("original image",input_image)
cv2.imshow("brightened image",brightened_image)


