from hashlib import sha256
from utils import meshmaker, xorutil, esbox
import random

def cryptoround(plaintext, password, rounds):
    passmesh = meshmaker(password)
    plainmesh = meshmaker(plaintext)
    for i in range(8):
        for j in range(8):
            plainmesh[i][j] = int(plainmesh[i][j], 16)
            # Part 1: XOR with passmesh row
            for k in range(8):
                plainmesh[i][j] = xorutil(plainmesh[i][j], int(passmesh[i][k], 16))
            # Part 2: XOR with passmesh column
            for k in range(8):
                plainmesh[i][j] = xorutil(plainmesh[i][j], int(passmesh[k][j], 16))
            # Convert back to single hex character
            plainmesh[i][j] = format(plainmesh[i][j], 'x')
    # Convert mesh back to string
    out = ''.join([''.join(row) for row in plainmesh])
    out = esbox(out)
    if rounds > 0:
        new_password = esbox(out)
        return encrypt(out, new_password, rounds - 1, initial=False)
    else:
        return out

def encrypt(plaintext, password, rounds, initial=True):
    cryptpass = sha256(password.encode('utf-8')).hexdigest()
    if initial:
        # Convert plaintext to hex only in the initial call
        plaintext = plaintext.encode().hex()
    # Process blocks
    random.seed(int(cryptpass, 16))
    out = ""
    # Split into 64-character blocks (32 bytes)
    while len(plaintext) >= 64:
        block = plaintext[:64]
        encrypted_block = cryptoround(block, cryptpass, rounds)
        out += encrypted_block
        plaintext = plaintext[64:]
    # Pad remaining block if needed
    if len(plaintext) > 0:
        padding_length = 64 - len(plaintext)
        padding = random.randbytes(padding_length).hex()
        plaintext += padding
        plaintext = plaintext[:64]
        encrypted_block = cryptoround(plaintext, cryptpass, rounds)
        out += encrypted_block
    return out

# Example usage
print(encrypt("hello", "Printme", 5))