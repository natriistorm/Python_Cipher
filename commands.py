import parser
import text_work
import caesar
import vigenere
import vernam
import trainer
import abstract_class


def main():
    args = parser.parser()
    keydata = text_work.user_input(args.key_file)
    data = text_work.user_input(args.input)
    cipher = abstract_class.AbstractCipher

    if args.action == "Hack":
        if args.cipher == "Caesar":
            cipher.hack("text.json")
        else:
            raise ValueError("Only Caesar cipher can be hacked!")

    if args.action == "Train":
        trainer.train(data, args.output)
    else:
        if args.cipher == "Caesar":
            cipher = caesar.Caesar(keydata, data, args.action)
        elif args.cipher == "Vigenere":
            cipher = vigenere.Vigenere(keydata, data, args.action)
        elif args.cipher == "Vernam":
            cipher = vernam.Vernam(keydata, data, args.action)
        text_work.user_output(cipher.output_text, args.output)


if __name__ == "__main__":
    main()
