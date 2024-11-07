MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

method = input("type encrypt to encrypte, type decrypt to decrypte: ").lower()


# method for encrypt morse code
def encrypt(e_text):
    cipher = ""

    #iterate word per word
    for letter in e_text:
        # adding from dictionary morse code per letter
        # one space indicate different character
        # two spaces indicate different words
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter.upper()] + " "
        else:
            cipher += " "
    return cipher


# method for decrypt morse code
def decrypt(d_text):
    pass


if method == "encrypt":
    text_to_encrypte = input("Text to encrypte: ")
    encrypt(e_text=text_to_encrypte)

elif method == "decrypt":
    text_to_decrypte = input("Text to decrypte: ")
    decrypt(d_text=text_to_decrypte)

else:
    print("Try again. Use only encrypt or decrypt")
