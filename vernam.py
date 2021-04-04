def to_letters_or_numbers(action, answer):
    ans = []
    i = 0
    while i < len(answer):
        cur_word = ""
        decimal_number = 0
        for j in range(i, i + 8):
            cur_word += answer[j]
        for l in range(len(cur_word)):
            cur_bit = int(cur_word[l])
            position = int(l)
            decimal_number += (cur_bit * (2 ** (7 - position)))
        if action == "Decrypt":
            ans.append(chr(decimal_number))
        else:
            ans.append(decimal_number)
        i += 8
    return ans


def vernam_main(action, text, key):
    if len(key) != len(text):
        print('Key text must the same length as the text')
        return
    text_binary = key_binary = ""
    for line in text:
        for sym in line:
            text_binary += bin(ord(sym))
    for line in key:
        for sym in line:
            key_binary += bin(ord(sym))
    answer = ""
    for i in range(len(text_binary)):
        if text_binary[i] == 'b':
            continue
        temp = int(text_binary[i]) ^ int(key_binary[i])
        answer += str(temp)
    ans = to_letters_or_numbers(action, answer)
    return ans
