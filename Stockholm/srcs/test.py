from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Define the key and IV
key = 'This is a key123'
iv2 = 'This is an IV456'

iv = "Red-Taylor-Swift"

print(len(iv), len(iv2), len(key))
# 
# Ensure the message is padded to a multiple of AES block size (16 bytes)
message = "The answer is no"
message_bytes = message.encode('utf-8')  # Convert message to bytes
# padded_message = pad(message_bytes, AES.block_size)
# 
# Encrypt the padded message
# obj = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
# ciphertext = obj.encrypt(padded_message)
# print("Ciphertext:", ciphertext)

# Decrypt the message
# obj2 = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
# decrypted_padded_message = obj2.decrypt(ciphertext)

# Unpad the decrypted message
# decrypted_message = unpad(decrypted_padded_message, AES.block_size).decode('utf-8')
# print("Decrypted message:", decrypted_message)

from Crypto.Cipher import AES
obj = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
message = message_bytes
ciphertext = obj.encrypt(message)
print(ciphertext, type(ciphertext))
obj2 = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
print(obj2.decrypt(ciphertext).decode())