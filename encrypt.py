from hashlib import sha256
from utils import xorencrypt, esbox
import random


def cryptoround(plaintext, password, rounds):
    out = xorencrypt(plaintext,password)
    # Convert mesh back to string
    out = esbox(out,password)
    if rounds > 0:
        return cryptoround(out, password, rounds - 1)
    else:
        return out

def encrypt(plaintext, password, rounds, initial=True):
    cryptpass = sha256(password.encode('utf-8')).hexdigest()
    if initial:
        # Add PKCS#7 padding
        plaintext_bytes = plaintext.encode()
        pad_len = 16 - (len(plaintext_bytes) % 16)
        plaintext_bytes += bytes([pad_len] * pad_len)
        plaintext = plaintext_bytes.hex()
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
        # Convert remaining hex chars back to bytes
        remaining_bytes = bytes.fromhex(plaintext)
        pad_len = 32 - len(remaining_bytes)  # 64 hex chars = 32 bytes
        padded_bytes = remaining_bytes + bytes([pad_len] * pad_len)
        padded_hex = padded_bytes.hex()

        encrypted_block = cryptoround(padded_hex, cryptpass, rounds)
        out += encrypted_block

    return out
