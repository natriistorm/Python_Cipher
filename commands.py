
# 1 - encrypt with Caesar
# 2 - encrypt with Vigenere
# 3 - encrypt with Vemar

import sys
import caesar
import vigenere

def choose_action(action, cipher, data, key_data):
    if cipher == 'Caesar':
        caesar.caesar_main(action, data, key_data)
    elif cipher == 'Vigenere':
        vigenere.vigenere_main(action, data, key_data)



def show_help():
    print('Something went wrong. Checkout your input')
    print('Options:')
    print('--action [name]  Choose one of the actions: Encrypt, Decrypt')
    print('--cipher [name]  Choose one of the ciphers: Caesar, Vigenere, Vernam')
    print('--key [name]  Enter the file with the key')
    print('--input_file [name]  Enter the file with the text to encrypt or to decrypt')


def input():
    action = sys.argv[1]
    if not action:
        show_help()
        sys.exit()

    cipher = sys.argv[2]
    if not cipher:
        show_help()
        sys.exit()

    key = sys.argv[3]
    if not key:
        show_help()
        sys.exit()
    with open(key, "r") as k:
        keydata = k.read()

    filename = sys.argv[4]
    if not filename:
        show_help()
        sys.exit()
    with open(filename, "r") as f:
        data = f.read()

    choose_action(action, cipher, data, keydata)


input()
