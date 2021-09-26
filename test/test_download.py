from posixpath import join
from typing import FrozenSet
from page_loader.loader import download
from page_loader.download_asset import download_assets
from page_loader.get_name import url_to_slug_and_ext
import tempfile
import os


url = 'https://www.google.com/'

def test_download():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_path = os.path.join(temp_dir, 'ru-hexlet-io-courses.html')
        assert download(url, temp_dir) ==  test_path

def test_download():
    with tempfile.TemporaryDirectory() as temp_dir:
        download_assets_path = os.path,join(temp_dir, 'www-google-com-_files')
        assert download_assets(html, url, 'www-google-com-_files', download_assets_path) ==  open('test/fixture/download_asset', 'r').read()