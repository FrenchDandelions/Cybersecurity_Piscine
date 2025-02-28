import time
import pyotp

secret_key = b"OEEJI6QTP45CNFRXJFQROSOKKOZCLLMEJ5EM6JXFR25IGXYDPY5Q===="
otp = pyotp.TOTP(secret_key)
while True:
    print(f"Your Time-based OTP at {time.ctime()}:", otp.now())

    time.sleep(10)
