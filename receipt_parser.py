from PIL import Image
import pytesseract
import numpy as np
import cv2
filename = "cfa2.JPG"
file = Image.open(filename)
img = np.array(file)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
img = cv2.threshold(img, 100, 200, cv2.THRESH_TRUNC)[1]
# img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
img = cv2.normalize(img, norm_img, 0, 200, cv2.NORM_MINMAX)
img = cv2.GaussianBlur(img, (1, 1), 0)
kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(img, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)
Image.fromarray(img).save("cfafinalthresholdtrunc100-200.png")
text = pytesseract.image_to_string(img)

print(text)
