# Encryption

def encrypt_char(char, key):
    return chr(ord('A') + (ord(char) - ord('A') + 3) % 26)


def encrypt_message(message, key):
    message = message.upper()
    cipher = ''
    for c in message:
        if c in " .,":
            cipher += c
        else:
            cipher += encrypt_char(c, key)
    return cipher


print(encrypt_message("you are Awesome", 3))


# Decryption
def decrypt(char, key):
    return chr(ord('A') + (ord(char) - ord('A') + 26 - key) % 26)


def decrypt_message(cipher, key):
    message = ''
    for c in cipher:
        if c in " ,.":
            message += c
        else:
            message += decrypt(c, key)
    return message


print(decrypt_message("BRX DUH DZHVRPH ", 3))
