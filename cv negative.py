import cv2
import numpy as np
from matplotlib import pyplot as plt
def create_negative(image_path):
    img = cv2.imread(image_path)
    img_negative = 255 - img
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img_negative, cv2.COLOR_BGR2RGB))
    plt.title('Negative Image')
    plt.show()
input_image_path = "C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot 2023-09-03 212640.png"
create_negative(input_image_path)
