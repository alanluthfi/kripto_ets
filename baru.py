from PIL import Image, ImageOps
import numpy as np
import cv2
from PIL import Image

def keyRSA (pa, qa):
    # pick 2 prime number (p, q)
    p = pa #int(input("Input prime number 1: "))
    q = qa #int(input("Input prime number 2: "))

    N = p * q  # mod key
    eu = (p-1) * (q-1)  # euler
    print("N = {}, eu = {}".format(N, eu))

    # choose e (encryption key)
    e = 0
    factorN = set([i if N % i == 0 else 1 for i in range(2, N+1)])
    factoreu = set([i if eu % i == 0 else 1 for i in range(2, eu+1)])

    for e in range(2, eu):
      c = set([i if e % i == 0 else 1 for i in range(2, e+1)])
      if c.intersection(factorN) == {1} and c.intersection(factoreu) == {1}:
        break
    print("Public key: ({}, {})".format(e, N))

    # choose d (decryption key)
    for d in range(1, 9999):
        if (e * d) % eu == 1:
            break
    print("Private key: ({}, {})".format(d, N))

def encryptRSA(ma):
    key = "7, 2867" # input("Input public key:")
    e, N = int(key.split(",")[0]), int(key.split(",")[1])
    m = ma #"""hallo lan. look at this, more more more more.
    #testing a new line.""" # input("Input message: ")

    # plainText = [ord(i) for i in m]
    block = 4
    # encrypted = ["{}".format(c**e % N).zfill(block) for c in plainText]
    encrypted = ["{}".format(c**e % N).zfill(block) for c in m]
    # encrypted = "".join([c for c in encrypted])
    return tuple(encrypted)

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




# list pixel (a, b, c, d) -> mbuh berapa
            #(e, f, g, h)
"""
    for row in pixel:
        for tup in row: (a, b, c, d)
            pixel_out(encryptRSA(tup))
"""