import sys


def user_input(file=None):
    if file is None:
        text = sys.stdin.read()
        return text
    with open(file, 'r') as f:
        return f.read()


def user_output(text, file=None):
    if file is None:
        for line in text.split("\n"):
            print(line)
    else:
        with open(file, 'w') as f:
            return f.write(text)
