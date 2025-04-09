from hashlib import sha256
from utils import xorencrypt, esbox
import random

def cryptoround(plaintext, initial_key, rounds):
    current_key = initial_key
    out = plaintext
    for _ in range(rounds):
        out = xorencrypt(out, current_key)
        out = esbox(out, current_key)
        # Derive next key using SHA-256
        current_key = sha256(current_key.encode('utf-8')).hexdigest()
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
    out = ""
    # Split into 64-character blocks (32 bytes)
    while len(plaintext) >= 64:
        block = plaintext[:64]
        encrypted_block = cryptoround(block, cryptpass, rounds)
        out += encrypted_block
        plaintext = plaintext[64:]
    # Pad remaining block if needed
    if len(plaintext) > 0:
        remaining_bytes = bytes.fromhex(plaintext)
        pad_len = 32 - len(remaining_bytes)
        padded_bytes = remaining_bytes + bytes([pad_len] * pad_len)
        padded_hex = padded_bytes.hex()
        encrypted_block = cryptoround(padded_hex, cryptpass, rounds)
        out += encrypted_block
    return out