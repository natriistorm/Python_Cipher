import argparse
import sys


def parser():
    main_parser = argparse.ArgumentParser()
    crypt_subparsers = main_parser.add_subparsers(dest='func')
    cipher_parser = crypt_subparsers.add_parser("Encrypt or Decrypt")

    cipher_parser.add_argument('action', choices=['Encrypt', 'Decrypt'])
    cipher_parser.add_argument("cipher", choices=['Caesar', 'Vigenere', 'Vernam'],
                               help='Choose Cipher: Caesar or Vigenere or Vernam')
    cipher_parser.add_argument('key_file', help='Enter the name of the file with cipher key:'
                                                'an integer for Caesar and a string for Vigenere and Vernam')
    cipher_parser.add_argument('--input', help='Enter the name of file with text to encrypt/decrypt',
                               default=None)
    cipher_parser.add_argument('--output', help='Enter the name of file to put the encrypted/decrypted text',
                               default=None)
    args = cipher_parser.parse_args()
    return args
