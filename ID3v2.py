import Constants
import TextHandlers

class ID3v2:
    def __init__(self):
        self.header = None
        self.version = None
        self.subversion = None
        self.flags =None
        self.size = None
        self.frames = None

    def parse_file(self, file):
        file.seek(0,0)
        head = file.read(10)
        self.header = head[0:3].decode('iso-8859-1')
        self.version = int.from_bytes(head[3:4], byteorder='big')
        self.subversion = int.from_bytes(head[4:5], byteorder='big')
        self.set_flags(head[5:6])
        self.set_size(head[6:])
        self.set_frames(file)

    def set_flags(self, info):
        temp = bin(int.from_bytes(info, byteorder='big'))
        self.flags = ''
        if temp[:1] == 'a':
            self.flags += 'Unsynchronisation '
        if temp[1:2] == 'b':
            self.flags += 'Extended header '
        if temp[2:3] == 'b':
            self.flags += 'Experimental indicator '


    def set_size(self, info):
        result = []
        for i in range(4):
            result.append(bin(int(info[i]))[2:].zfill(7))
        self.size = int(''.join(result), 2)

    def set_frames(self, file):
        file.seek(10, 0)
        frames = []
        counter = 0
        while counter < self.size:
            frame = Frame()
            try:
                frame.set_tag(file.read(4))
            except ValueError as e:
                break
            frame.set_size(file.read(4))
            frame.set_flags(file.read(2))
            frame.set_text(file.read(frame.size))
            print(frame.tag, frame.text)
            frames.append(frame)
            counter += 10 + frame.size
        self.frames = frames

    def __str__(self):
        info = 'ID3v2 TAG'+'\nVersion: ' + str(self.version) + '\nSubversion: ' + str(self.subversion) + \
               '\nFlags: ' + str(self.flags) + '\n'
        for e in self.frames:
            info+= e.tag + ' ' + Constants.TAG_NAMES_TO_DESCRIPTION[e.tag] + ' :' + e.text + '\n'
        return info


class Frame:
    def __init__(self):
        self.tag = None
        self.size = None
        self.flags = None
        self.text = None
        self.text_handler = None

    def set_tag(self, info):
        temp = info.decode('iso-8859-1')
        if temp in Constants.TAG_NAMES_TO_DESCRIPTION.keys():
            self.tag = temp
        else:
            raise ValueError('End of frames')

    def set_size(self, info):
        self.size = int.from_bytes(info, byteorder='big')

    def set_flags(self, info):
        self.flags = int.from_bytes(info, byteorder='big')

    def set_text(self, info):
        if self.tag in TextHandlers.tag_to_handler:
            h = TextHandlers.tag_to_handler[self.tag]
            self.text = h(info)
        else:
            self.text = TextHandlers.default_handler(info)


def main():
    a = ID3v2()
    with open('30 Seconds To Mars - This Is War.mp3', 'rb') as file:
        a.parse_file(file)


if __name__ == '__main__':
    main()