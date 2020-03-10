    # Mission/Task Description:
    # * For the "password", provide an 10-digit time-based one time password conforming to RFC6238 TOTP.
    # 
    # ** You have to read RFC6238 (and the errata too!) and get a correct one time password by yourself.
    # ** TOTP's "Time Step X" is 30 seconds. "T0" is 0.
    # ** Use HMAC-SHA-512 for the hash function, instead of the default HMAC-SHA-1.
    # ** Token shared secret is the userid followed by ASCII string value "HDECHALLENGE003" (not including double quotations).
    # 
    # *** For example, if the userid is "ninja@example.com", the token shared secret is "ninja@example.comHDECHALLENGE003".
    # *** For example, if the userid is "ninjasamuraisumotorishogun@example.com", the token shared secret is "ninjasamuraisumotorishogun@example.comHDECHALLENGE003"
    # 

import hmac
import hashlib
import time
import sys
import struct
import binascii
import base64


userid = "ninja@example.com"
secret_suffix = "HDECHALLENGE003"
shared_secret = userid + secret_suffix

x = shared_secret.encode()
TX = 30
T0 = 0

dk = hashlib.sha512(x)
print(dk.hexdigest())
y = binascii.hexlify(x)
print(y)
z = y.decode("utf-8")
print(z)
print(len(z))

def HOTP(K, C):
    K_bytes = K.encode()
    ZZ64 = base64.b64encode(K_bytes)
    YK = binascii.hexlify(K_bytes)
    #ZK = YK.decode("utf-8")
    Z64 = base64.b64encode(YK)
    print("%S%S%S")
    print(Z64)
    Z32 = base64.b32encode(YK)
    print(Z32)
    print("%S%S%S")
    B = hex(C)
    print(B)
    B = str(B)
    B = B[2:]
    print(B)
    if(len(B) < 16):
        r = 16-len(B)
        B = '0'*r + B
    print(B)
    print()
    B = bytes.fromhex(B)
    print(B)
    CPP = str(C)
    CPP = CPP.encode()
    C_bytes = struct.pack(">Q", C)
    y = binascii.hexlify(x)
    YP = b'fanz@hotmail.com.auHENNGECHALLENGE003'
    h512 = hashlib.sha512(K_bytes)
    h512.update(C_bytes)
    print(C_bytes)
    print(h512.hexdigest())
    hmac_sha512 = hmac.new(key = YP, msg=B, digestmod=hashlib.sha512).hexdigest()
    print("ASH")
    print(hmac_sha512)
    hmac_sha5122 = hmac.new(key = ZZ64, msg=B, digestmod=hashlib.sha512).hexdigest()
    print(hmac_sha5122)
    return Truncate(hmac_sha512)[-10:]

def Truncate(hmac_sha512):
    """truncate sha512 value"""
    offset = int(hmac_sha512[-1], 16)
    binary = int(hmac_sha512[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
    return str(binary)

def TOTP(K):
    C = int((int(time.time())-T0)/TX)
    print("EMIO")
    print(C)
    return HOTP(K, C)

passwd = TOTP(shared_secret)
print(passwd)
