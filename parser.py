import argparse


def parser():
    main_parser = argparse.ArgumentParser()
    crypt_subparsers = main_parser.add_subparsers(dest='func')
    cipher_parser = crypt_subparsers.add_parser("Action")

    cipher_parser.add_argument('action', choices=['Encrypt', 'Decrypt', 'Hack', 'Train'])
    cipher_parser.add_argument("cipher", choices=['Caesar', 'Vigenere', 'Vernam'],
                               help='Choose Cipher: Caesar or Vigenere or Vernam', default=None)
    cipher_parser.add_argument('key_file', help='Enter the name of the file with cipher key:'
                                                'an integer for Caesar and a string for Vigenere and Vernam. You don"t '
                                                'need it for Hack mode', default=None)
    cipher_parser.add_argument('--input', help='Enter the name of file with text to encrypt/decrypt',
                               default=None)
    cipher_parser.add_argument('--output', help='Enter the name of file to put the encrypted/decrypted text,'
                                                'for the Train mode enter the JSON file', default=None)
    args = cipher_parser.parse_args()
    return args
