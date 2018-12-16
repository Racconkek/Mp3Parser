from ID3v1 import *
from ID3v2 import *
import re
from arg_parser import ArgParser

class Parser:
    def __init__(self):
        self.ID3v1 = ID3v1()
        self.ID3v2 = ID3v2()

    def parse_file(self, file_name):
        self.parse_tag1(file_name)
        self.parse_tag2(file_name)

    def parse_tag1(self, file_name):
        try:
            with open(file_name, 'rb') as file:
                file.seek(-128, 2)
                if file.read(3) == b'TAG':
                    file.seek(-128, 2)
                    self.ID3v1.parse_info(file.read(128))
                    print(str(self.ID3v1))
                else:
                    print('No ID3v1 TAG')
        except Exception:
            print('Can\'t open file')

    def parse_tag2(self, file_name):
        try:
            with open(file_name, 'rb') as file:
                if file.read(3) == b'ID3':
                    self.ID3v2.parse_file(file)
                    print(str(self.ID3v2))
                else:
                    print('No ID3v2 TAG')
        except Exception:
            print('Can\'t open file')


def main():
    parser = Parser()
    ar = ArgParser()
    try:
        file_name, commands = ar.parse_arguments()
        for command in commands:
            if command == 'parse tag1':
                parser.parse_tag1(file_name)
            elif command == 'parse tag2':
                parser.parse_tag2(file_name)
            elif command == 'parse':
                parser.parse_file(file_name)
    except Exception as e:
        print(str(e))
# while not end:
#     command = input()
#     if command == 'parse tag1' and file_name is not None:
#         parser.parse_tag1(file_name)
#     elif command == 'parse tag2' and file_name is not None:
#         parser.parse_tag2(file_name)
#     elif re.match(r'set file .+.mp3', command) is not None:
#         file_name = command[9:]
#         print(file_name)
#     elif command == 'end':
#         end = True
#     elif command == 'parse' and file_name is not None:
#         parser.parse_file(file_name)
    # parser.parse_file('30 Seconds To Mars - This Is War.mp3')

if __name__ == '__main__':
    main()
