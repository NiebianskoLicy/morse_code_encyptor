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

# splitting text to words to encode or decode
def to_list(t_text):
    text_list = [letter.split() for letter in t_text]
    return  text_list

# method for encrypt morse code
def encrypte(e_text):
    to_list(e_text)

# method for decrypt morse code
def decrypte(d_text):
    pass

if method == "encrypt":
    encrypte(e_text=method)

elif method == "decrypt":
    decrypte(d_text=method)
else:
    print("Try again. Use only encrypt or decrypt")
