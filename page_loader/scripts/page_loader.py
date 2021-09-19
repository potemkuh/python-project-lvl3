from loader import download
from parser import parse


def main():
    args = parse()
    download(args.url, args.output)

if __name__ == '__main__':
    main()