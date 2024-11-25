# dictionary containing letters and its equivalent in morse code
MORSE_CODE_DICT = {'letters':
                       {'A': '.-', 'B': '-...',
                        'C': '-.-.', 'D': '-..', 'E': '.',
                        'F': '..-.', 'G': '--.', 'H': '....',
                        'I': '..', 'J': '.---', 'K': '-.-',
                        'L': '.-..', 'M': '--', 'N': '-.',
                        'O': '---', 'P': '.--.', 'Q': '--.-',
                        'R': '.-.', 'S': '...', 'T': '-',
                        'U': '..-', 'V': '...-', 'W': '.--',
                        'X': '-..-', 'Y': '-.--', 'Z': '--..', }
    , 'else':
                       {'1': '.----', '2': '..---', '3': '...--',
                        '4': '....-', '5': '.....', '6': '-....',
                        '7': '--...', '8': '---..', '9': '----.',
                        '0': '-----', ',': '--..--', '.': '.-.-.-',
                        '?': '..--..', '/': '-..-.', '-': '-....-',
                        '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                        '&': '.-...', ':': '---...', ';': '-.-.-.',
                        '=': '-...-', '+': '.-.-.', '_': '..--.-',
                        '"': '.-..-.', "$": '...-..-', '@': '.--.-.'}}
# Start by selecting method
method = input("Type encrypt or decrypt: ").lower()


# method for encrypt morse code
def encrypt(e_text):
    cipher = ""
    # iterate word per word
    for letter in e_text:
        # adding from dictionary morse code per letter
        # one space indicate different character
        # two spaces indicate different words
        if letter.upper() in MORSE_CODE_DICT["letters"]:
            if letter != " ":
                cipher += MORSE_CODE_DICT['letters'][letter.upper()] + " "
            else:
                cipher += " "
        else:
            if letter != " ":
                cipher += MORSE_CODE_DICT["else"][letter] + " "
            else:
                cipher += " "
    print(f"encrypted code: {cipher}")
    return cipher


# method for decrypt morse code
def decrypt(d_text):
    # adding space in the end of text helps with sliced last character
    d_text += " "
    # counts number of spaces
    i = 0
    # deciphered text
    decipher = ""
    # putting together characters from input to prepare it for decryption
    morse_code = ""
    for morse in d_text:
        # one space separate character, two spaces separate words
        # if its character, not a space adding it to string
        if morse != " ":
            # resets spaces
            i = 0
            morse_code += morse
        # decoding character is letter
        elif morse_code in MORSE_CODE_DICT["letters"].values():
            # counting number of spaces
            i += 1
            if i >= 2:
                # adding space to separate words
                decipher += " "
            else:
                # adding character(values) from dictionary with keys
                decipher += list(MORSE_CODE_DICT["letters"].keys())[
                    list(MORSE_CODE_DICT["letters"].values()).index(morse_code)]
                # resets morse_code to start assemble new letter
                morse_code = ""
        # decoding if its symbol
        else:
            i += 1
            if i >= 2:
                decipher += " "
            else:
                decipher += list(MORSE_CODE_DICT["else"].keys())[
                    list(MORSE_CODE_DICT['else'].values()).index(morse_code)]
                morse_code = ""
    print(f"decrypted code: {decipher}")
    return decipher


if method.lower() == "exit" or method.lower() == "e":
    if method == "encrypt":
        text_to_encrypt = input("Text to encrypt: ")
        encrypt(e_text=text_to_encrypt)

    elif method == "decrypt":
        text_to_decrypt = input("Text to decrypt: ")
        decrypt(d_text=text_to_decrypt)

    else:
        print("Try again. Use only encrypt or decrypt")
