hex = bytes.fromhex(input("Anna hex: "))
key = ord(input("Anna avain: "))

out = b''
out += bytes(char ^ key for char in hex)

print("".join(chr(char) for char in out))