import string
def encrypt(message, key):
    alpha = string.ascii_lowercase
    new = ""
    for i in message:
        if i not in key:
            new += i
        else:
            crypt = alpha.find(i)
            new += key[crypt]
    return new

def decrypt(message, key):
    alpha = string.ascii_lowercase
    new = ""
    for i in message:
        if i not in alpha:
            new += i
        else:
            crypt = key.find(i)
            new += alpha[crypt]
    return new


print(encrypt("the good ol boyos", "qwertyuiopasdfghjklzxcvbnm"))
print(decrypt("zit uggr gs wgngl", "qwertyuiopasdfghjklzxcvbnm"))