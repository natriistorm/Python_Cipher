import parser
import text_work
import caesar
import vigenere
import vernam


def main():
    args = parser.parser()
    keydata = text_work.user_input(args.key_file)
    data = text_work.user_input(args.input)

    if args.cipher == "Caesar":
        cipher = caesar.Caesar(keydata, data)
    elif args.cipher == "Vigenere":
        cipher = vigenere.Vigenere(keydata, data)
    elif args.cipher == "Vernam":
        cipher = vernam.Vernam(keydata, data)

    if args.action == "Encrypt":
        cipher.encrypt()
    elif args.action == "Decrypt":
        cipher.decrypt()
    text_work.user_output(cipher.output_text, args.output)


if __name__ == "__main__":
    main()
