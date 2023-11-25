import cv2
image = cv2.imread("C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot_20221116_214743.png")
kernel_size = (5, 5)  
blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
cv2.imshow("original image" ,image)
cv2.imshow("blurred image" ,blurred_image)
