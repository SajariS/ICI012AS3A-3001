hexList = [bytes.fromhex(line.strip()) for line in open("./4.txt")]
keyList = [i for i in range(255)]

def scoreString(s):
    comparison = list('ETAOINSHRDLUetaoinshrdlu')
    score = 0
    for char in s:
        score += 1 if chr(char) in comparison else 0
    return score

def formCipher(hex, key):
    out = b''
    out += bytes(char ^ key for char in hex)
    return out

candidates = []
i = 1
for hex in hexList:
    for key in keyList:
        cipher = formCipher(hex, key)
        score = scoreString(cipher)
        if score > 0:
            candidates.append((cipher, score, key, i))
    i += 1
        
candidates.sort(reverse=True, key = lambda score: score[1])
candidates = candidates[:5]
for tuple in candidates:
    print(f'Answer: {tuple[0]} score = {tuple[1]} key = "{chr(tuple[2])}" line = {tuple[3]}')