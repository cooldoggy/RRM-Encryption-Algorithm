import hashlib
import sys
from encrypt import encrypt
from decrypt import decrypt
sys.setrecursionlimit(4096)
#plaintext matrix
#SHA-256 sum on the password to make it 64 characters to put into a matrix
def main():
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
    elif(sys.argv[1]=="-r"):
        #rick
        pass
    else:
        print("Invalid flag. Use -r for a tutorial.")
        
main()