import socket
from PIL import Image
from numpy import imag
import pickle
import io
# from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True

def decryptRSA(ma):
    key = "77,221" # input("Input public key:")
    d, N = int(key.split(",")[0]), int(key.split(",")[1])
    m = ma
    #block = 4
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
#img.close()

#image = Image.open("tugasdec.png")
#pixels = list(image_chunk.getdata())

# pixels_out = []
# for row in pixels:
#     for tup in row:
#         pixels_out.append(tup)
# image2 = Image.frombytes('RGBA', (128,128), image_chunk, 'raw')
# pixels = list(image2.getdata())
# # width, height = image2.size
# # pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

# pixels_out = []
# for row in pixels:
#     for tup2 in row:
#         pixels_out.append(tup2)

# image_out = Image.new(image2.mode,image2.size)
# image_out.putdata(pixels_out)
# image_out.save('test_out.png')

# for row in pixels:
#     for tup in row:
#         decryptRSA(tup)




# pixels_out = []
# for row in pixels:
#     for tup in row:
#         pixels_out.append(tup)