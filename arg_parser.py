from argparse import ArgumentParser

class ArgParser(ArgumentParser):
    def __init__(self):
        ArgumentParser.__init__(self, prog="MP3 Parser", description="Gives you information about mp3 file")
        self.add_argument("-p", "--parse", action="store_true", default=True, help="Parse all mp3 file")
        self.add_argument("-v1", "--ID3v1", action="store_true", help="Parse ID3v1 tag in mp3 file")
        self.add_argument("-v2", "--ID3v2", action="store_true", help="Parse ID3v2 tag in mp3 file")
        self.add_argument("-f", "--file", action="store", nargs=1, help="Write here path to your mp3 file")

    def parse_arguments(self):
        arg = self.parse_args()
        return self.get_settings(arg)

    def get_settings(self, arg):
        file_name = arg.file[0]
        commands = []
        if arg.ID3v1:
            commands.append('parse tag1')
        if arg.ID3v2:
            commands.append('parse tag2')
        if arg.parse:
            commands.clear()
            commands.append('parse')
        if file_name is not None:
            return file_name, commands
        else:
            raise Exception("No file path")
