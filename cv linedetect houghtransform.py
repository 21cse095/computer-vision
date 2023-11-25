import cv2
import numpy as np
image = cv2.imread("C:\\Users\\Lenovo\\Desktop\\chessboard.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
canny_edges = cv2.Canny(blurred, 75, 150)
detect_lines = cv2.HoughLinesP(canny_edges, 1, np.pi / 180, 60, maxLineGap=30)
for line in detect_lines:
    x0, y0, x1, y1 = line[0]
    cv2.line(image, (x0, y0), (x1, y1), (0, 0, 255), 1)
cv2.imshow("linedetection.png", image)
