import os.path
import requests
from page_loader.download_asset import download_assets
from page_loader.get_name import get_filename, get_dirname
import logging


def download(url, output_path=None):
    response = requests.get(url)
    response.raise_for_status()
    logging.info('requested url: {0}'.format(url))

    # получение имени файла и дериктории
    filename = get_filename(url)
    dirname = get_dirname(url)

    # пути файлов
    full_path = os.path.join(os.getcwd(), output_path)
    path_file = os.path.join(full_path, filename)
    assets_path = os.path.join(full_path, dirname)

    if not os.path.exists(assets_path):
        os.mkdir(assets_path)

    updated_html = download_assets(response.text, url, dirname, assets_path)

    with open(path_file, 'w') as f:
        f.write(updated_html)
    logging.info('output path: {0}'.format(full_path))
    return path_file
