import socket
from PIL import Image
import pickle

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
    key = "5,221" # input("Input public key:")
    e, N = int(key.split(",")[0]), int(key.split(",")[1])
    m = ma #"""hallo lan. look at this, more more more more.
    #testing a new line.""" # input("Input message: ")

    # plainText = [ord(i) for i in m]
    #block = 4
    # encrypted = ["{}".format(c**e % N).zfill(block) for c in plainText]
    #global encrypted
    encrypted = [(c**e % N) for c in m]
    #print(encrypted)
    # encrypted = "".join([c for c in encrypted])
    return tuple(encrypted)


image = Image.open("tugas.png")
pixels = list(image.getdata())
width, height = image.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
keyRSA(17,13)
pixels_test = []
for row in pixels:
    for tup in row:
        pixels_test.append(encryptRSA(tup))


image_test = Image.new(image.mode,image.size)
image_test.putdata(pixels_test)

image_test.save('test_out_encr.png')

file = open('test_out_encr.png', 'rb')
image_data = file.read(2048)


#res = int.from_bytes(tup, byteorder ='big')

#encryptRSA(pixels)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
client.connect(('localhost', 1002))  # 127.0.0.1

#file = open('tugasKecil.png', 'rb')
#image_data = file.read(2048)

#sup = pickle.dumps(tup)
while image_data:
    #client.send(sup)
    client.send(image_data)
    image_data = file.read(2048)


#file.close()
client.close()





# for row in pixels:
#     for tup in row:
#         encryptRSA(tup)