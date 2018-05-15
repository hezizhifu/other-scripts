#!/usr/bin/env python
#-*-coding:utf8-*-
import encrypt_passwd
passwd='lj123'
key='9700'
aes=encrypt_passwd.AESCipher(key)
en=aes.encrypt(passwd)
print en

