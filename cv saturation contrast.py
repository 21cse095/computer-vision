import cv2
img = cv2.imread("C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot 2023-09-03 212640.png")
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_contrast = cv2.equalizeHist(img_grayscale)
img_contrast_color = cv2.cvtColor(img_contrast, cv2.COLOR_GRAY2BGR)
saturated_factor = 1.5  
img_saturated = cv2.convertScaleAbs(img_contrast_color, alpha=saturated_factor, beta=0)
cv2.imshow("Saturated Image", img_saturated)


