cipher_text = []
plain_text = []

def encrypt(text, key):
    for i in range(len(text)):
        encrypted = chr((ord(text[i]) - ord('a') + key) % 26 + ord('a'))
        cipher_text.append(encrypted)

    return ''.join(cipher_text)
    
def decrypt(cipher, key):
    
    for i in range(len(cipher)):
        decrypted = chr((ord(cipher[i]) - ord('a') - key) % 26 + ord('a'))
        plain_text.append(decrypted)

    return ''.join(plain_text)


def caesar_cipher(plain_text, key):

    encrypt(plain_text, key)
    decrypt(cipher_text, key)

    print("Ciphertext: " + ''.join(cipher_text))
    print("Plaintext: " + ''.join(plain_text))

def main():
    plain_text = input("Enter the text for encryption: ")
    key = int(input("Enter the key: "))
    caesar_cipher(plain_text, key)

    print()

if __name__ == '__main__':
    main()