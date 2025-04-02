from hashlib import sha256
import random
def encrypt(plaintext, password, rounds):
    cryptpass=sha256(password.encode('utf-8')).hexdigest()
    random.seed(int(cryptpass,16))
    out=""
    passmesh = [[cryptpass[:8]],
                [cryptpass[8:16]],
                [cryptpass[16:24]],
                [cryptpass[24:32]],
                [cryptpass[32:40]],
                [cryptpass[40:48]],
                [cryptpass[48:56]],
                [cryptpass[56:]],]
    while(len(plaintext)>64):
        out+=encrypt(plaintext[:64],password,rounds)
        plaintext=plaintext[64:]
    while(len(plaintext)<64):
        plaintext=plaintext+random.randbytes(1).hex()
    while(len(plaintext)>64):
        plaintext=plaintext[:64]
    plainmesh = [[plaintext[:8]],
                [plaintext[8:16]],
                [plaintext[16:24]],
                [plaintext[24:32]],
                [plaintext[32:40]],
                [plaintext[40:48]],
                [plaintext[48:56]],
                [plaintext[56:]],]
    for i in range(8):
        for j in range(8):
            print(plaintext[i,j])
            #loop through plaintext and xor with row then column of passmesh
            
    return "hello7cd5139d4a0a8e04a8ed6261d94124f34841e3ce0c8cf4c29467533acdc"

    

encrypt("hello","Printme",5)

