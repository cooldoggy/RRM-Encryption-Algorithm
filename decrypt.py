from hashlib import sha256
from utils import meshmaker, xorutil, dsbox
import random

def decryptround(ciphertext, password, rounds):
    passmesh = meshmaker(password)
    # Reverse substitution first
    out = dsbox(ciphertext)
    plainmesh = meshmaker(out)
    for i in range(8):
        for j in range(8):
            plainmesh[i][j] = int(plainmesh[i][j], 16)
            # Reverse XOR order: columns first, then rows
            for k in range(8):
                plainmesh[i][j] = xorutil(plainmesh[i][j], int(passmesh[k][j], 16))
            for k in range(8):
                plainmesh[i][j] = xorutil(plainmesh[i][j], int(passmesh[i][k], 16))
            plainmesh[i][j] = format(plainmesh[i][j], 'x')
    # Convert mesh back to string
    out = ''.join([''.join(row) for row in plainmesh])
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