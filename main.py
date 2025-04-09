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
            tutorial(decrypt("14C8A2963EFD0411AC4389AEE11D90931CC9DA3949D5B674E44692B0CACAE32D35DE910C486D763C7AB53074B6D64E29545DF9EDD779DC8296E11149600575CF", "password", 2048))
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
