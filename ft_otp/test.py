import hmac
import base64
import time
import datetime

key = b'password'
secret = base64.b32encode(key)
counter = 0
time_timer = 10


def Dynamic_Truncation(hmac_res):
    offset = hmac_res[-1] & 0b00001111 #work as well: 0b1111 0xF 15
    bin_code = (
        (hmac_res[offset] & 0x7f) << 24
        | (hmac_res[offset + 1] & 0xff) << 16
        | (hmac_res[offset + 2] & 0xff) << 8
        | (hmac_res[offset + 3] & 0xff)
    )
    return bin_code


def hotp(key, counter_value):
    counter_bytes = counter_value.to_bytes(8, byteorder="big")
    hs_hmac = hmac.new(key, counter_bytes, "sha1")
    hmac_res = hs_hmac.digest()
    num = Dynamic_Truncation(hmac_res)
    print(bin(num))
    return num % 10 ** 6

def totp(key, time_value):
    time_now = datetime.datetime.now()
    seconds_since_epoch = time.mktime(time_now.timetuple())
    time_steps = int(seconds_since_epoch / time_value)
    otp = hotp(key=key, counter_value=time_steps)
    return otp

print(totp(secret, time_timer))
# print(hotp(secret, counter))
