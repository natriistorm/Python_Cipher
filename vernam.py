import abstract_class


def to_letters_or_numbers(answer: list) -> list:
    ans = []
    for i in range(len(answer)):
        if answer[i] < 0:
            ans.append('\n')
        else:
            ans.append(chr(answer[i] + 11))
    return ans


def finding_slashes(text: str) -> int:
    back_slashes_count = 0
    for sym in text:
        if sym == '\n':
            back_slashes_count += 1
    return back_slashes_count


class Vernam(abstract_class.AbstractCipher):
    def __init__(self, key: str, text: str, action: str):
        back_slashes_text = finding_slashes(text)
        self.binary_shift_key = bytes(key, encoding='utf-8')
        self.binary_input_text = bytes(text, encoding='utf-8')
        self.output_text = ""
        if len(self.binary_shift_key) != len(self.binary_input_text) - back_slashes_text:
            raise ValueError('Key text must the same length as the text')
        self.start(action)

    def crypt(self, flag: int) -> list:
        counter = 0
        answer = []
        for i in range(len(self.binary_shift_key)):
            if self.binary_input_text[i + counter] == ord('\n'):
                answer.append(-ord('\n'))
                counter += 1
            temp = int(self.binary_input_text[i + counter] - 11 * flag) ^ int(self.binary_shift_key[i])
            temp -= 11 * flag
            answer.append(temp)
        return answer

    def encrypt(self):
        answer = self.crypt(0)
        self.output_text = ''.join(to_letters_or_numbers(answer))

    def decrypt(self):
        answer = self.crypt(1)
        self.output_text = ''.join(to_letters_or_numbers(answer))
