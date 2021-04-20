from itertools import cycle
import abstract_class
import string


def dict_creation() -> dict:
    dictionary = {}
    missed_symbols = 0
    for i in range(60):
        if chr(i + 65) in string.ascii_letters:
            dictionary[i - missed_symbols] = chr(i + 65)
        else:
            missed_symbols += 1
    return dictionary


def comparing_key_with_indexes(value: list, key: list) -> dict:
    return dict([(indexes, [ch[0], ch[1]])
                 for indexes, ch in enumerate(zip(value, cycle(key)))])


def making_a_word(cur_ind: int, line: str) -> tuple:
    word = ""
    while cur_ind < len(line) and line[cur_ind] in string.ascii_letters:
        word += line[cur_ind]
        cur_ind += 1
    return word, cur_ind


class Vigenere(abstract_class.AbstractCipher):
    def __init__(self, key: str, text: str, action: str):
        self.dictionary_of_symbols = dict_creation()
        self.shift_key = self.start_encoding(key)
        self.input_text = text.split('\n')
        self.output_text = ""
        self.start(action)

    def start_encoding(self, word: str) -> list:
        symbols_and_indexes = []
        for symbol in word:
            for key, value in self.dictionary_of_symbols.items():
                if symbol == value:
                    symbols_and_indexes.append(key)
        return symbols_and_indexes

    def start_decoding(self, word: list) -> list:
        decode = []
        for symbol in word:
            if symbol in self.dictionary_of_symbols:
                decode.append(self.dictionary_of_symbols[symbol])
        return decode

    def getting_final_result(self, value: list, key: list, action_flag: int) -> list:
        dictionary = comparing_key_with_indexes(value, key)
        answer = []
        length = len(self.dictionary_of_symbols)

        for v in dictionary.values():
            if action_flag == 1:
                temp_result = (v[0] + v[1]) % length
            if action_flag == -1:
                temp_result = (v[0] - v[1] + length) % length
            answer.append(temp_result)
        return answer

    def encrypt(self):
        for line in self.input_text:
            worked_line = ""
            cur_ind = 0
            while cur_ind < len(line):
                if not line[cur_ind] in string.ascii_letters:
                    cur_ind += 1
                    continue
                word, cur_ind = making_a_word(cur_ind, line)
                encoded_word = self.start_encoding(word)
                encrypted_word = self.getting_final_result(encoded_word, self.shift_key, 1)
                worked_line += ''.join(self.start_decoding(encrypted_word))
                worked_line += ' '
            self.output_text += worked_line

    def decrypt(self):
        for line in self.input_text:
            worked_line = ""
            cur_ind = 0
            while cur_ind < len(line):
                if not line[cur_ind] in string.ascii_letters:
                    cur_ind += 1
                    continue
                word, cur_ind = making_a_word(cur_ind, line)
                encoded_word = self.start_encoding(word)
                decrypted_word = self.getting_final_result(encoded_word, self.shift_key, -1)
                decrypted_word_list = self.start_decoding(decrypted_word)
                worked_line += ''.join(decrypted_word_list)
                worked_line += ' '
            self.output_text += worked_line
