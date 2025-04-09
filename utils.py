import random
def meshmaker(inputstring):
    return [list(inputstring[i*8:(i+1)*8]) for i in range(8)]

def xorutil(a, b):
    return a ^ b

def xorencrypt(plaintext, password):
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
    out = ''.join([''.join(row) for row in plainmesh])
    return out

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

def generate_dynamic_sbox(cryptpass):
    """Generate a 16x16 key-dependent S-box using cryptpass."""
    # Create a PRNG instance seeded with cryptpass to avoid interfering with global random
    seed = int(cryptpass, 16)  # Convert hex string to integer
    prng = random.Random(seed)
    # Generate shuffled list of all 256 byte values (00 to FF)
    sbox_entries = [format(i, '02x').upper() for i in range(256)]
    prng.shuffle(sbox_entries)
    # Convert to 16x16 grid
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
