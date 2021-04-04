import string

def shift(n, shift_step, flag):
    if n not in string.ascii_letters:
        return n
    if n.isupper():
        new_symbol = chr(ord('A') + (ord(n) - ord('A') + (flag * shift_step)) % 26)
        return new_symbol
    if n.islower():
        new_symbol = chr(ord('a') + (ord(n) - ord('a') + (flag * shift_step)) % 26)
        return new_symbol


def caesar_main(action, text, key):
    text_list = text.split('\n')
    n = int(key)
    encrypted_line = ""
    new_file = ""
    for line in text_list:
        for sym in line:
            if action == 'Encrypt':
                encrypted_line += shift(sym, n, 1)
            elif action == 'Decrypt':
                encrypted_line += shift(sym, n, -1)
        new_file += encrypted_line
        new_file += "\n"
        encrypted_line = ""
    for line in new_file.split("\n"):
        print(line)