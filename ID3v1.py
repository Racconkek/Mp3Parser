import json


class ID3v1:
    def __init__(self):
        self.header = None
        self.title = None
        self.artist = None
        self.album = None
        self.year = None
        self.comment = None
        self.zero_byte = None  # Если есть номер трека, то установлен в 0
        self.track = None  # Номер трека
        self.genre = None

        with open('genres.json', 'r', encoding='utf-8') as f:
            self.genres = json.load(f)

    def parse_info(self, info):
        self.set_header(info[0:3])
        self.set_title(info[3:33])
        self.set_artist(info[33:63])
        self.set_album(info[63:93])
        self.set_year(info[93:97])
        self.set_zero_byte(info[125:126])
        if self.zero_byte == 0:
            self.set_comment(info[97:125])
            self.set_track(info[126:127])
        else:
            self.set_comment(info[97:127])
        self.set_genre(info[127:128])

    def set_header(self, info):
        self.header = info.decode('cp1251')

    def set_title(self, info):
        self.title = info.decode('cp1251')

    def set_artist(self, info):
        self.artist = info.decode('cp1251')

    def set_album(self, info):
        self.album = info.decode('cp1251')

    def set_year(self, info):
        self.year = info.decode('cp1251')

    def set_zero_byte(self, info):
        temp = int.from_bytes(info, byteorder='big')
        if temp == 0:
            self.zero_byte = temp

    def set_comment(self, info):
        self.comment = info.decode('cp1251')

    def set_track(self, info):
        self.track = int.from_bytes(info, byteorder='big')

    def set_genre(self, info):
        number = str(int.from_bytes(info, byteorder='big'))
        self.genre = self.genres[number]

    def __str__(self):
        info = 'ID3v1 TAG \n' + 'Title: ' + self.title + '\nArtist: ' + self.artist + '\nAlbum: ' + self.album +\
               '\nYear: ' + str(self.year) + '\nGenre: ' + self.genre
        if self.comment != "" or self.comment is not None:
            info += '\nComment: ' + self.comment
        else:
            info += '\nComment:'
        if self.zero_byte is not None and self.track != '':
            info += '\nNumber of track: ' + str(self.track)
        else:
            info += '\nNumber of track: unknown'
        return info


def main():
    pass

if __name__ == '__main__':
    main()
