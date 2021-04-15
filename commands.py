import parser
import text_work
import caesar
import vigenere
import vernam
import abstract_class


def choose_cipher(args, data, keydata):
    if args.cipher == 'Caesar':
        output_file = caesar.caesar_main(args.action, data, keydata)
    elif args.cipher == 'Vigenere':
        output_file = vigenere.vigenere_main(args.action, data, keydata)
    elif args.cipher == 'Vernam':
        output_file = vernam.vernam_main(data, keydata)
    text_work.user_output(output_file, args.output)


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
        result = cipher.encrypt()
    elif args.action == "Decrypt":
        result = cipher.decrypt()
    text_work.user_output(cipher.output_text, args.output)


if __name__ == "__main__":
    main()
