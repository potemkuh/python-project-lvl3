from page_loader.loader import download
from page_loader.parser import parse


def main():
    args = parse()
    download(args.url, args.output)

if __name__ == '__main__':
    main()