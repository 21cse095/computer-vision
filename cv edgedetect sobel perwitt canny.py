import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread("C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot (1).png", cv2.IMREAD_GRAYSCALE)

# Sobel edge detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = np.sqrt(sobel_x**2 + sobel_y**2)

# Canny edge detection
canny_edges = cv2.Canny(image, 50, 150)

# Prewitt edge detection
kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
prewitt_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
prewitt_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)
prewitt_edges = np.sqrt(prewitt_x**2 + prewitt_y**2)

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(231), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(232), plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(233), plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.subplot(234), plt.imshow(sobel_edges, cmap='gray')
plt.title('Sobel Edges'), plt.xticks([]), plt.yticks([])

plt.subplot(235), plt.imshow(canny_edges, cmap='gray')
plt.title('Canny Edges'), plt.xticks([]), plt.yticks([])

plt.subplot(236), plt.imshow(prewitt_edges, cmap='gray')
plt.title('Prewitt Edges'), plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
