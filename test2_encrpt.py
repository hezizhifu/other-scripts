#!/usr/bin/env python
#-*-coding:utf-8 -*-
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
 
def encrypt(key, source, encode=True):
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = Random.new().read(AES.block_size)  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode("latin-1") if encode else data
if __name__=='__main__':
	my_password = b"secret_AES_key_string_to_encrypt/decrypt_with"
	my_data = b"input_string_to_encrypt/decrypt"
 
	print("key:  {}".format(my_password))
	print("data: {}".format(my_data))
	encrypted = encrypt(my_password, my_data)
