import base64
import itertools

def hammingCalc(s1, s2):
    sum = 0
    for char1, char2 in zip(s1, s2):
        sum += 1 if char1 != char2 else 0
    
    return sum

def binaryString(s):
    binary = ''
    for byte in s:
        binary += format(byte, '08b')
    return binary

def calculateKeysize(s):
    candidates = []
    for x in range(60):
        if x <= 1:
            continue
        s1 = s[:x]
        s2 = s[x:(x + x)]
        normalized = hammingCalc(binaryString(s1), binaryString(s2)) / x
        candidates.append((x, normalized))

    candidates.sort(key=lambda normal: normal[1])
    return candidates[0]

def splitIntoBlocks(s, keysize):
    return [s[i:i+keysize] for i in range(0, len(s), keysize)]

def transposeBlocks(blocks):
    length = max(len(block) for block in blocks)
    transposed = [b''.join(block[i:i+1] for block in blocks if i < len(block)) for i in range(length)]
    return transposed

def calculateKey(block):
    possibleKeys = [i for i in range(255)]
    candidates= []
    for key in possibleKeys:
        cipher = b''
        cipher += bytes(char ^ key for char in block)
        score = scoreString(cipher)
        candidates.append((key, score))
    candidates.sort(reverse=True, key=lambda score: score[1])
    return candidates[:5]


def scoreString(s):
    comparison = list(b'ETAOINSHRDLUetaoinshrdlu')
    score = 0
    for char in s:
        score += 1 if char in comparison else 0
    return score

def generateCombinations(keys):
    return list(itertools.product(*keys))

def decodeBytes(s, key):
    out = b''
    i = 0
    for char in s:
        if i == len(key):
            i = 0
        out += bytes([char ^ key[i]])
        i += 1
    
    return out

def main():
    hexList = [bytes(line.strip(), 'utf-8') for line in open("./6.txt")]
    encodedHex = b''.join(hexList)
    hex = b''
    hex += base64.decodebytes(encodedHex)
    keysize = calculateKeysize(hex)[0]
    blocks = transposeBlocks(splitIntoBlocks(hex, keysize))
    keyCandidates = []
    for block in blocks:
        keys = calculateKey(block)
        keyCandidates.append([key[0] for key in keys])
    
    keyCombinations = generateCombinations(keyCandidates)

    
    candidates = []
    for keys in keyCombinations:
        out = b''
        out += (bytes(decodeBytes(splitIntoBlocks(hex, keysize)[0], keys)))
        score = scoreString(out)
        candidates.append((out, score, keys))   

    candidates.sort(reverse=True, key=lambda score: score[1])
    candidates = candidates[:100]
    f = open("./out.txt", "w")
    for candidate in candidates:
        f.write("Keys:")
        f.write(''.join(chr(key) for key in candidate[2]))
        f.write('\n')
        f.write("Points: ")
        f.write(str(candidate[1]))
        f.write('\n')
        f.write(candidate[0].decode('utf-8'))
        f.write('\n')



if __name__ == "__main__":
    main()