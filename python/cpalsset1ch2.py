# Itse kirjoitettu vastaus
hex = bytes.fromhex("1c0111001f010100061a024b53535009181c")
keylist = bytes.fromhex("686974207468652062756c6c277320657965")
answer = ""


for char, key in zip(hex, keylist):
    answer += chr(char ^ key)

# AI jälkikäteen generoima vastaus, jolla pyritään pelaamaan pelkillä bytes objekteilla
result = bytes(char ^ key for char, key in zip(hex, keylist))


#Tarkistus
expected = "746865206b696420646f6e277420706c6179"
print("Oma")
print(answer.encode('utf-8').hex())
print("Oikein" if answer.encode('utf-8').hex() == expected else "Väärin")
print("GPT")
print(result.hex())
print("Oikein" if result.hex() == expected else "Väärin")