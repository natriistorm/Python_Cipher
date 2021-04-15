import abstract_class
import string


class Caesar(abstract_class.AbstractCipher):
    shift_key = 1
    input_text = []
    output_text = ""

    def __init__(self, key: str, text: str):
        self.shift_key = int(key)
        self.input_text = text.split('\n')
        self.output_text = ""

    def shift(self, n: str, flag: int) -> str:
        if n not in string.ascii_letters:
            return n
        if n.isupper():
            new_symbol = chr(ord('A') + (ord(n) - ord('A') + (flag * self.shift_key)) % 26)
            return new_symbol
        if n.islower():
            new_symbol = chr(ord('a') + (ord(n) - ord('a') + (flag * self.shift_key)) % 26)
            return new_symbol

    def encrypt(self):
        encrypted_line = ""
        for line in self.input_text:
            for sym in line:
                encrypted_line += self.shift(sym, 1)
            self.output_text += encrypted_line
            self.output_text += "\n"
            encrypted_line = ""

    def decrypt(self):
        encrypted_line = ""
        for line in self.input_text:
            for sym in line:
                encrypted_line += self.shift(sym, -1)
            self.output_text += encrypted_line
            self.output_text += "\n"
            encrypted_line = ""

    def start(self, action: str):
        if action == 'Encrypt':
            self.encrypt()
        if action == 'Decrypt':
            self.decrypt()
