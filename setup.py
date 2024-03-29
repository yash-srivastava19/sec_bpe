import os 
from bpe import BPE
from hashing import CorpusCipherMapping

class SecBPETokenizer:
    def __init__(self, num_merges, key=os.urandom(32), iv=os.urandom(16)) -> None:
        self.num_merges = num_merges
        self.key = key
        self.nonce = iv

        self.bpe = BPE(num_merges=num_merges)
        self.cp = CorpusCipherMapping(self.key, self.nonce)

    def encode(self, text: bytes) -> bytes:
        if isinstance(text, str):
            ciphertext = self.cp.encrypt(bytes(text, 'utf-8'))
        elif isinstance(text, bytes):
            ciphertext = self.cp.encrypt(text)
        else:
            raise ValueError("Input must be of type str or bytes.")
        
        self.bpe.byte_pair_encoding(ciphertext)  # Basically, merging is of no use here, as maybe ciphertext is generating enough gibberish. See this.
        tokens = self.bpe.tokenize(ciphertext)
        self.bpe.build_vocab(tokens)
        encoded = self.bpe.encode(ciphertext)
        
        return encoded # returns list of integers
    
    def decode(self, encoded: bytes) -> bytes:
        decoded = self.bpe.decode(encoded)
        return self.cp.decrypt(decoded)  # returns bytes


if __name__ == '__main__':
    key = b'\x10g\xc0,!\xe2n@\xbc\x97\x84\xa1\xb56\xb6\x85f(\xc2\x1b\x9f\xce\x87\xbb!\xed\xe6\xbek~\xf1P'
    iv = b'\xc6!b^\x18\xed<\xedM~\xe1\xfb\xca\x9f\xce\xaf'

    text = b'This is a test sentence for Byte Pair Encoding.'
    chars = sorted(list(set(text)))  # possible elements from the dataset.
    vocab_size = len(chars)

    print(vocab_size)
    
    
    sbpe = SecBPETokenizer(5, key, iv)
    print("Encoded :",sbpe.encode(text))
    print("Decoded :",sbpe.decode(sbpe.encode(text)))