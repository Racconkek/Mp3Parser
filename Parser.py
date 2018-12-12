from ID3v2 import *
from ID3v1 import *


class Parser:
    def __init__(self):
        self.ID3v1 = ID3v1()
        self.ID3v2 = ID3v2()

    def parse_file(self, file_name):
        with open(file_name, 'rb') as file:
            # if file.read(3) == b'ID3':
            #     file.seek(0, 0)
            #     self.ID3v2.parse_info(file)
            #     print(str(self.ID3v2))
            # else:
            #     print('No ID3v2 TAG')
            # Работает
            file.seek(-128, 2)
            if file.read(3) == b'TAG':
                file.seek(-128, 2)
                self.ID3v1.parse_info(file.read(128))
                print(str(self.ID3v1))
            else:
                print('No ID3v1 TAG')


def main():
    parser = Parser()
    parser.parse_file('30 Seconds To Mars - This Is War.mp3')


if __name__ == '__main__':
    main()
