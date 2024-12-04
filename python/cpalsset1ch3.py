hex = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
charList = []

# Käännä käsiteltäväksi listaksi, merkit tulevat desimaali arvoina ascii taulukosta
for char in hex:
    charList.append(ord(chr(char)))

# Selvitä kaikki uniikit merkit ja luo uusi lista niistä
uniqueChrList = list(set(charList))

# Selvitä mikä uniikki merkki esiintyy eniten alkuperäisessä merkkijonossa
key = 0
count = 0
for char in uniqueChrList:
    if count < charList.count(char):
        key = char
        count = charList.count(char)

# Käännä alkuperäinen hex tunnistetulla avaimella
result = bytes(char ^ key for char in hex)
print(result.decode('utf-8'))

potentialKeys = [i for i in range(65, 122)]
ciphered = []

for key in potentialKeys:
    ciphered.append((bytes(char ^ key for char in hex).decode('utf-8'), key))


score = 0
answer = ""
comparison = list('ETAOINSHRDLUetaoinshrdlu')
scoreList = []

for text in ciphered:
    scoreList.append((text[0], sum(text[0].count(char) for char in comparison), text[1]))

scoreList.sort(reverse=True, key=lambda score: score[1])
scoreList = scoreList[:5]
print("Top 5:")
for tuple in scoreList:
   print(f'Answer: "{tuple[0]}" with score {tuple[1]} and key "{chr(tuple[2])}"')