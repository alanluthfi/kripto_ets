import socket
from PIL import Image
from numpy import imag
import pickle
import io


def decryptRSA(ma):
    key = "77,221" # input("Input public key:")
    d, N = int(key.split(",")[0]), int(key.split(",")[1])
    m = ma
    decrypted = [(c**d % N) for c in m]
    return tuple(decrypted)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
server.bind(('localhost', 1002))  # 127.0.0.1
server.listen()

client_socket, client_address = server.accept()

file = open("server_image.png", "wb")
image_chunk = client_socket.recv(2048)  # stream-based protocol

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)

file.close()

image = Image.open("server_image.png")
pixels2 = list(image.getdata())
width, height = image.size
pixels2 = [pixels2[i * width:(i + 1) * width] for i in range(height)]

pixels_out2 = []
for row in pixels2:
    for tup3 in row:
        pixels_out2.append(decryptRSA(tup3))

image_out2 = Image.new(image.mode,image.size)
image_out2.putdata(pixels_out2)
image_out2.save('test_outDec.png')


client_socket.close()