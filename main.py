import sys
import downloader


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        downloader.download(args[0])
    else:
        print("Either no argument was provided or more than expected are provided!")
