from hashlib import sha256
from utils import meshmaker, xorutil, dsbox
import random

def xordecrypt(ciphertext, password):
    # Create the mesh matrices for password and ciphertext
    passmesh = meshmaker(password)
    ciphermesh = meshmaker(ciphertext)
    
    # Iterate through the 8x8 grid and reverse the XOR operations
    for i in range(8):
        for j in range(8):
            # Convert the hex character into an integer
            ciphermesh[i][j] = int(ciphermesh[i][j], 16)
            
            # Reverse Part 1: XOR with passmesh row
            for k in range(8):
                ciphermesh[i][j] = xorutil(ciphermesh[i][j], int(passmesh[i][k], 16))
            
            # Reverse Part 2: XOR with passmesh column
            for k in range(8):
                ciphermesh[i][j] = xorutil(ciphermesh[i][j], int(passmesh[k][j], 16))
            
            # Convert back to a single hex character
            ciphermesh[i][j] = format(ciphermesh[i][j], 'x')
    
    # Convert the 8x8 grid back into a string
    out = ''.join([''.join(row) for row in ciphermesh])
    return out

def decryptround(ciphertext, password, rounds):
    
    # Reverse substitution first
    out = dsbox(ciphertext)
    out=xordecrypt(out,password)
    if rounds > 0:
        return decrypt(out, password, rounds - 1, initial=False)
    else:
        return out

def decrypt(ciphertext, password, rounds, initial=True):
    cryptpass = sha256(password.encode('utf-8')).hexdigest()
    # Process blocks
    random.seed(int(cryptpass, 16))
    out = ""
    # Split into 64-character blocks
    while len(ciphertext) >= 64:
        block = ciphertext[:64]
        decrypted_block = decryptround(block, cryptpass, rounds)
        out += decrypted_block
        ciphertext = ciphertext[64:]
    # Remove padding (assuming original was hex-encoded)
    if initial:
        out = bytes.fromhex(out).decode('utf-8', errors='ignore').rstrip('\x00')
    return out

print(decrypt("8793645532634905727850857393987278690825630938547919846076022413","Printme",5))