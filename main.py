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
                        '"': '.-..-.', "$": '...-..-', '@': '.--.-.', ' ': ' '}}


# method for encrypt morse code
def encrypt(e_text):
    cipher = ""
    # iterate word per word
    is_exit = True
    for letter in e_text:
        if e_text == "e" or e_text == "exit":
            exit()
        # adding from dictionary morse code per letter
        # one space indicate different character
        # two spaces indicate different words
        elif letter.upper() in MORSE_CODE_DICT["letters"]:
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
    # counts number of spaces
    i = 0
    # deciphered text
    decipher = ""
    # putting together characters from input to prepare it for decryption
    morse_code = ""
    is_exit = True
    for morse in d_text:
        # one space separate character, two spaces separate words
        # if its character, not a space adding it to string
        if d_text.lower() == "e" or d_text == "exit":
            print(d_text)
            exit()
        elif morse != " ":
            # resets spaces
            i = 0
            morse_code += morse
        # decoding character is letter
        elif morse_code in MORSE_CODE_DICT["letters"].values():
            # counting number of spaces
            i += 1
            if i == 2:
                # adding space to separate words
                decipher += " "
            else:
                # adding character(values) from dictionary with keys
                decipher += list(MORSE_CODE_DICT["letters"].keys())[
                    list(MORSE_CODE_DICT["letters"].values()).index(morse_code)]
                # resets morse_code to start assemble new letter
                morse_code = ""
        # decoding if its symbol
        elif morse_code in MORSE_CODE_DICT["else"].values():
            i += 1
            if i == 2:
                decipher += " "
            else:
                decipher += list(MORSE_CODE_DICT["else"].keys())[
                    list(MORSE_CODE_DICT['else'].values()).index(morse_code)]
                morse_code = ""
        else:
            # return to text decrypt if its not decoded text
            print("Write only decoded text.")
            is_exit = False
    # false statement allow to not printing empty list
    if is_exit:
        print(f"decrypted code: {decipher}")
        return decipher


# program start by selecting method
method = input("Type encrypt or decrypt: ").lower()


# defining new function for choosing method
def method_choice(method_to_choose):
    if method_to_choose == "encrypt":
        text_to_encrypt = input("Text to encrypt (type 'e' or 'exit' to exit): ")
        encrypt(e_text=text_to_encrypt)

    elif method_to_choose == "decrypt":
        text_to_decrypt = input("Text to decrypt(type 'e' or 'exit' to exit): ")
        decrypt(d_text=text_to_decrypt)

    else:
        print("Try again. Use only encrypt or decrypt")
        return method_choice(input("Type encrypt or decrypt: ").lower())


# creating loop allow to stay in program
while method.lower() != "exit" or method.lower() != "e":
    method_choice(method)

