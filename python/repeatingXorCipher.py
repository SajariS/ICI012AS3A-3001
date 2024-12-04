from base64 import b64decode

def decryptRepeatingXor(cipher: bytes, keysize: int, key: int):
    out = b''
    i = 0
    for byte in cipher:
        if i == keysize:
            i = 0
        out += bytes([byte ^ key[i]])
        i += 1
    
    return out

if __name__=="__main__":
    with open("./6.txt") as f:
        b64 = f.read()
    ciphertext = b64decode(b64)
    avain = (bytes(input("Anna avain: "), 'ascii'))

    print(decryptRepeatingXor(ciphertext, len(avain), avain).decode('ascii'))