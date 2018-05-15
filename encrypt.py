#!/usr/bin/env python
# -*- coding=utf-8-*-
from base64 import b64decode
import hashlib
from Crypto.Hash import SHA256
from base64 import b64encode
from Crypto.Cipher import AES
BLOCK_SIZE = 16  # Bytes
class AESCipher:
    def __init__(self, key):
        self.key = SHA256.new(key).digest()
    def pad(self, s):
        return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
    def unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]
    def encrypt(self, raw):
        raw = self.pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB,b'0000000000000000')
        return b64encode(cipher.encrypt(raw))
    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB,b'0000000000000000')
        return self.unpad(cipher.decrypt(enc)).decode('utf8')
if __name__ == "__main__":
#    msg = 'lj123'
#    key='9582'
#   aes = AESCipher(key)
#    en = aes.encrypt(msg)
#  print('en:', en)
   

