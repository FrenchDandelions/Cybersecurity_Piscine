import hmac
import base64

key = b'password'
secret = base64.b32encode(key)
counter = 0
# byteorder = endian
counter_bytes = counter.to_bytes(8, byteorder="big")
hs_hmac = hmac.new(secret, counter_bytes, "sha1")
print(hs_hmac.digest())


def low_order_4_bits(n):
    return n & 0xF


def last_31_bits(p):
    return (
        (p[0] )
    )


def Dynamic_Truncation(hmac_hash):
    offset = low_order_4_bits(hmac_hash[19])
    p = hmac_hash[offset:offset+4]
    return last_31_bits(p)
# def htop(key, counter_value):
    # return truncate(hmac_sha_11(key, counter_value))
