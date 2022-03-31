#socket_echo_client.py
import random
from PIL import Image
import socket
import time
from Crypto.Cipher import AES
import os


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

# closing will close the file and exit the client program
def closing():
    print('closing socket')
    s.close()
    exit()

def make_nonce(cls):
    """Generate pseudorandom number."""
    return str(random.randint(0, 100000000))

#sending will send a file to the server
def sending():
    #filename = "pdf.pdf"  # File wanting to send
    im = Image.open('tugasKecil.png', 'r')
    pix_val = list(im.getdata())
    pix_val_flat = [x for sets in pix_val for x in sets]    
    #f = open(filename, 'rb')  # Open file
    buf = 4000  # Buffer size

    keyRSA(47,61)
    encryptRSA(pix_val_flat)
    while (True):
        #l = im.read(buf) #read buffer-sized byte section of the file
        l = os.path.getsize('tugasKecil.png') #read buffer-sized byte section of the file
        #if len(l) < 1: closing() #if there is no more of the file to be read, close it and end program

        #cipher = AES.new(key, AES.MODE_EAX) #create cipher object for encryption
        #nonce = make_nonce(pix_val_flat) #generate nonce number
        #pix_val_flat, tag = pix_val_flat.encrypt_and_digest(l) #encrypt f and generate a tag for integrity-checking
        #print('sending {}'.format())
        # concatinate the ciphertext, tag, and nonce separate by uniqueword pattern so that they can be separated on the server
        #pix_val_flat = pix_val_flat + b'uniqueword' + tag + b'uniqueword' + nonce
        time.sleep(.01) #required to send each section error-free
        s.sendto(pix_val_flat.encode(), server_address) #send the ciphertext, tag, and nonce to the server


#receiving will recieve a file from the server
def recieving():
    buf = 4096 #reading buffer size
    filename = b"pdf.pdf"  # File wanting to recieve
    fnew = open('new' + filename.decode('utf-8'), 'wb') #file name for new file

    # concatinate isafile with requested filename so it can be distingueshed as a client-recieving command
    filename = b'isafile' + filename
    print("sending {}".format(filename))
    s.sendto(filename, server_address) #send requested filename to server

    # Create a UDP/IP socket
    r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    new_server_address = (socket.gethostname(), 10100)
    r.bind(new_server_address) #bind the socket to the address
    while (True):
        #if failed, will throw socket.timeout exception and file/socket will be closed/exited
        try:
            while (True):
                r.settimeout(2) #will throw socket.timeout exception when it isn't recieving anymore data
                print('waiting for a connection')

                ciphertext, address = r.recvfrom(buf) #begin recieving file

                ciphertext, ignore, nonce = ciphertext.rpartition(b'uniqueword') #separate nonce from ciphertext variable
                ciphertext, ignore, tag = ciphertext.rpartition(b'uniqueword')   #separate ciphertext and tag from ciphertext variable

                print('received {}'.format(ciphertext))
                # print('received {}'.format(tag))
                cipher = AES.new(key, AES.MODE_EAX, nonce=nonce) #create cipher object for decryption
                plaintext = cipher.decrypt(ciphertext) #decrypt cipher text

                #try to verify message with tag. If its been changed in transit, throw ValueError and close file/socket and exit
                try:
                    cipher.verify(tag) #verify the tag to check integrity
                    print("The message is authentic:", plaintext)
                except ValueError:
                    print("Key incorrect or message corrupted")
                    print('closing')
                    fnew.close()
                    s.close()
                    exit()
                fnew.write(plaintext) #write data to the new file

        except socket.timeout:
            print('closing')
            fnew.close()
            s.close()
            r.close()
            exit()
    exit()


# Create a UDP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (socket.gethostname(), 10000)
# Generate key for AES encryption
key = b'Sixteen byte key'

cors = input("Are you receiving or sending? (r or s)")

#if sending a file, go to sending function, else if receiving a file go to receiving function, else repeat
while True:
    if cors == 'r' or cors == 'R':
        recieving()
    elif cors == 's' or cors == 'S':
        sending()
    else:
        cors = input("Enter r or s (r or s)")









