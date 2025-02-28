#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
from utils import Argument, _change_color, bcolors, print_header, print_key_value
import hmac
import base64
import datetime
import string


class HOTP:
    def __init__(self, key=b'password', counter_value="0", len_pwd=6, byteorder="big", verbose=False, color=False):
        self.key = base64.b32decode(key, casefold=True)
        self.verbose = verbose
        self.color = color
        if self.verbose == True:
            print_header("HOTP ALGO")
            if self.color == True:
                print_key_value("Base32 secret:", base64.b32encode(self.key).decode(), bcolors.GREEN)
            else:
                print_key_value("Base32 secret:", base64.b32encode(self.key).decode())

        self.counter_value = counter_value
        self.len_pwd = len_pwd
        self.htop = None
        self.byteorder = byteorder
        pass
    
    
    def Dynamic_Truncation(self):
        offset = self.hmac_res[19] & 0xf #work as well: 0b1111 0xb00001111 15
        bin_code = (
            (self.hmac_res[offset] & 0x7f) << 24
            | (self.hmac_res[offset + 1] & 0xff) << 16
            | (self.hmac_res[offset + 2] & 0xff) << 8
            | (self.hmac_res[offset + 3] & 0xff)
        )
        if self.verbose == True:
            color = bcolors.GREEN if self.color == True else ""
            print_key_value("HMAC Digest:", self.hmac_res.hex(), color)
            print_key_value("Offset:", offset, color)
            print_key_value("Truncated value:", bin_code, color)

        return bin_code
    
    def generate_hotp(self):
        counter_bytes = self.counter_value.to_bytes(8, byteorder=self.byteorder)
        hs_hmac = hmac.new(self.key, counter_bytes, "sha1")
        self.hmac_res = hs_hmac.digest()
        self.htop = self.Dynamic_Truncation()
        self.otp = self.htop % 10 ** self.len_pwd
        if self.verbose == True:
            color = bcolors.GREEN if self.color == True else ""
            print_key_value("Counter Bytes:", counter_bytes.hex(), color)
            print_key_value("OTP generated:", self.otp, color)
        return self.otp
    
    def get_hotp(self):
        if self.htop == None:
            print("HOTP object: generate_htop function not called, generating first", 
                "otp of object", self)
            self.generate_hotp()
        return self.otp
    


class TOTP(Argument):
    def __init__(self, timer=30, verbose=False, color=False, path_fernet_key="~/.hidden_fernet_key.key", arg=None):

        self.verbose = verbose
        self.color = color

        super().__init__(arg=arg)

        if self.fernet_key_file == None:
            self.hidden_file = os.path.expanduser(path_fernet_key)
        else:
            self.hidden_file = os.path.expanduser(self.fernet_key_file)
        
        self.time_value = timer # this is in seconds
        self.key = ""



    def run(self):
        if self.mode == True:
            self.generate_password()
        else:
            self.generate_key()
    
    
    def get_decryption(self):
        with open(self.hidden_file, "r") as f:
            fernet_key = f.read()
        fernet = Fernet(fernet_key)
        with open("ft_otp.key", "rb") as f:
            encryption = f.read()
        decryption = fernet.decrypt(encryption)
        return decryption


    def totp(self):
        time_now = datetime.datetime.now(datetime.timezone.utc)
        seconds_since_epoch = int(time_now.timestamp())
        time_steps = int(seconds_since_epoch / self.time_value)
        if self.verbose == True:
            color = bcolors.BRIGHT_MAGENTA if self.color == True else ""
            print_key_value("Epoch Time (UTC):", seconds_since_epoch, color)
            print_key_value("Time Now =>", time_now, color)
            print_key_value("Counter (TOTP Step):", time_steps, color)
            print_key_value("TIME_STEPS =>", time_steps, color)
        new_hotp = HOTP(key=self.key, counter_value=time_steps, verbose=self.verbose,color=self.color)
        otp = new_hotp.generate_hotp()
        return otp


    def generate_password(self):
        if self.verbose == True:
            print_header("Starting Password Generation")
        self.key = self.get_decryption()

        if self.verbose == True:
            color = bcolors.BRIGHT_MAGENTA if self.color == True else ""
            print_key_value("Base32 secret:", self.key.decode(), color)
        totp = self.totp()
        if self.verbose == True:
            color = bcolors.GREEN if self.color == True else ""
            print_key_value("Generated OTP:", totp, color)

        print_header("Password generated!")

        if self.color == True:
            _change_color(bcolors.RED)
            print(str(totp).center(40, " "))
            _change_color(bcolors.ENDC)
        else :
            print(str(totp).center(40, " "))

        print()
        return


    def generate_key(self):
        fkey = Fernet.generate_key()
        with open(self.hidden_file, "wb") as f:
            f.write(fkey)
        fernet = Fernet(fkey)
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

        decoded_key = bytes.fromhex(s)
        encrypt_key = base64.b32encode(decoded_key)
        encrypt_key = fernet.encrypt(encrypt_key)
        with open("ft_otp.key", 'wb') as f:
            f.write(encrypt_key)
        print()
        print("Key generated!".center(40, "~"))
        if self.verbose == True:
            if self.color == True :
                print("Key =>")
                _change_color(bcolors.BRIGHT_CYAN)
                print(encrypt_key.decode())
                _change_color(bcolors.ENDC)
            else :
                print("Key =>", encrypt_key.decode())
            print("~"*40)
            print()

        return


def main():
    otp = TOTP(color=False, verbose=False)
    otp.run()
    return


if __name__ == "__main__":
    # try:
        main()
    # except Exception as e:
        # print(e)

