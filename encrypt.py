from hashlib import sha256
from utils import meshmaker, xorutil, esbox
import random

def cryptoround(plaintext, password, rounds):
    passmesh = meshmaker(password)
    plainmesh = meshmaker(plaintext)
    print(plaintext)
    print(password)
    print(plainmesh)
    print(passmesh)
    for i in range(8):
        for j in range(8):
            plainmesh[i][j]=int(plainmesh[i][j],16)
            print(str(i)+"   "+str(j))
            print("part1")
            for k in range(8):
                plainmesh[i][j] = xorutil(plainmesh[i][j], int(passmesh[i][k],16))
            print("part2")
            for k in range(8):
                
                plainmesh[i][j] = xorutil(plainmesh[i][j], int(passmesh[k][j],16))
    # Convert mesh back to string
    out = ''.join([''.join(str(row)) for row in plainmesh])
    out = esbox(out)
    if rounds > 0:
        new_password = esbox(out)
        return encrypt(out, new_password, rounds - 1)
    else:
        return out

def encrypt(plaintext, password, rounds):
    cryptpass = sha256(password.encode('utf-8')).hexdigest()
    print(cryptpass)
    plaintext=str(plaintext.encode().hex())
    print(plaintext)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    random.seed(int(cryptpass, 16))
    out = ""
    # Split into 64-byte blocks
    while len(plaintext) >= 64:
        block = plaintext[:64]
        encrypted_block = cryptoround(block, cryptpass, rounds)
        out += encrypted_block
        plaintext = plaintext[64:]
    # Pad remaining block if needed
    if len(plaintext) > 0:
        padding_length = 64 - len(str(plaintext))
        padding = random.randbytes(padding_length).hex()
        plaintext += padding
        plaintext=plaintext[:64]
        encrypted_block = cryptoround(plaintext, cryptpass, rounds)
        out += encrypted_block
    return out



encrypt("hello", "Printme", 5)