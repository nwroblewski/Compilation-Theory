
import sys
import scanner
import mparser

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example1.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = mparser.parser
    text = file.read()
    scanner.line = text
    parser.parse(text, lexer=scanner.lexer)