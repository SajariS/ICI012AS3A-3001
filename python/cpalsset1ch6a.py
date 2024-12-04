from base64 import b64decode
import itertools
from eng_score import  evaluate_string
from pprint import pprint 

def hammingWheight():
    weights = {0:0}
    pow2 = 1
    for _ in range(8):
        for k, v in weights.copy().items():
            weights[k+pow2] = v+1
        pow2 <<= 1
    return weights
weights = hammingWheight()

def bytesXor(a: bytes, b: bytes):
    return bytes((byte1 ^ byte2) for byte1, byte2 in zip(a, b))

def hammingCalc(s1, s2):
    return sum(weights[byte] for byte in bytesXor(s1, s2))

MAX_KEYSIZE = 40
def guessKeysize(ct: bytes, guesses: int = 1):
    def get_score(size: int):
        chunks = (ct[:size],
                  ct[size:2*size],
                  ct[2*size:3*size])
        avg = sum(hammingCalc(a, b) for a, b in itertools.combinations(chunks, 2)) / 6
        return avg / size
    
    scores = [(get_score(size), size) for size in range(2, MAX_KEYSIZE+1)]
    scores.sort()
    return scores[:guesses]

def crackRepeatingXor(cipher: bytes, keysize: int):
    chunks = [cipher[i::keysize] for i in range(keysize)]
    cracks = [crackSingleXor(chunk) for chunk in chunks]

    combinedScore = sum(guess[0] for guess in cracks) / keysize
    key = bytes(guess[1] for guess in cracks)
    return combinedScore, key

def crackSingleXor(cipher: bytes):
    canditates = []

    for keyCanditate in range(256):
        fullKey = bytes([keyCanditate]) * len(cipher)
        plaintext = bytesXor(fullKey, cipher)
        score = evaluate_string(plaintext)
        canditates.append((score, keyCanditate))
    
    canditates.sort(reverse=True, key=lambda score: score[0])
    return canditates[0]

def repeatingXor(cipher: bytes, key: int, keysize: int):
    out = b''
    i = 0
    for byte in cipher:
        if i == keysize:
            i = 0
        out += bytes([byte ^ key[i]])
        i += 1
    
    return out
    

if __name__=="__main__":
    assert hammingCalc(b'this is a test', b'wokka wokka!!!') == 37

    with open("./6.txt") as f:
        b64 = f.read()
    ciphertext = b64decode(b64)
    keysizes = guessKeysize(ciphertext, 5)
    
    canditates = [crackRepeatingXor(ciphertext, guess) for _, guess in keysizes]
    canditates.sort()
    bestCandidate = canditates[0]
    bestKey = bestCandidate[1]
    print("bestkey: ")
    pprint(bestKey.decode('ascii'))
    print(repeatingXor(ciphertext, bestKey, len(bestKey)).decode('ascii'))
