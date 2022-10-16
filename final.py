# Final Decryption 

from caesar import encrypt as caeser_encrypt, decrypt as caeser_decrypt
from polyalphabetic import encrypt as polyalphabetic_encrypt, decrypt as polyalphabetic_decrypt
from hill import encrypt as hill_encrypt, decrypt as hill_decrypt


def get_caeser_key(key):
    key_list = list(key)

    key_numbers_list = []
    i = 0
    key_sum = 0
    length = len(key_list)

    while i < length:

        number = ord(key_list[i]) - ord('a')
        key_numbers_list.append(number)
        key_sum += key_numbers_list[i]
        i += 1

    key_sum = key_sum * length
    return key_sum

################################    ROTATION    #######################################
def rotate_text(text):
    list_text = list(text)
    length = len(list_text)
    n = 4
    list_text = list_text[n:] + list_text[:n]
        
    return ''.join(list_text)
        

def original_rotation(text):
    list_text = list(text)
    length = len(list_text)
    n = 4
    list_text = list_text[-n:] + list_text[:-n]     

    return ''.join(list_text)


################################    POSITION    #######################################
def positions_exchange(text):
    list_text = list(text)
    text_positions = []

    i = 0
    while i < len(list_text):

        if (i+1) == len(list_text):
            text_positions.append(list_text[i])
            break
        else:
            first = list_text[i]
            second = list_text[i + 1]
        
            text_positions.append(second)
            text_positions.append(first)

        i += 2
    
    return ''.join(text_positions)

def original_positions(text):

    list_text = list(text)
    original_text_positions = []

    i = 0
    while i < len(list_text):

        if (i+1) == len(list_text):
            original_text_positions.append(list_text[i])
            break
        else:
            first = list_text[i]
            second = list_text[i + 1]
        
            original_text_positions.append(second)
            original_text_positions.append(first)

        i += 2
    
    return ''.join(original_text_positions)

################################    ALGORITHM PROCESS   #######################################
def encrypt(text, key):
    global caeser_key 
    caeser_key = get_caeser_key(key)

    t1_positions = positions_exchange(text)
    t1_rotation = rotate_text(t1_positions)

    caeser_en_text = caeser_encrypt(t1_rotation, caeser_key)

    t2_rotation = rotate_text(caeser_en_text)
    t2_positions = positions_exchange(t2_rotation)

    poly_en_text = polyalphabetic_encrypt(t2_positions)

    t3_positions = positions_exchange(poly_en_text)
    t3_rotation = rotate_text(t3_positions)

    hill_en_text = hill_encrypt(t3_rotation, key)

    t4_positions = positions_exchange(hill_en_text)
    t4_rotation = rotate_text(t4_positions)
    
    
    cipher_text = t4_rotation

    return cipher_text

def decrypte(cipher, key):

    t4_Orotation = original_rotation(cipher)
    t4_Opositions = original_positions(t4_Orotation)

    hill_de_text = hill_decrypt(t4_Opositions, key)

    t3_Orotation = original_rotation(hill_de_text)
    t3_Opositions = original_positions(t3_Orotation)

    poly_de_text = polyalphabetic_decrypt(t3_Opositions)

    t2_Opositions = original_positions(poly_de_text)
    t2_Orotation = original_rotation(t2_Opositions)

    caeser_de_text = caeser_decrypt(t2_Orotation, caeser_key)

    t1_Orotation = original_rotation(caeser_de_text)
    t1_Opositions = original_positions(t1_Orotation)

    plain_text = t1_Opositions

    return plain_text

################################    MAIN ALGORITHM    #######################################
def my_algorithm(text, key):

    cipher_text = encrypt(text, key)
    plain_text = decrypte(text, key)
    print()
    #print("Ciphertext:", cipher_text)
    print("Plaintext: ", plain_text)
    print()


def main():
    plain_text = input("Enter the cipher text: ")
    key = input("Enter a key: ")

    my_algorithm(plain_text, key)

if __name__ == "__main__":    
    main()