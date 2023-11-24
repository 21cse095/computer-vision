import cv2
image = cv2.imread("C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot_20221116_214743.png")
if image is None:
    print('Error reading image')
else:
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
