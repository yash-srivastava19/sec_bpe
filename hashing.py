from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class CorpusCipherMapping:
    def __init__(self, key, iv, mode=None, backend=default_backend()):
        self.cipher = Cipher(algorithms.ChaCha20(key, iv), mode=mode, backend=backend)
        self.key = key
        self.nonce = iv 

    def encrypt(self, message):
        encryptor = self.cipher.encryptor()
        if type(message) == str:
            return encryptor.update(message.encode('utf-8'))
        elif type(message) == bytes:
            return encryptor.update(message)
        else:
            raise ValueError("Message must be of type str or bytes")
        
    def decrypt(self, ciphertext):
        try:
            decryptor = self.cipher.decryptor()
            return decryptor.update(ciphertext)
        except Exception as e:
            raise e
        
# key = os.urandom(32)
# iv = os.urandom(16)

# cp = CorpusCipherMapping(key, iv)

# print(cp.decrypt(cp.encrypt("This is a not secret message!")))  