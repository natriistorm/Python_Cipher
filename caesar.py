import abstract_class
import string
import json
import getting_stat


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

    def hack(self, model_file):
        alphabet = string.ascii_lowercase
        current_stat = getting_stat.get_stat(self.input_text)
        with open(model_file, "r") as f:
            true_stat = json.load(f)
        best_k = 0
        best_distance = -1
        for k in range(1, len(alphabet)):
            distance = getting_stat.find_model_distance(k, current_stat, true_stat)
            if distance < best_distance or best_distance == -1:
                best_distance = distance
                best_k = k
        self.shift_key = best_k
        self.decrypt()
