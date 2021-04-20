import sys


def user_input(file=None):
    if file is None:
        text = sys.stdin.read()
        return text
    with open(file, 'r') as f:
        return f.read()


def user_output(text, file=None):
    if file is None:
        print(text)
    else:
        with open(file, 'w') as f:
            return f.write(text)
