#!/usr/bin/env python3
import os
import encodings
# import hashlib
from cryptography.fernet import Fernet
from utils import Argument


class TOTP(Argument):
    def __init__(self):
        super().__init__()
        self.hidden_file = os.path.expanduser("~/.hidden_fernet_key.key")
    
    def run(self):
        if self.mode == True:
            self.generate_password()
        else:
            self.generate_key()
    
    
    def get_decryption(self):
        with open(self.hidden_file, "r") as f:
            fernet_key = f.read()
        fernet = Fernet(fernet_key)
        print(fernet_key)
        with open("ft_otp.key", "rb") as f:
            encryption = f.read()
        print(encryption)
        decryption = fernet.decrypt(encryption)
        return decryption.decode()
    
    def generate_password(self):
        decryption = self.get_decryption()
        print(decryption)
        print("Password generated!")
        return
    
    
    def generate_key(self):
        fkey = Fernet.generate_key()
        with open(self.hidden_file, "wb") as f:
            f.write(fkey)
        fernet = Fernet(fkey)
        file = ""
        with open(self.file, 'rb') as f:
            file = f.read()
        print(file)
        encrypt_key = fernet.encrypt(file)
        with open("ft_otp.key", 'wb') as f:
            f.write(encrypt_key)
        print("Key generated!")

        return


def main():
    otp = TOTP()
    otp.run()
    return


if __name__ == "__main__":
    # try:
        main()
    # except Exception as e:
        # print(e)

