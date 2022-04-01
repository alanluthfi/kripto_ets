import socket
from PIL import Image
import AES, RSA

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
client.connect(('localhost', 1002))  # 127.0.0.1

option = input("Send Image/Text? ")
client.send(option.encode("ascii"))

if option.lower() == "image":
    imagename = input("Input image name: ")
    # image encryption
    image = Image.open(imagename)
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    string_pixels_test = []
    for row in pixels:
        for tup in row:
            string_pixels_test.append(RSA.enc(tup))
    
    string_pixels_test.append(str(image.size[0]).zfill(5))
    string_pixels_test.append(str(image.size[1]).zfill(5))
    string_pixels_test = "".join(string_pixels_test)
    client.send(string_pixels_test.encode('ascii'))
    image.close()

elif option.lower() == "text":
    message = input("message: ").zfill(16)
    encrypted = AES.enc(message)
    print("Sending encrypted message...")
    client.send(encrypted.encode("ascii"))
    print("Message sent.")

else:
    print("Input error!")

client.close()