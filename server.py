import socket
from PIL import Image
import numpy as np

import AES, RSA

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
server.bind(('localhost', 1002))  # 127.0.0.1
server.listen()

client_socket, client_address = server.accept()

option = client_socket.recv(2048).decode('ascii')
if option.lower() == "image":
    print("Receiving encrypted image...")
    encrypted_string = client_socket.recv(16384000).decode('ascii')
    
    imagename = input("Decrypting image...\nInput image name: ")
    pixels_test = RSA.dec(encrypted_string[:-10])
    # print(pixels_test)
    image_test = Image.new('RGBA',(int(encrypted_string[-10:-5]), int(encrypted_string[-5:])))
    image_test.putdata(pixels_test)
    image_test.save('{}.png'.format(imagename))
    
    print("Image Received.")

    """image = open("rec_encrypted.png", "wb")
    image_chunk = client_socket.recv(2048)

    while image_chunk:
        image.write(image_chunk)
        image_chunk = client_socket.recv(2048)

    image.close()

    encrypted_string = client_socket.recv(2048).decode('ascii')
    imagename = input("Decrypting image...\nInput image name: ")
    image = Image.open("rec_encrypted.png")
    pixels = list(image.getdata())
    width, height = image.size
    pixels_test = RSA.dec(encrypted_string)
    # print(pixels_test)
    image_test = Image.new(image.mode,image.size)
    image_test.putdata(pixels_test)
    image_test.save('{}.png'.format(imagename))
    image.close()
    print("Image Received.")"""

    



elif option.lower() == "text":
    print("Receiving text...")
    message = client_socket.recv(2048).decode('ascii')
    print("encrypted message: ", end="")
    print(message)
    print("decrypted message: ", end="")
    print(AES.dec(message))

client_socket.close()