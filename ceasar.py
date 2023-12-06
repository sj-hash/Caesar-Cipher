def encrypt(txt, s):
    result = ""
    for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 64) % 26 + 64)
        else:
            result += chr((ord(char) + s - 96) % 26 + 96)
    return result
def decrypt(txt , s):
    result = ""
    for i in range(len(txt)):
        char = txt[i]
        if (char.isupper()):
            result += chr((ord(char)-s -64)% 26 +64)
        else:
            result += chr((ord(char)-s-96)%26+96)
    return result

d = input("Enter the process (encryption/decryption (e/d))")
if (d=='e'):
    txt = input("Enter the plaintext ")
else:
    txt = input("Enter the ciphertext ")
s = int(input("Enter the key "))
if (d=='e'):
    txt2 = encrypt(txt,s)
    print("Ciphertext: "+txt2)
else:
    txt2 = decrypt(txt,s)
    print("Plaintext: "+txt2)
