import os.path
import requests
import re
from page_loader.loader import download_assets
from urllib.parse import urlparse


#link = 'https://ru.hexlet.io/courses'
def download(link, dir=None):
    html = requests.get(link)
    html = html.text

    filename, ext = url_to_slug_and_ext(link)
    filename = str(filename + ext)
    dirname, _ = url_to_slug_and_ext(link)
    dirname  = str(dirname + '_files')

    full_path = os.path.join(os.getcwd(), dir)
    path = os.path.join(full_path, filename)
    assets_path = os.path.join(full_path, dirname)
    if not os.path.exists(assets_path):
        os.mkdir(assets_path)

    updated_html = download_assets(html, link, dirname, assets_path)

    with open(path, 'w') as f:
        f.write(updated_html)
    return path

def url_to_slug_and_ext(url):
    result_url_parse = urlparse(url)
    path, ext = os.path.splitext(result_url_parse.path)
    return (replace_chars(result_url_parse.netloc + path), ext if ext else '.html')

def replace_chars(s):
    return re.sub(re.compile(r'[^0-9a-zA-Z]+'), '-', s)