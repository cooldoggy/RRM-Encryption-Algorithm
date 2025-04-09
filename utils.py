def meshmaker(inputstring):
    return [list(inputstring[i*8:(i+1)*8]) for i in range(8)]

def xorutil(a, b):
    return a ^ b
def generate_inverse_sbox(encrypt_table):
    # Initialize a 10x10 decryption table with placeholders
    decrypt_table = [[None for _ in range(10)] for _ in range(10)]
    
    # Populate the decryption table using the encryption table
    for a in range(10):
        for b in range(10):
            encrypted_value = encrypt_table[a][b]
            x = int(encrypted_value[0])  # First digit of the encrypted value
            y = int(encrypted_value[1])  # Second digit of the encrypted value
            
            # Ensure the slot is empty (no duplicates)
            if decrypt_table[x][y] is not None:
                raise ValueError(f"Conflict at decrypt_table[{x}][{y}]")
            decrypt_table[x][y] = f"{a:01d}{b:01d}"
    
    # Check for missing entries (incomplete inverse)
    for x in range(10):
        for y in range(10):
            if decrypt_table[x][y] is None:
                raise ValueError(f"Missing entry at decrypt_table[{x}][{y}]")
    
    return decrypt_table
def substitutionboxencrypt(a, b):
    encrypttable = [
        ["97", "96", "42", "20", "36", "78", "16", "63", "11", "08"],
        ["13", "30", "68", "09", "95", "89", "05", "99", "65", "35"],
        ["01", "44", "72", "46", "04", "71", "02", "22", "29", "90"],
        ["61", "81", "62", "21", "34", "32", "73", "53", "45", "80"],
        ["98", "49", "93", "41", "60", "64", "70", "47", "40", "69"],
        ["87", "54", "24", "84", "18", "77", "66", "26", "38", "85"],
        ["59", "43", "48", "91", "92", "00", "14", "58", "03", "75"],
        ["28", "67", "17", "15", "83", "12", "94", "23", "39", "86"],
        ["52", "27", "37", "88", "82", "51", "06", "55", "10", "33"],
        ["57", "07", "76", "50", "56", "31", "25", "74", "19", "79"]
    ]
    #decrypt_table = generate_inverse_sbox(encrypttable)
    #print(decrypt_table)
    return encrypttable[a][b]
def substitutionboxdecrypt(a,b):
    decrypttable = [
    ['65', '20', '26', '68', '24', '16', '86', '91', '09', '13'], 
    ['88', '08', '75', '10', '66', '73', '06', '72', '54', '98'], 
    ['03', '33', '27', '77', '52', '96', '57', '81', '70', '28'], 
    ['11', '95', '35', '89', '34', '19', '04', '82', '58', '78'], 
    ['48', '43', '02', '61', '21', '38', '23', '47', '62', '41'], 
    ['93', '85', '80', '37', '51', '87', '94', '90', '67', '60'], 
    ['44', '30', '32', '07', '45', '18', '56', '71', '12', '49'], 
    ['46', '25', '22', '36', '97', '69', '92', '55', '05', '99'], 
    ['39', '31', '84', '74', '53', '59', '79', '50', '83', '15'], 
    ['29', '63', '64', '42', '76', '14', '01', '00', '40', '17']
    ]
    return decrypttable[a][b]


def esbox(inputstring):
    temp = ""
    out = ""
    for i in inputstring:
        temp += i
        if len(temp) == 2:
            a = int(temp[0], 16) % 10
            b = int(temp[1], 16) % 10
            out += substitutionboxencrypt(a, b)
            temp = ""
    return out


def dsbox(inputstring):
    temp = ""
    out = ""
    for i in inputstring:
        temp += i
        if len(temp) == 2:
            a = int(temp[0], 16) % 10
            b = int(temp[1], 16) % 10
            out += substitutionboxdecrypt(a, b)
            temp = ""
    return out

for i in range(10):
    for j in range(10):
        #print(substitutionboxencrypt(i,j))
        p=substitutionboxencrypt(i,j)
        print(substitutionboxdecrypt(int(p[0]),int(p[1])))