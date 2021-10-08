from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests, os
from page_loader import get_name
from progress.bar import Bar



def download_assets(html, url, dirname, assets_path):
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.find_all(['img', 'link', 'script'])
    bar = Bar('Processing', max=len(tag_list))
    for source_tag in tag_list:
        attribute_name = find_attribute(source_tag.name)
        short_asset_url = source_tag.get(attribute_name)
        full_asset_url = urljoin(url + '/', short_asset_url)
        filename, ext = get_name.url_to_slug_and_ext(full_asset_url)
        if urlparse(full_asset_url).netloc == urlparse(url).netloc:
            filename = str(filename + ext)
            full_asset_path = os.path.join(assets_path, filename)
            download_files(full_asset_url, full_asset_path)
            source_tag[attribute_name] = os.path.join(dirname, filename)
        bar.next()
    bar.finish()

    return soup.prettify()


def download_files(url, full_asset_path):
    response = requests.get(url, stream=True)
    save_file(response.content, full_asset_path)


def save_file(data, path):
    with open(path, 'wb') as f:
        f.write(data)


def find_attribute(tag):
    if tag == 'link':
        return 'href'
    if tag == 'script':
        return 'src'
    if tag == 'img':
        return 'src'
