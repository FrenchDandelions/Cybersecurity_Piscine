import time
import pyotp

# Create a secret key (keep it secret!)̥
# secret_key = pyotp.random_base32()
secret_key = b"OEEJI6QTP45CNFRXJFQROSOKKOZCLLMEJ5EM6JXFR25IGXYDPY5Q===="
otp = pyotp.TOTP(secret_key)
# Generate an OTP using TOTP after every 30 seconds
while True:
    print(f"Your Time-based OTP at {time.ctime()}:", otp.now())

    time.sleep(10)
