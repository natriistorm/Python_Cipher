import parser
import text_work
import caesar
import vigenere
import vernam


def choose_cipher(args, data, keydata):
    if args.cipher == 'Caesar':
        output_file = caesar.caesar_main(args.action, data, keydata)
    elif args.cipher == 'Vigenere':
        output_file = vigenere.vigenere_main(args.action, data, keydata)
    elif args.cipher == 'Vernam':
        output_file = vernam.vernam_main(args.action, data, keydata)
    if args.output is not None:
        text_work.user_output(output_file, args.output)
    else:
        text_work.user_output(output_file)

args = parser.parser()
keydata = text_work.user_input(args.key_file)
data = text_work.user_input(args.input)
choose_cipher(args, data, keydata)