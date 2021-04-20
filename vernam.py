import abstract_class


def to_letters_or_numbers(answer: list) -> list:
    ans = []
    for i in range(len(answer)):
        ans.append(chr(answer[i] + ord('A')))
    return ans


class Vernam(abstract_class.AbstractCipher):
    def __init__(self, key: str, text: str, action: str):
        self.binary_shift_key = bytes(key, encoding='utf-8')
        self.binary_input_text = bytes(text, encoding='utf-8')
        self.output_text = ""
        if len(self.binary_shift_key) != len(self.binary_input_text):
            raise ValueError('Key text must the same length as the text')
        self.start(action)

    def crypt(self) -> list:
        answer = []
        for i in range(len(self.binary_input_text)):
            temp = int(self.binary_input_text[i]) ^ int(self.binary_shift_key[i])
            answer.append(temp)
        return answer

    def encrypt(self) -> str:
        answer = self.crypt()
        self.output_text = ''.join(to_letters_or_numbers(answer))

    def decrypt(self) -> str:
        answer = self.crypt()
        self.output_text = ''.join(to_letters_or_numbers(answer))
