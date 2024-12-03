teksti = input("Anna dekryptattava teksti: ")
dekrypt = ""

for char in teksti:
    dekrypt += chr(ord(char) - 2)

print(dekrypt)