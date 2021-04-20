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
    if args.cipher == "Caesar":
        cipher = caesar.Caesar(keydata, data)
    elif args.cipher == "Vigenere":
        cipher = vigenere.Vigenere(keydata, data)
    elif args.cipher == "Vernam":
        cipher = vernam.Vernam(keydata, data)
    if args.action != "Train":
        if args.action == "Encrypt":
            cipher.encrypt()
        elif args.action == "Decrypt":
            cipher.decrypt()
        elif args.action == "Hack":
            if args.cipher == "Caesar":
                cipher.hack("text.json")
            else:
                raise ValueError("Only Caesar cipher can be hacked!")
        text_work.user_output(cipher.output_text, args.output)
    else:
        trainer.train(data, args.output)


if __name__ == "__main__":
    main()
