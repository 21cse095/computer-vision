import cv2
from matplotlib import pyplot as plt
def convert_to_grayscale_and_show(image_path):
    img = cv2.imread(input_image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Grayscale Image')

    plt.show()
input_image_path="C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot 2023-09-03 212640.png"
convert_to_grayscale_and_show(input_image_path)


