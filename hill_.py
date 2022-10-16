
# Hill Encryption 

keyMatrix = [[0] * 2 for i in range(2)]
keyInverse = [[0] * 2 for j in range(2)]
keyDecryptMatrix = [[0] * 2 for k in range(2)]
plain_text_Matrix = [[0] for m in range(2)]
cipher_text_Matrix = [[0] for n in range(2)]

plain_text = []
cipher_text = []

################################    REQUIRED METHODS    #######################################
def split_text(text):
    text_pairs = []

    i = 0
    while i < len(text):
        a = text[i]
        b = ''

        if (i+1) == len(text): # Insert a filler character x
            b = 'x'
        else:
            b = text[i+1]
    
        text_pairs.append(a+b)
        i += 2
    return text_pairs
    

def get_key_matrix(key):
    key_matrix = [[0] * 2 for i in range(2)]
    k = 0
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = ord(key[k]) % 97
            k += 1
    return key_matrix

def mod_inverse(diameter, nums_of_letters):
    for x in range(1, nums_of_letters):
        if ((diameter % nums_of_letters) * (x % nums_of_letters)) % nums_of_letters == 1:
            return x     
    print("Module number Not Found !!\n")
    quit()

def get_key_matrix_inverse(key_inv):
    for i in range(2):
        for j in range(2):
            if i == j == 0:
                tmp = key_inv[i][j]
                key_inv[i][j] = key_inv[i + 1][j + 1]
                key_inv[i + 1][j + 1] = tmp
            elif i != j:
                key_inv[i][j] = key_inv[i][j] * -1
                key_inv[i][j] = key_inv[i][j] % 26

            keyInverse[i][j] = key_inv[i][j]


def get_key_matrix_determinant(key):
    for i in range(2):
        for j in range(2):
            if i == j == 0:
                main_diameter = key[i][j] * key[i + 1][j + 1]
            elif i == 0 and j == 1:
                sub_diameter = key[i][j] * key[j][i]

    key_d = (main_diameter - sub_diameter) % 26
    return key_d


def generate_key_decrypt(diameter, inverse):
    number_mod_inverse = mod_inverse(diameter, 26)

    for i in range(2):
        for j in range(2):
            keyDecryptMatrix[i][j] = (inverse[i][j] * number_mod_inverse) % 26

################################    ALGORITHM PROCESSING    #######################################
def encrypt(text, key):
    global text_length
    text_length = len(text)

    key_matrix = get_key_matrix(key)

    text_pairs = split_text(text)

    row = 0
    for i in range(len(text_pairs)):
        
        for i in range(2):
            plain_text_Matrix[i][0] = ord(text_pairs[row][i]) % 97
        
        if row < len(text_pairs):
            for i in range(2):
                for j in range(1):
                    cipher_text_Matrix[i][j] = 0
                    for x in range(2):
                        cipher_text_Matrix[i][j] += (key_matrix[i][x] * plain_text_Matrix[x][j])
    
                cipher_text_Matrix[i][j] = cipher_text_Matrix[i][j] % 26
            
            for i in range(2):
                cipher_text.append(chr(cipher_text_Matrix[i][0] + 97))

        row += 1
    
    return ''.join(cipher_text)
    

def decrypt(text, key):
    # cipher_matrix = [[0] for n in range(2)] #
    key_matrix = get_key_matrix(key)
    key_diameter = get_key_matrix_determinant(key_matrix)
    get_key_matrix_inverse(key_matrix)
    generate_key_decrypt(key_diameter, keyInverse)

    cipher_pairs = split_text(text)
    
    row = 0
    
    for i in range(len(cipher_pairs)):
        
        for i in range(2):
            cipher_text_Matrix[i][0] = ord(cipher_pairs[row][i]) % 97 #

        if row < len(cipher_pairs):

            for i in range(2):
                for j in range(1):
                    plain_text_Matrix[i][j] = 0
                    for x in range(2):
                        plain_text_Matrix[i][j] += (keyDecryptMatrix[i][x] * cipher_text_Matrix[x][j])
                    plain_text_Matrix[i][j] = plain_text_Matrix[i][j] % 26

            for i in range(2):
                plain_text.append(chr(plain_text_Matrix[i][0] + 97))
        row += 1

    if (text_length % 2) != 0: # delete the filler characters x
        plain_text.pop()

    return ''.join(plain_text)
    
################################    MAIN ALGORITHM    #######################################
def hill_cipher(text, key):
    cipher_text = encrypt(text, key)
    plain_text = decrypt(cipher_text, key)
    
    print("Ciphertext:", ''.join(cipher_text))
    # print("Plaintext: ",  ''.join(plain_text))
    print()


def main():
    plain_text = input("Enter the plain text: ")
    key = input("Enter the key: ")

    print()
    hill_cipher(plain_text, key)

if __name__ == "__main__":
    main()