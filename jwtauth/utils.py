# from Crypto.Cipher import AES
#
# class Encryption:
#
#     BLOCK_SIZE = 16
#     key = b"1234567890123456"  # TODO change to something with more entropy
#
#     def do_encrypted_str(self, string):
#         hash_number = 0
#         if len(string) == 0:
#             return hash_number
#         for i in range(len(string)):
#             char = ord(string[i])
#             hash_number = ((hash_number << 5) - hash_number) + char
#             hash_number = hash_number & hash_number
#         return hash_number
#
#     def pad(self, data):
#         length = self.BLOCK_SIZE - (len(data) % self.BLOCK_SIZE)
#         return data + chr(length) * length
#
#     def unpad(self, data):
#         return data[:-ord(data[-1])]
#
#     def encrypt(self, message, key):
#         IV = Random.new().read(self.BLOCK_SIZE)
#         aes = AES.new(key, AES.MODE_CBC, IV)
#         return base64.b64encode(IV + aes.encrypt(pad(message)))
#
#     def decrypt(self, encrypted, key):
#         encrypted = base64.b64decode(encrypted)
#         IV = encrypted[:self.BLOCK_SIZE]
#         aes = AES.new(key, AES.MODE_CBC, IV)
#         return unpad(aes.decrypt(encrypted[self.BLOCK_SIZE:]))
