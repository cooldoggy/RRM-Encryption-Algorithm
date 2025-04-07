from hashlib import sha256
from utils import meshmaker, xorutil
import random

def cryptoround(plaintext, password, rounds):
    rounds=0
    cryptpass=sha256(password.encode('utf-8')).hexdigest()
    random.seed(int(cryptpass,16))
    passmesh = meshmaker(cryptpass)
    plainmesh = meshmaker(plaintext)
    for i in range(8):
        for j in range(8):
            for k in range(8):
                plainmesh[i][j]=xorutil(plainmesh[i][j],passmesh[i][k])
            for k in range(8):
                plainmesh[i][j]=xorutil(plainmesh[i][j],passmesh[k][j])
    print(plaintext)
    crypttext=""
    for i in plainmesh:
        for j in i:
            crypttext+=str(j)
    print(crypttext)
    if(rounds>0):
        return round(crypttext,cryptpass,rounds-1)
    else:
        return crypttext

def encrypt(plaintext, password, rounds):
    out=""
    while(len(plaintext)>64):
        out+=cryptoround(plaintext[:64],password,rounds)
        plaintext=plaintext[64:]
    while(len(plaintext)<64):
        plaintext=plaintext+random.randbytes(1).hex()
    while(len(plaintext)>64):
        plaintext=plaintext[:64]
    out+=cryptoround(plaintext, password, rounds)
    return "hello7cd5139d4a0a8e04a8ed6261d94124f34841e3ce0c8cf4c29467533acdc"

    

encrypt("hello","Printme",5)
