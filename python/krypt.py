teksti = input("Anna kryptattava teksti: ")
krypt = ""

for char in teksti:
    krypt += chr(ord(char) + 2)

print(krypt) 