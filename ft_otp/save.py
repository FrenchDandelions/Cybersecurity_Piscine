#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
from utils import Argument, _change_color, bcolors
import hmac
import base64
key = b'7108947a137f3a26963749611749ca53b225ad844f48cf26e58eba835f037e3b'
base32_key = base64.b32encode(key).decode('utf-8')

import time
import datetime
import string


class HOTP:
    def __init__(self, key=b'password', counter_value="0", len_pwd=6, byteorder="big"):
        # self.key = key
        self.key = base64.b32decode(key)

        
        print("KEY =>", self.key)
        self.counter_value = counter_value
        self.len_pwd = len_pwd
        self.htop = None
        self.byteorder = byteorder
        pass
    
    
    def Dynamic_Truncation(self):
        offset = self.hmac_res[-1] & 0x0F #work as well: 0b1111 0xF 15
        bin_code = (
            (self.hmac_res[offset] & 0x7f) << 24
            | (self.hmac_res[offset + 1] & 0xff) << 16
            | (self.hmac_res[offset + 2] & 0xff) << 8
            | (self.hmac_res[offset + 3] & 0xff)
        )
        print("HMAC Digest:", self.hmac_res.hex())
        print("Offset:", offset)
        print("Truncated value:", bin_code)

        return bin_code
    
    def generate_hotp(self):
        counter_bytes = self.counter_value.to_bytes(8, byteorder=self.byteorder)
        print("Counter Bytes:", counter_bytes.hex())
        hs_hmac = hmac.new(self.key, counter_bytes, "sha1")
        self.hmac_res = hs_hmac.digest()
        # print("HMAC Digest:", self.hmac_res.hex())
        self.htop = self.Dynamic_Truncation()
        self.otp = self.htop % 10 ** self.len_pwd
        print("OTP generated:", self.otp)
        # print(bin(self.htop))
        return self.otp
    
    def get_hotp(self):
        if self.htop == None:
            print("generate_htop function not called, generating first", 
                "otp of object", self)
            self.generate_hotp()
        return self.otp
    


class TOTP(Argument):
    def __init__(self, timer=30, path_fernet_key="~/.hidden_fernet_key.key", print_data=False, color=False):
        super().__init__()
        self.hidden_file = os.path.expanduser(path_fernet_key)
        self.time_value = timer # this is in seconds
        self.key = ""
        self.print = print_data
        self.color = color
    
    def run(self):
        if self.mode == True:
            self.generate_password()
        else:
            self.generate_key()
    
    
    def get_decryption(self):
        # with open(self.hidden_file, "r") as f:
            # fernet_key = f.read()
        # fernet = Fernet(fernet_key)
        # print(fernet_key)
        with open("ft_otp.key", "rb") as f:
            encryption = f.read()
        # print(encryption)
        # decryption = fernet.decrypt(encryption)
        # hex_key = decryption.hex()
        # return hex_key.encode()
        return encryption
    
    
    def totp(self):
        time_now = datetime.datetime.now()
        seconds_since_epoch = time.mktime(time_now.timetuple())
        print("Current epoch time:", seconds_since_epoch)
        time_steps = int(seconds_since_epoch / self.time_value)
        print("TIME_STEPS =>", time_steps)
        new_hotp = HOTP(key=self.key, counter_value=time_steps)
        otp = new_hotp.generate_hotp()
        return otp
    
    
    def generate_password(self):
        self.key = self.get_decryption()
        # print(self.key)
        print("Decrypted key:", self.key)
        totp = self.totp()
        print("Generated OTP:", totp)
        print()
        print("Password generated!".center(40, "~"))
        print()
        
        if self.color == True:
            _change_color(bcolors.RED)
            print(str(totp).center(40, " "))
            _change_color(bcolors.ENDC)
        else :
            print(str(totp).center(40, " "))

        print()
        return
    
    
    def generate_key(self):
        # fkey = Fernet.generate_key()
        # with open(self.hidden_file, "wb") as f:
            # f.write(fkey)
        # fernet = Fernet(fkey)
        file = ""
        with open(self.file, 'rb') as f:
            file = f.read()
        s = file.decode()
        if all(c in string.hexdigits for c in s) == False or len(s) < 64:
            if self.color == True:
                _change_color(bcolors.FAIL)
            print("./ft_otp: error: key must be 64 hexadecimal characters.")
            if self.color == True:
                _change_color(bcolors.ENDC)
            raise
        
        
        # encrypt_key = fernet.encrypt(file)
        encrypt_key = base64.b32encode(file)
        with open("ft_otp.key", 'wb') as f:
            f.write(encrypt_key)
        print()
        print("Key generated!".center(40, "~"))
        if self.print == True:
            if self.color == True :
                print("Key =>")
                _change_color(bcolors.BRIGHT_CYAN)
                print(encrypt_key.decode())
                _change_color(bcolors.ENDC)
            else :
                print("Key =>", encrypt_key)
            print()

        return


def main():
    otp = TOTP(color=False, print_data=False)
    otp.run()
    return


if __name__ == "__main__":
    # try:
        main()
    # except Exception as e:
        # print(e)

