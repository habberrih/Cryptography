letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

key = [
        'k', 'c', 'h', 'f', 'n', 'w', 'q', 'o', 'm', 'j', 'b', 'v', 'a', 'z', 'p',
        's', 'x', 'u', 'r', 'l', 'g', 't', 'e', 'd', 'i', 'y'
    ]

def encrypt(text):
    cipher_text = []
    for i in text:
        l_index = letters.index(i)
        new_letter = key[l_index]
        cipher_text.append(new_letter)

    return ''.join(cipher_text)


def decrypt(text):
    plain_text = []
    for i in text:
        l_index = key.index(i)
        new_letter = letters[l_index]
        plain_text.append(new_letter)

    return ''.join(plain_text)


def mono_alphabetic_cipher(text):
    


    cipher_text = encrypt(text)
    plain_text = decrypt(cipher_text)

    print("Ciphertext:", cipher_text)
    print("Plaintext: ", plain_text)


def main():
    plain_text = input("Enter the text: ")
    mono_alphabetic_cipher(plain_text)

if __name__ == "__main__":
    main()