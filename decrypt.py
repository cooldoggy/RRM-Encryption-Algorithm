from hashlib import sha256
from utils import xordecrypt, dsbox
import random



def decryptround(ciphertext, password, rounds):
    
    # Reverse substitution first
    out = dsbox(ciphertext,password)
    out=xordecrypt(out,password)
    if rounds > 0:
        return decryptround(out, password, rounds - 1,)
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
    out_bytes = bytes.fromhex(out)
    if out_bytes:
        pad_len = out_bytes[-1]
        # Check for padding and remove if it's correct
        if pad_len > 0 and pad_len <= 16 and all(b == pad_len for b in out_bytes[-pad_len:]):
            out_bytes = out_bytes[:-pad_len]
        out_bytes = out_bytes.rstrip(b'\x0b')
    out = out_bytes.decode('utf-8', errors='ignore')


    return out

#print(decrypt("8793645532634905727850857393987278690825630938547919846076022413","Printme",5))