import socket
from PIL import Image

def decryptRSA():
    key = "1183, 2867" # input("Input public key:")
    d, N = int(key.split(",")[0]), int(key.split(",")[1])
    m = encrypted
    block = 4
    decrypted = [int(m[i:i+block])**d % N for i in range(0, len(m), block)]
    for c in decrypted:
        if c == 10:
            print()
    else:
        print(chr(c), end="")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
server.bind(('localhost', 1002))  # 127.0.0.1
server.listen()

client_socket, client_address = server.accept()

#file = open('server_image.jpg', "wb")
image_chunk = client_socket.recv(2048)  # stream-based protocol

while image_chunk:
    decryptRSA(image_chunk)
    pixels_out = []
    for row in pixels:
        for tup in row:
            pixels_out.append(tup)

image_out = Image.new(Image.mode,Image.size)
image_out.putdata(pixels_out)

image_out.save('test_out.png')

#img.close()
client_socket.close()