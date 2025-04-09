import hashlib
import sys
from encrypt import encrypt
from decrypt import decrypt
from utils import tutorial
sys.setrecursionlimit(4096)
#plaintext matrix
#SHA-256 sum on the password to make it 64 characters to put into a matrix
def main():
    try:
        if(sys.argv[1] == "-r"):
            tutorial(decrypt("E7E27CC72FCB3645179D2756EBBF6694249A46F6210C509AF7D6DCA49533EA823CF0DBC56BF808DD87AC71B7A3B4D7049791F9759A6E985F78442CBB4268C377", "password", 2048))
    except:
        pass
    rounds = 2048
    if(len(sys.argv)<5):
        print("Not enough arguments\n"
            "Usage:\t main.py -e [8 char plaintext] [password] [Encryption Rounds]\n"
            "\t main.py -d [ciphertext] [8 char key] [Encryption Rounds]\nUse -r to use the defaults.\n")
        return
    if(len(sys.argv[3])<1):
        print("Please enter a password.\n")
        return
    try:
        rounds = int(sys.argv[4])
    except:
        print("Please specify the number of encryption rounds.\n")
    if(sys.argv[1]=="-e"):
        encrypted = encrypt(str(sys.argv[2]), str(sys.argv[3]), rounds)
        print(encrypted)
        return
    elif(sys.argv[1]=="-d"):
        decrypted = decrypt(str(sys.argv[2]), str(sys.argv[3]), rounds)
        print(decrypted)
        return
    else:
        print("Invalid flag. Use -r for a tutorial.")
        
main()
