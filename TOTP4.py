import hmac, base64, struct, hashlib, time, array

def Truncate(hmac_sha1):
    """
    Truncate represents the function that converts an HMAC-SHA-1
    value into an HOTP value as defined in Section 5.3.

    http://tools.ietf.org/html/rfc4226#section-5.3

    """
    offset = int(hmac_sha1[-1], 16)
    binary = int(hmac_sha1[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
    return str(binary)

def _long_to_byte_array(long_num):
    """
    helper function to convert a long number into a byte array
    """
    byte_array = array.array('B')
    for i in reversed(range(0, 8)):
        byte_array.insert(0, long_num & 0xff)
        long_num >>= 8
    return byte_array

def HOTP(K, C, digits=10):
    """
    HOTP accepts key K and counter C
    optional digits parameter can control the response length

    returns the OATH integer code with {digits} length
    """
    C_bytes = _long_to_byte_array(C)
    hmac_sha1 = hmac.new(key=K, msg=C_bytes, digestmod=hashlib.sha512).hexdigest()
    print(K)
    print(C_bytes)
    print(hmac_sha1)
    return Truncate(hmac_sha1)[-digits:]

def TOTP(K, digits=10, window=30):
    """
    TOTP is a time-based variant of HOTP.
    It accepts only key K, since the counter is derived from the current time
    optional digits parameter can control the response length
    optional window parameter controls the time window in seconds

    returns the OATH integer code with {digits} length
    """
    C = int(time.time() / window)
    return HOTP(K, C, digits=digits)

K = b"ninja@example.comHDECHALLENGE003"
pw = TOTP(K, 10, 30)
print(pw)
