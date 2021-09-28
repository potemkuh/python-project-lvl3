from page_loader.loader import download
from page_loader.parser import parse
import logging
import sys


def main():
    try:
        args = parse()
        logging.basicConfig(level=logging.INFO)
        logging.info('Start download')
        download(args.url, args.output)
    except:
        sys.exit(1)

if __name__ == '__main__':
    main()