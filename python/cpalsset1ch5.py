input = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"

out = b''
i = 0
for char in input:
    if i == 3:
        i = 0
    out += bytes([char ^ key[i]])
    i += 1

print(out.hex())

correct = bytes.fromhex("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")

print("Oikea vastaus!" if correct == out else "Väärä vastaus")