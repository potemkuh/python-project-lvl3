from page_loader.loader import download
from page_loader.parser import parse
import logging
import sys


def main():
    args = parse()
    logging.basicConfig(level=logging.INFO)
    logging.info('Start download')
    try:
        filepath = download(args.url, args.output)
        print(f"Page was downloaded as '{filepath}'")
    except Exception as e:
        logging.critical(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
