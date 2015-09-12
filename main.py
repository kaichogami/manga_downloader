import argparse
from core import download

class main:

    def __init__(self):
        self.args = self.get_argument()

    def get_argument(self):
        ap = argparse.ArgumentParser()
        ap.add_argument('-d', nargs = 3,required = True, help = "-d <manga_name> <start chapter> <end_chapter> NOTE: in manga name, put '_' instead of space")
        args = ap.parse_args()
        return args.d

    def download(self):
        d = download.download(self.args[0], self.args[1], self.args[2])

        d.start_download()

if __name__ == '__main__':
    m = main()
    m.download()
