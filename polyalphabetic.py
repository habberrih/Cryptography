cipher_text = []
plain_text = []

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

even_key = [  
    'k', 'c', 'h', 'f', 'n', 'w', 'q', 'o', 'm', 'j', 'b', 'v', 'a', 'z', 'p',
    's', 'x', 'u', 'r', 'l', 'g', 't', 'e', 'd', 'i', 'y'
]

odd_key = [  
    's', 'c', 'l', 'q', 'm', 'h', 'u', 'g', 'n', 'v', 'z', 'k', 'd', 'e', 'i',
    'a', 'b', 'w', 't', 'y', 'r', 'f', 'o', 'p', 'x', 'j'
]

def encrypt(text):

    for i in range(len(text)):
        letter_number = letters.index(text[i])
        if (i + 1) % 2 == 0: # i = 0, and first character is odd_key, this is why (i+1)
            cipher_letter = even_key[letter_number]
            cipher_text.append(cipher_letter)
        else:
            cipher_letter = odd_key[letter_number]
            cipher_text.append(cipher_letter)

    return ''.join(cipher_text)
    

def decrypt(text):

    for i in range(len(text)):
        if (i + 1) % 2 == 0:
            key1_number = even_key.index(text[i])
            plain_letter = letters[key1_number]
            plain_text.append(plain_letter)
        else:
            key2_number = odd_key.index(text[i])
            plain_letter = letters[key2_number]
            plain_text.append(plain_letter)

    return ''.join(plain_text)


def poly_alphabetic_cipher(text):
    
    cipher_text = encrypt(text)
    plain_text = decrypt(cipher_text)

    print("Ciphertext: " + ''.join(cipher_text))
    print("Plaintext: " + ''.join(plain_text))

def main():
    plain_text = input("Enter the text: ")
    poly_alphabetic_cipher(plain_text)

if __name__ == '__main__':
    main()