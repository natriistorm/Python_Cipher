from itertools import cycle


def dict_creation():
    dictionary = {}
    missed_symbols = 0
    for i in range(60):
        if (ord('A') <= i + 65 <= ord('Z')) or (ord('a') <= i + 65 <= ord('z')):
            dictionary[i - missed_symbols] = chr(i + 65)
        else:
            missed_symbols += 1
    return dictionary


def start_encoding(word):
    symbols_and_indexes = []
    dictionary = dict_creation()
    for symbol in word:
        for key, value in dictionary.items():
            if symbol == value:
                symbols_and_indexes.append(key)
    return symbols_and_indexes


def comparing_key_with_indexes(value, key):
    return dict([(indexes, [ch[0], ch[1]])
                for indexes, ch in enumerate(zip(value, cycle(key)))])


def final_encoding(value, key):
    dictionary = comparing_key_with_indexes(value, key)
    answer = []
    length = len(dict_creation())

    for v in dictionary.values():
        temp_sum = (v[0] + v[1]) % length
        answer.append(temp_sum)
    return answer


def start_decoding(word):
    decode = []
    dictionary = dict_creation()

    for symbol in word:
        if symbol in dictionary:
            decode.append(dictionary[symbol])
    return decode


def final_decoding(value, key):
    dictionary = comparing_key_with_indexes(value, key)
    answer = []
    length = len(dict_creation())

    for v in dictionary.values():
        dif = (v[0] - v[1] + length) % length
        answer.append(dif)
    return answer


def vigenere_main(action, text, key):
    encoded_key = start_encoding(key)
    text_list = text.split('\n')
    encrypted_line = ""
    new_file = ""
    for line in text_list:
        cur_ind = 0
        while cur_ind < len(line):
            word = ""
            if not ('a' <= line[cur_ind] <= 'z') and not('A' <= line[cur_ind] <= 'Z'):
                cur_ind += 1
                continue
            while cur_ind < len(line) and (('a' <= line[cur_ind] <= 'z') or ('A' <= line[cur_ind] <= 'Z')):
                word += line[cur_ind]
                cur_ind += 1
            encoded_word = start_encoding(word)
            encrypted_word = final_encoding(encoded_word, encoded_key)
            if action == "Encrypt":
                encrypted_line += ''.join(start_decoding(encrypted_word))
                encrypted_line += ' '
            elif action == "Decrypt":
                decrypted_word = final_decoding(encoded_word, encoded_key)
                decrypted_word_list = start_decoding(decrypted_word)
                encrypted_line += ''.join(decrypted_word_list)
                encrypted_line += ' '
        new_file += encrypted_line
        new_file += "\n"
        encrypted_line = ""
    for line in new_file.split("\n"):
        print(line)
