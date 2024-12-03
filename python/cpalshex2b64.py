import base64

hex = bytes.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

print(hex.decode('utf-8'))
print(base64.b64encode(hex).decode('utf-8'))

if "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t" == base64.b64encode(hex).decode('utf-8'):
    print("Oikein")