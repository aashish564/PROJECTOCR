# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re
import io
import json
import ftfy
'''
image = cv2.imread("sample.jpg")

cv2.imshow("Original", image)
#print(image.shape)
cv2.waitKey(2000)
'''
image = cv2.imread("sample.jpg")

''' Tune the below 3 lines to get the better text incase something is broken in your image'''

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
#gray = cv2.medianBlur(gray, 3)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 61, 93)
text = pytesseract.image_to_string(thresh, config="psm 6")


# write othe grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
cv2.imshow("Original", gray)
#print(image.shape)
cv2.waitKey(2000)

# the temporary file
text = pytesseract.image_to_string(Image.open('D:\\testworkspace\\demo\\test1.jpg', mode='r'))
#os.remove(filename)
print(text)

# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(5000)

# writing extracted data into a text file
text_output = open('outputbase.txt', 'w', encoding='utf-8')
text_output.write(text)
text_output.close()

file = open('outputbase.txt', 'r', encoding='utf-8')
text = file.read()
# print(text)
print(text)
