import math


def encrypt(text, key):
	cipher_text = ""

	k_index = 0

	text_length = int(len(text))
	text_list = list(text)
	key_list = sorted(list(key))

	column_number = len(key)
	row = int(math.ceil(text_length / column_number))
	fill_null = int((row * column_number) - text_length)
	text_list.extend('_' * fill_null)
	
	cipher_matrix = [text_list[i: i + column_number] for i in range(0, len(text_list), column_number)]

	
	for i in range(column_number):
		current_index = key.index(key_list[k_index])
		cipher_text += ''.join([row[current_index] for row in cipher_matrix])
		k_index += 1

	return cipher_text


def decrypt(text, key):
	plain_text = ""

	k_index = 0

	text_index = 0
	text_length = int(len(text))
	text_list = list(text)

	column_number = len(key)
	row = int(math.ceil(text_length / column_number))
	key_list = sorted(list(key))

	decrypte_cipher = []
	for i in range(row):
		decrypte_cipher += [[None] * column_number] # create empty list 

	for i in range(column_number):
		current_index = key.index(key_list[k_index])
		for j in range(row):
			decrypte_cipher[j][current_index] = text_list[text_index]
			text_index += 1
		k_index += 1

	try:
		plain_text = ''.join(sum(decrypte_cipher, []))
	except TypeError:
		raise TypeError("This program cannot",
						"handle repeating words.")

	null_count = plain_text.count('_')

	if null_count > 0:
		return plain_text[: -null_count]

	return plain_text

def columnar_cipher(text, key):

	cipher_text = encrypt(text, key)
	plain_text = decrypt(cipher_text, key)

	print("Ciphertext:", cipher_text)
	print("Plaintext: ", plain_text)

def main():

	plain_text = input("Enter a plaintext: ")                       # "hello world!"
	key = input("Enter a key: ")                                    #"Hack"

	columnar_cipher(plain_text, key)

if __name__ == "__main__":
	main()
