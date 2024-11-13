MORSE_CODE_DICT = {'letters':
                       {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',}
                   ,'else':
                       {'1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
                   '&': '.-...', ':': '---...', ';': '-.-.-.',
                   '=': '-...-', '+': '.-.-.', '_': '..--.-',
                   '"': '.-..-.', "$": '...-..-', '@': '.--.-.'}}

method = input("Type encrypt or decrypt: ").lower()


# method for encrypt morse code
def encrypt(e_text):
    cipher = ""
    #iterate word per word
    for letter in e_text:
        # adding from dictionary morse code per letter
        # one space indicate different character
        # two spaces indicate different words
        if letter.upper() in MORSE_CODE_DICT["letters"]:
            if letter != " ":
                cipher += MORSE_CODE_DICT['letters'][letter.upper()] + " "
            else:
                cipher += " "
        else :
            if letter != " ":
                cipher += MORSE_CODE_DICT["else"][letter] + " "
            else:
                cipher += " "
    print(f"encrypted code: {cipher}")
    return cipher


# method for decrypt morse code
def decrypt(d_text):
    decipher = ""
    spaces = 0
    morse_code = ""
    for morse in d_text:
        if morse != " ":
            morse_code += morse
        elif morse == " " and spaces == 0:
            if morse in MORSE_CODE_DICT["letters"]:
                spaces += 1
                key_list = [key for key, val in MORSE_CODE_DICT["letters"].items() if val == morse_code]
                print(key_list)
                decipher += MORSE_CODE_DICT["letters"][key_list][0]
            elif morse in MORSE_CODE_DICT["else"]:
                spaces += 1
                key_list = [key for key, val in MORSE_CODE_DICT["else"].items() if val == morse_code]
                print(key_list)
                decipher += MORSE_CODE_DICT["else"][key_list][0]
        elif morse == " " and spaces == 1:
            decipher += " "
            spaces = 0
    print(f"decrypted code: {decipher}")
    return decipher

if method == "encrypt":
    text_to_encrypt = input("Text to encrypte: ")
    encrypt(e_text=text_to_encrypt)

elif method == "decrypt":
    text_to_decrypt = input("Text to decrypte: ")
    decrypt(d_text=text_to_decrypt)

else:
    print("Try again. Use only encrypt or decrypt")
