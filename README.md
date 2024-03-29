## SecBPE - A modified,secure version of Byte Pair Encoding algorithm
SecBPE is an innovative modification to Byte Pair Encoding (BPE) for tokenization, focusing on enhancing privacy and effectiveness. There are many approaches on improving BPE, and I tried experimenting before I went ahead with this one. But first, a question arises, why does BPE needs improvement?

## Understanding Byte Pair Encoding (BPE)
Like most people in the world, I'm a big fan of karpathy, and he was the motivation behind this project. Everyone knows that BPE is used almost everywhere, but few understand the inner workings of the algorithm. BPE, basically compresses language into tokens by merging frequent bigram words, establishing a lookup table of merges and vocabulary. I would highly, highly recommend the minBPE video by karpathy, as it sets up a really good base for this project.
It is not that I want to change BPE, but I wanted to understand an alternate to this scheme and that's how Sec-BPE came into picture. Let us see how and what made me to think in this direction.

## Sec-BPE Approach
As I understood Byte Pair Encoding (BPE), and reading through the Random BPE paper, I was convinvced that the algorithm's greediness doesn't significantly impact its effectiveness, taking me to a different path where I can "improve" the algorithm. This line of thought prompted me to consider tokens from a matrix representation perspective, drawing parallels to the structure found in Playfair ciphers. Thinking about the potential use of hashing as a compression algorithm for tokenization, I recognized its limitations due to its irreversiblity( and that too without a means of decoding!).
It was this moment where I realised that I can use Block Ciphers(ChaCha20, which is kinda my favourite) as a way to generate a proxy corpus on which I can do BPE(block ciphers produce ciphertext of equal length from a given corpus). This was basically a signal for me to start the coding, and I will continue to design experiments on this(will be released here itself). Inspired by these insights, I questioned the feasibility of utilizing ciphertext for generating merges and vocabularies, giving rise to a novel approach to BPE wherein a proxy corpus generates proxy merges and vocabularies, with decoding simply requiring a reverse process.

## Advantages and Disadvantages
### Advantages : 
- Data privacy and obfuscation.
- Increased entropy and randomness might improve the effectiveness of BPE(how?)
	- In the ciphertext, the byte pairs are much more evenly distributed, and the frequency of any particular byte pair is likely to be lower compared to the plaintext. This increased entropy and randomness can lead to more effective byte pair merging by the BPE algorithm
	- Analogy : Imagine you're trying to compress a long string of digits, like "1234567890123456789012345678901234567890". In this case, the BPE algorithm might not be very effective because there are no obvious repeating patterns or frequent substrings to merge. However, if you first apply a random permutation to the string (e.g., "5273981064698710235647182309456781092"), the BPE algorithm may find more opportunities for merging due to the increased randomness and distribution of digits.
- Maybe the model generalizes well on unseen data.

### Disadvantages :
- Increased computational overhead.
- Key management?
- Potential loss of interpretability.(Hard one)
	- There are some approaches that attempt to preserve certain semantic properties or relationships within the data while still providing a level of obfuscation or privacy. One such approach is called "semantic-preserving hashing" or "similarity-preserving hashing." These techniques aim to generate hash values such that similar inputs produce similar hash values, while dissimilar inputs produce dissimilar hash values.
	- In the context of your proposed approach, using a semantic-preserving hashing technique instead of a block cipher encryption could potentially mitigate the loss of interpretability to some extent. However, it's crucial to carefully evaluate the trade-offs between interpretability, security, and the specific requirements of your application.

## Conclusion
The proposed enhanced BPE approach offers a promising solution for tokenization, addressing privacy concerns while acknowledging trade-offs in efficiency and interpretability. Please teach me more, and we can make it into something awesome!! Raise a PR, or mail me(or better, hmu on Twitter)!
