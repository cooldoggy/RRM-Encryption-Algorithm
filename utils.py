
import random
import os
import base64
import sys
import hmac
import hashlib

def meshmaker(inputstring):
    return [list(inputstring[i*8:(i+1)*8]) for i in range(8)]

def generate_dynamic_sbox(cryptpass):
    """Generate a 16x16 key-dependent S-box using cryptpass securely."""
    cryptpass_bytes = bytes.fromhex(cryptpass)
    sbox_entries = [format(i, '02x').upper() for i in range(256)]
    
    # Use HMAC-SHA256 to generate deterministic secure randomness for shuffling
    for i in range(255, 0, -1):
        # Create HMAC using cryptpass as the key and index as the message
        hmac_digest = hmac.new(cryptpass_bytes, i.to_bytes(4, 'big'), hashlib.sha256).digest()
        # Convert digest to an integer and calculate j
        j = int.from_bytes(hmac_digest, 'big') % (i + 1)
        # Swap entries
        sbox_entries[i], sbox_entries[j] = sbox_entries[j], sbox_entries[i]
    
    # Organize into 16x16 grid
    sbox_grid = [sbox_entries[i*16:(i+1)*16] for i in range(16)]
    return sbox_grid

def generate_dynamic_inv_sbox(sbox_grid):
    """Generate the inverse of a dynamic S-box."""
    inv_sbox = [[None for _ in range(16)] for _ in range(16)]
    for a in range(16):
        for b in range(16):
            val = sbox_grid[a][b]
            val_high = int(val[0], 16)
            val_low = int(val[1], 16)
            inv_sbox[val_high][val_low] = f"{a:01x}{b:01x}"
    return inv_sbox

def esbox(inputstring, cryptpass):
    """Encrypt using a key-dependent S-box."""
    sbox = generate_dynamic_sbox(cryptpass)
    out = ""
    for i in range(0, len(inputstring), 2):
        a = int(inputstring[i], 16)
        b = int(inputstring[i+1], 16)
        out += sbox[a][b]
    return out

def dsbox(inputstring, cryptpass):
    """Decrypt using the inverse key-dependent S-box."""
    sbox = generate_dynamic_sbox(cryptpass)
    inv_sbox = generate_dynamic_inv_sbox(sbox)
    out = ""
    for i in range(0, len(inputstring), 2):
        a = int(inputstring[i], 16)
        b = int(inputstring[i+1], 16)
        out += inv_sbox[a][b]
    return out

def tutorial(input):
    link=input
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system("xdg-open " + link)
    elif sys.platform == "darwin":
        os.system("open "+link)
    elif sys.platform == "win32":
        os.system("start "+link)
def xorutil(a, b):
    return a ^ b

def xorencrypt(plaintext, password):
    passmesh = meshmaker(password)
    plainmesh = meshmaker(plaintext)
    # Generate dynamic S-box using the password (cryptpass)
    sbox = generate_dynamic_sbox(password)
    for i in range(8):
        for j in range(8):
            plainmesh[i][j] = int(plainmesh[i][j], 16)
            # Part 1: XOR with S-box substituted passmesh row
            for k in range(8):
                pass_val = passmesh[i][k]  # 1 hex char (4-bit)
                # Expand to a byte (e.g., 'a' -> 'aa') and substitute via S-box
                substituted_byte = sbox[int(pass_val, 16)][int(pass_val, 16)]  # Use S-box lookup
                substituted_value = int(substituted_byte, 16)
                plainmesh[i][j] = xorutil(plainmesh[i][j], substituted_value)
            # Part 2: XOR with S-box substituted passmesh column
            for k in range(8):
                pass_val = passmesh[k][j]
                substituted_byte = sbox[int(pass_val, 16)][int(pass_val, 16)]
                substituted_value = int(substituted_byte, 16)
                plainmesh[i][j] = xorutil(plainmesh[i][j], substituted_value)
            # Ensure value stays within 4-bit range (0-15)
            plainmesh[i][j] = plainmesh[i][j] % 16
            plainmesh[i][j] = format(plainmesh[i][j], 'x')
    out = ''.join([''.join(row) for row in plainmesh])
    return out

def xordecrypt(ciphertext, password):
    passmesh = meshmaker(password)
    ciphermesh = meshmaker(ciphertext)
    sbox = generate_dynamic_sbox(password)
    for i in range(8):
        for j in range(8):
            ciphermesh[i][j] = int(ciphermesh[i][j], 16)
            # Reverse Part 1: XOR with substituted passmesh row (same as encryption)
            for k in range(8):
                pass_val = passmesh[i][k]
                substituted_byte = sbox[int(pass_val, 16)][int(pass_val, 16)]
                substituted_value = int(substituted_byte, 16)
                ciphermesh[i][j] = xorutil(ciphermesh[i][j], substituted_value)
            # Reverse Part 2: XOR with substituted passmesh column
            for k in range(8):
                pass_val = passmesh[k][j]
                substituted_byte = sbox[int(pass_val, 16)][int(pass_val, 16)]
                substituted_value = int(substituted_byte, 16)
                ciphermesh[i][j] = xorutil(ciphermesh[i][j], substituted_value)
            ciphermesh[i][j] = ciphermesh[i][j] % 16
            ciphermesh[i][j] = format(ciphermesh[i][j], 'x')
    out = ''.join([''.join(row) for row in ciphermesh])
    return out
