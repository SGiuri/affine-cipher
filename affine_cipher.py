import re


def encode(plain_text, a, b):
    '''
    E(x) = (ax + b) mod m

    where x is the letter's index from 0 - length of alphabet - 1
    m is the length of the alphabet. For the roman alphabet m == 26.
    and a and b make the key
    the decryption function is:
    '''

    clear_text = re.sub(f"[^a-zA-Z0-9\']", "", plain_text).lower()
    m = 26
    encrypted_text_string = ""
    for letter in clear_text:
        try:
            int(letter)
            encrypted_text_string += letter
        except:

            x = ord(letter) - ord("a")

            encripted_x = (a * x + b) % m
            encrypted_text_string += chr(encripted_x + ord("a"))
    print(clear_text, encrypted_text_string)
    encrypted_text = " ".join([encrypted_text_string[j:j + 5] for j in range(0, len(encrypted_text_string), 5)])
    return encrypted_text


def decode(ciphered_text, a, b):
    pass
