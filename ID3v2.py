from bitstring import BitArray
from Frames_constatn_names import FRAMES_NAMES

class ID3v2:
    def __init__(self):
        self.head = None
        self.title = None
        self.artist = None
        self.album = None
        self.year = None
        self.comment = None
        self.track = None
        self.genre = None


    def parse_frames(self, file):
        self.head = ID3v2_head()
        self.head.set_all_information(file)
        counter = 0
        frames = []
        while counter < self.head.int_size:
            try:
                frame = ID3v2_frame()
                frame.set_frame(file)
                frames.append(frame)
                # print(frame.id, frame.size + 10, frame.context)
                counter += 10
                counter += frame.size
            except ValueError:
                break
        self.head.frames = frames

    def parse_info(self, file):
        self.parse_frames(file)
        for frame in self.head.frames:
            if frame.id == 'TIT2':
                self.title = frame.context
            elif frame.id == 'TPE1':
                self.artist = frame.context
            elif frame.id == 'TALB':
                self.album = frame.context
            elif frame.id == 'TYER':
                self.year = frame.context
            elif frame.id == 'COMM':
                self.comment = frame.context
            elif frame.id == 'TRCK':
                self.track = frame.context
            elif frame.id == 'TCON':
                self.genre = frame.context

    def __str__(self):
        info = 'ID3v2 TAG \n' + 'Title: ' + self.title + '\nArtist: ' + self.artist + '\nAlbum: ' + self.album + \
              '\nYear: ' + str(self.year)
        if self.genre != 255:
            info += '\nGenre: ' + str(self.genre)
        else:
            info +='\nGenre: unknown'
        if self.comment != None:
            info += '\nComment: ' + self.comment
        else:
            info += '\nComment: None'
        if self.track != '':
            info += '\nNumber of track: ' + str(self.track)
        else:
            info +=  '\nNumber of track: unknown'
        return info

class ID3v2_head:
    def __init__(self):
        self.sign = None
        self.version = None
        self.sub_version = None
        self.flags = None
        self.int_size = None
        self.frames = None

    def set_all_information(self, file):
        self.set_sign(file.read(3))
        self.set_version(file.read(1))
        self.set_sub_version(file.read(1))
        self.set_flags(file.read(1))
        self.set_size(file.read(4))

    def set_sign(self, sign):
        self.sign = sign.decode()

    def set_version(self, ver):
        self.version  = int.from_bytes(ver, byteorder= 'big')

    def set_sub_version(self, subver):
        self.sub_version = int.from_bytes(subver, byteorder='big')

    def set_flags(self, flags):
        self.flags = int.from_bytes(flags, byteorder= 'big')

    def set_size(self, byte_size):
        self.int_size = self.convert_size_to_int(byte_size)

    def convert_size_to_int(self, byte_size):
        temp = BitArray(bytes = byte_size).bin
        binary_size = ''
        counter = 0
        for i in range(len(temp)):
            if i == counter:
                counter += 8
                continue
            binary_size += temp[i]
        return BitArray(bin = binary_size).int

class ID3v2_frame:
    def __init__(self):
        self.id = None
        self.size = None
        self.flags = None
        self.context = None
        self.frames_names = FRAMES_NAMES

    def set_id(self, bytes):
        self.id = bytes.decode()

    def set_size(self, bytes):
        self.size = int.from_bytes(bytes, byteorder= 'big')

    def set_flags(self, bytes):
        self.flags = int.from_bytes(bytes, byteorder='big')

    def set_context(self, data):
        result = ''
        for e in data:
            if e >= 32 and e <= 126:
                result += chr(e)
            else:
                continue
        self.context = result

    def set_frame(self, file):
        name = file.read(4)
        if name in self.frames_names:
            self.set_id(name)
            self.set_size(file.read(4))
            self.set_flags(file.read(2))
            self.set_context(file.read(self.size))
        else:
            raise ValueError('End of frames')


def main():
    with open('30 Seconds To Mars - This Is War.mp3', 'rb') as file:
        music = ID3v2()
        music.parse_info(file)
        print(str(music))


if __name__ == '__main__':
    main()