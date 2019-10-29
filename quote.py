from random import randint
from ast import literal_eval
from json import dump
from sys import argv, exit
from getopt import getopt, GetoptError


class Quote:
    def __init__(self):
        with open("Quotes.txt") as input_file:
            self.Quote = literal_eval(input_file.read())
            input_file.close()
        self.main()

    def printQuote(self):
        print("\n\n"+self.Quote[randint(0, len(self.Quote)-1)]+"\n\n")

    def addQuote(self, new_quote):
        self.Quote.append(new_quote)
        with open("Quotes.txt", "w+") as input_file:
            dump(self.Quote, input_file)
            input_file.close()

    def main(self):
        try:
            opts, args = getopt(argv[1:], "a:h")
            if opts.__len__() == 0:
                self.printQuote()
                exit()
            for opt, arg in opts:
                if opt == '-h':
                    print("Usage: python3 quote <options>\nOptions\t\tDescription\n-h\t\tTo read this message\n-a "
                          "\"your_quote\"\tTo add a quote")
                    exit()
                elif opt in ['-add', '-a']:
                    self.addQuote(arg)
        except GetoptError:
            print("Use -h for help")
            exit(2)



q = Quote()
