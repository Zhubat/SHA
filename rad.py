import pyotp

totp = pyotp.TOTP('base32secret3232')
totp.now() # => '492039'
