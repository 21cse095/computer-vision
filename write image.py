import cv2
def write_image(image_path, output_path):
   image = cv2.imread(image_path)
   if image is None:
    print(f"Error: Unable to read the image at {image_path}")
    return
   cv2.imwrite(output_path, image)
   print(f"Image successfully written to {output_path}")
input_image_path = "C:\\Users\\Lenovo\\Pictures\\Screenshots\\Screenshot 2023-09-03 212710.png"
output_image_path = "C:\\Users\\Lenovo\\Desktop\\img.jpg.bmp"
write_image(input_image_path, output_image_path)
