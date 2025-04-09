from hashlib import sha256
from utils import xordecrypt, dsbox
import random

def decryptround(ciphertext, initial_key, rounds):
    # Generate all keys for decryption
    keys = [initial_key]
    for _ in range(rounds - 1):
        keys.append(sha256(keys[-1].encode('utf-8')).hexdigest())
    # Reverse keys to undo encryption steps
    keys = reversed(keys)
    out = ciphertext
    for key in keys:
        out = dsbox(out, key)
        out = xordecrypt(out, key)
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
    # Remove padding
    out_bytes = bytes.fromhex(out)
    if out_bytes:
        pad_len = out_bytes[-1]
        if pad_len > 0 and pad_len <= 16 and all(b == pad_len for b in out_bytes[-pad_len:]):
            out_bytes = out_bytes[:-pad_len]
        out_bytes = out_bytes.rstrip(b'\x0b')
    out = out_bytes.decode('utf-8', errors='ignore')
    return out