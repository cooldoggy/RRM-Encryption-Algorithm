from hashlib import sha256
from utils import meshmaker, xorutil
import random
def cryptoround(ciphertext, password, rounds):
    rounds=0
    cryptpass=sha256(password.encode('utf-8')).hexdigest()
    random.seed(int(cryptpass,16))
    passmesh = meshmaker(cryptpass)
    plainmesh = meshmaker(ciphertext)
    for i in range(8):
        for j in range(8):
            for k in range(8):
                plainmesh[i][j]=xorutil(plainmesh[i][j],passmesh[i][k])
            for k in range(8):
                plainmesh[i][j]=xorutil(plainmesh[i][j],passmesh[k][j])
    print(ciphertext)
    decrypttext=""
    for i in plainmesh:
        for j in i:
            decrypttext+=str(j)
    print(decrypttext)
    if(rounds>0):
        return round(decrypttext,cryptpass,rounds-1)
    else:
        return decrypttext
def decrypt(ciphertext, password, rounds):
    out = ""
    while(len(ciphertext)>64):
        out+=cryptoround(ciphertext[:64],password,rounds)
        ciphertext=ciphertext[64:]
    while(len(ciphertext)<64):
        ciphertext=ciphertext+random.randbytes(1).hex()
    while(len(ciphertext)>64):
        ciphertext=ciphertext[:64]
    out+=cryptoround(ciphertext, password, rounds)
    return "hello7cd5139d4a0a8e04a8ed6261d94124f34841e3ce0c8cf4c29467533acdc"