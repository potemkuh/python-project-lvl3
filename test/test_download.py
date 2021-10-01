from requests import request
from page_loader.loader import download
from page_loader.download_asset import download_assets
import tempfile
import os
from urllib.parse import urljoin


ASSETS = [
    {
        'url_path': '/blog/about/assets/styles.css',
        'file_name': 'site-com-blog-about-assets-styles.css',
    }]
BASE_URL = 'http://site.com/'
URL = 'http://site.com/blog/about.html'
file_and_dir_name = 'site-com-blog-about'



def test_download(requests_mock):
    for asset in ASSETS:
        asset_url = urljoin(BASE_URL, asset['url_path'])
        asset_path = os.path.join(os.getcwd(),
                                  'test',
                                  'fixture',
                                  'site-com-blog-about_files',
                                  asset['file_name'],
                                  )
        with open(asset_path, 'rb') as file:
            asset_content = file.read()
        requests_mock.get(asset_url, content=asset_content)
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(get_path('init-site-com-blog-about.html'),
                  'r') as test_page:
            test_content = test_page.read()
        requests_mock.get(URL, text=test_content)
        test_path = os.path.join(temp_dir, file_and_dir_name + '.html')
        file_path = download(URL, temp_dir)
        assert file_path == test_path
        for asset in ASSETS:
            asset_path = os.path.join(
                temp_dir,
                file_and_dir_name + '_files',
                asset['file_name'],
                )
            with open(asset_path, 'rb') as asset_file:
                asset_content = asset_file.read()
                with open(os.path.join(os.getcwd(),
                                    'test',
                                    'fixture',
                                    'site-com-blog-about_files',
                                    asset['file_name']), 'rb') as test_file:
                    test_asset_file = test_file.read()
                    assert asset_content == test_asset_file    


def get_path(filename):
    return os.path.join(os.getcwd(), 'test', 'fixture', filename)
