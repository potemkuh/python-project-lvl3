import os.path
import requests
from page_loader.download_asset import download_assets
from page_loader.get_name import get_filename, get_dirname
import logging


def download(link, dir=None):
    html = requests.get(link)
    html.raise_for_status()
    html = html.text

# получение имени файла и дериктории
    filename = get_filename(link)
    dirname = get_dirname(link)

# пути файлов
    full_path = os.path.join(os.getcwd(), dir)
    path = os.path.join(full_path, filename)
    assets_path = os.path.join(full_path, dirname)

    if not os.path.exists(assets_path):
        os.mkdir(assets_path)

    updated_html = download_assets(html, link, dirname, assets_path)

    with open(path, 'w') as f:
        f.write(updated_html)
    print(path)

    logging.info('requested url: {0}'.format(link))
    logging.info('output path: {0}'.format(full_path))
    return path
