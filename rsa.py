import math

public_key = []
private_key = []

cipher_text = []
plain_text = []


################################    REQUIRED METHODS    #######################################
def get_n_m(p, q):
    n = p * q
    m = (p-1) * (q-1)

    return n, m

def modInverse(e, m):
    for x in range(1, m): 
        if ((e % m) * (x % m)) % m == 1:
            return x
    print("Module number Not Found !!")
    quit()

def isnot_prime(number):

    i = 2
    while i <= 2:
        if number % 2 == 0:
            return True
        i += 1


def get_keys(e, d, n):
    
    public_key.append(e)
    public_key.append(n)

    private_key.append(d)
    private_key.append(n)

    return public_key, private_key

################################    ALGORITHM PROCESSING    #######################################
def encrypt(text, e, n):
    text_list = list(text)

    i = 0
    while i < len(text_list):
        text_num = ord(text_list[i]) - ord('a')
        cipher = int(math.pow(text_num, e) % n) 
        cipher_text.append(chr(cipher + 97))
        i += 1
    
    return "".join(cipher_text)


def decrypt(text_list, d, n):

    i = 0
    while i < len(text_list):
        text_num = ord(text_list[i]) - ord('a')
        plain = int(math.pow(text_num, d) % n)
        plain_text.append(chr(plain + 97))
        i += 1
    
    return "".join(plain_text)


################################    MAIN ALGORITHM    #######################################
def rsa_cipher(text, p, q, e):
    n, m = get_n_m(p, q)
    d = modInverse(e,m)

    public_key, private_key = get_keys(e, d, n)

    cipher_text = encrypt(text, e, n)
    plain_text = decrypt(cipher_text, d, n)

    print("Public Key: ", public_key)
    print("Private Key: ", private_key)

    print("Ciphertext: ", cipher_text)
    print("Plaintext: ", plain_text)

def main():
    
    p = int(input("Enter a prime number for P: "))
    if isnot_prime(p):
        print("\nP is not a prime number\n")
        return

    q = int(input("Enter a prime number for Q: "))
    if  isnot_prime(q):
        print("\nQ is not a prime number\n")
        return

    e = int(input("Enter a random prime number for E: "))
    if isnot_prime(e):
        print("\nE is not a prime number\n")
        return

    plain_text = input("Enter the plain text: ")
    print()
    rsa_cipher(plain_text, p, q, e)    


if __name__ == "__main__":
    main()