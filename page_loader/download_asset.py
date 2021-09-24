from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import requests
from page_loader import loader
import os


def download_assets(html, url, dirname, assets_path):
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.find_all('img')
    for source_tag in tag_list:
        attribute_name = 'src'
        short_asset_url = source_tag.get(attribute_name)
        full_asset_url = urljoin(url + '/', short_asset_url)
        filename, ext = loader.url_to_slug_and_ext(full_asset_url)
        filename = str(filename + ext)
        full_asset_path = os.path.join(assets_path, filename)
        download_files(url, full_asset_path)
        source_tag[attribute_name] = os.path.join(dirname,  filename )

    return soup.prettify(formatter="html5")

def download_files(url, full_asset_path):
    response = requests.get(url, stream=True)
    save_file(response.content, full_asset_path)


def save_file(data, path):
    with open(path, 'wb') as f:
        f.write(data)