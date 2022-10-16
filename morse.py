english_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
                    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
                    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 
                    'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..', 
                    }


MORSE_TO_ENGLISH = {}
for key, value in english_to_morse.items():
    MORSE_TO_ENGLISH[value] = key

def morse_to_english(morse_code):
    morse_code = morse_code.split(" ")
    english = []
    for code in morse_code:
        if code in MORSE_TO_ENGLISH:
            english.append(MORSE_TO_ENGLISH[code])
    return " ".join(english)


def main():
    
    morse = input("Enter Morse code: ")
    english = morse_to_english(morse)
    print("English Letter: ", english)


if __name__ == "__main__":
    main()