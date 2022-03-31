from PIL import Image, ImageOps
import numpy as np
import cv2
from PIL import Image
image = Image.open("tugas.png")
pixels = list(image.getdata())
width, height = image.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

# print(pixels)

pixels_out = []
for row in pixels:
    for tup in row:
        pixels_out.append(tup)
    
image_out = Image.new(image.mode,image.size)
image_out.putdata(pixels_out)

image_out.save('test_out.png')
