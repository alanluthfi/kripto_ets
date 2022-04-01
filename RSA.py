import numpy as np


# pick 2 prime number (p, q)
p = 7
q = 37

N = p * q  # mod key
eu = (p-1) * (q-1)  # euler

# choose e (encryption key)
e = 0
factorN = set([i if N % i == 0 else 1 for i in range(2, N+1)])
factoreu = set([i if eu % i == 0 else 1 for i in range(2, eu+1)])

for e in range(2, eu):
  c = set([i if e % i == 0 else 1 for i in range(2, e+1)])
  if c.intersection(factorN) == {1} and c.intersection(factoreu) == {1}:
    break

# choose d (decryption key)
for d in range(1, 9999):
  if (e * d) % eu == 1:
    break

def enc(m):
    encrypted = [((c**e) % N) for c in m]
    block = 4
    string_encrypted = ["{}".format(c**e % N).zfill(block) for c in m]
    string_encrypted = "".join([c for c in string_encrypted])
    return tuple(encrypted), string_encrypted

def dec(m):
    decrypted = [int(m[i:i+4])**d % N for i in range(0, len(m), 4)]
    decrypted = np.array(decrypted).reshape(int(len(decrypted)/4), 4)
    return [tuple(i) for i in decrypted]