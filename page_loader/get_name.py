from urllib.parse import urlparse
import re
import os


def url_to_slug_and_ext(url):
    if url.endswith('/'):
        url = url[:-1]
    result_url_parse = urlparse(url)
    path, ext = os.path.splitext(result_url_parse.path)
    return (replace_chars(result_url_parse.netloc + path),
            ext if ext else '.html')


def replace_chars(string):
    return re.sub(re.compile(r'[^0-9a-zA-Z]+'), '-', string)


def get_filename(url):
    filename, ext = url_to_slug_and_ext(url)
    return str(filename + ext)


def get_dirname(url):
    dirname, _ = url_to_slug_and_ext(url)
    return str(dirname + '_files')
