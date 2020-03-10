import hmac, base64, struct, hashlib, time

secret = b"fanz@hotmail.com.auHENNGECHALLENGE003"

def get_hotp_token(secret, intervals_no):
    key = secret
    msg = struct.pack(">Q", intervals_no)
    print(msg)
    print(intervals_no)
    print(key)
    h = hmac.new(key, msg, hashlib.sha512)
    h2 = h.hexdigest()
    print(h2)
    h = h.digest()
    o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 10000000000
    return h

def get_totp_token(secret):
    return get_hotp_token(secret, intervals_no=int(time.time())//30)

pw = get_totp_token(secret)
print(pw)
