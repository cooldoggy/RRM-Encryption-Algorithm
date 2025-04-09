from encrypt import xorencrypt
from decrypt import xordecrypt
from hashlib import sha256
from utils import esbox, dsbox
plaintext="1234567812345678123456781234567812345678123456781234567812345678"
password= sha256("password".encode('utf-8')).hexdigest()
encrypted=xorencrypt(plaintext,password)
print(encrypted)
decrypted=xordecrypt(encrypted,password)
print(decrypted)

sencrypted=esbox(plaintext)
print(sencrypted)
sdecrypted=dsbox(sencrypted)
print(sdecrypted)