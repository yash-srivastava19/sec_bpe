class BPE:
    def __init__(self, num_merges):
        self.num_merges = num_merges
        self.vocab = {}
        self.merges = []

    def get_vocab(self, text):
        for word in text.split(b' '):
            if word in self.vocab:
                self.vocab[word] += 1
            else:
                self.vocab[word] = 1

    def get_stats(self):
        pairs = {}
        for word, freq in self.vocab.items():
            symbols = str(word).split()
            for i in range(len(symbols)-1):
                pair = (symbols[i], symbols[i+1])
                if pair in pairs:
                    pairs[pair] += freq
                else:
                    pairs[pair] = freq
        return pairs

    def merge_vocab(self, pair):
        v_out = {}
        pair_str = b' '.join(pair)
        for word in self.vocab:
            w_out = word.replace(pair_str, b''.join(pair))
            v_out[w_out] = self.vocab[word]
        self.vocab = v_out

    def byte_pair_encoding(self, text):
        self.get_vocab(text)
        for i in range(self.num_merges):
            pairs = self.get_stats()
            if not pairs:
                break
            best = max(pairs, key=pairs.get)
            self.merges.append(best)
            self.merge_vocab(best)
    
    def get_merges(self):
        return self.merges
    
    def tokenize(self, text):
        tokens = list(text)
        for merge in self.merges:
            new_token = b''.join(merge)
            while new_token in tokens:
                i = tokens.index(new_token)
                tokens[i:i+2] = [new_token]
        return tokens

    def build_vocab(self, tokens):
        self.vocab = {token: i for i, token in enumerate(set(tokens))}
        return self.vocab
    
    def encode(self, text):
        tokens = self.tokenize(text)
        self.build_vocab(tokens)
        encoded = [self.vocab[token] for token in tokens]
        return encoded

    def build_reverse_vocab(self):
        return {i: token for token, i in self.vocab.items()}

    def decode(self, encoded):
        reverse_vocab = self.build_reverse_vocab()
        tokens = [reverse_vocab[i] for i in encoded]
        text = b''.join([bytes([token]) for token in tokens])
        return text
    
# # Instantiate the BPE class
# bpe = BPE(num_merges=7)

# # Assume corpus is a bytes object containing your text
# corpus = b"your text here"

# # Learn the merges and build the vocabulary
# bpe.byte_pair_encoding(corpus)

# # Tokenize and encode the text
# encoded = bpe.encode(corpus)
# print(encoded)
# # Decode the encoded text
# decoded = bpe.decode(encoded)
# print(decoded)