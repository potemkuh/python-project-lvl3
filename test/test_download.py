from page_loader.loader import download
import tempfile
import os
from urllib.parse import urljoin
import pytest
from page_loader.get_name import (
    url_to_slug_and_ext,
    replace_chars,
    get_filename,
    get_dirname
)


ASSETS = [
    {
        'url_path': '/blog/about/assets/styles.css',
        'file_name': 'site-com-blog-about-assets-styles.css',
    },
    {
        'url_path': '/photos/me.jpg',
        'file_name': 'site-com-photos-me.jpg',
    },
    {
        'url_path': '/assets/scripts.js',
        'file_name': 'site-com-assets-scripts.js',
    },
    {
        'url_path': '/blog/about',
        'file_name': 'site-com-blog-about.html',
    },
]
BASE_URL = 'http://site.com'
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
                asset['file_name'],)
            with open(asset_path, 'rb') as asset_file:
                asset_content = asset_file.read()
                with open(os.path.join(
                            os.getcwd(),
                            'test',
                            'fixture',
                            'site-com-blog-about_files',
                    asset['file_name']), 'rb') as test_file:
                    test_asset_file = test_file.read()
                    assert asset_content == test_asset_file    


def get_path(filename):
    return os.path.join(os.getcwd(), 'test', 'fixture', filename)


def test_url_to_slug_and_ext():
    assert url_to_slug_and_ext(BASE_URL) == ('site-com', '.html')


def test_replace_chars():
    assert replace_chars(BASE_URL) == 'http-site-com'


def test_error_dirname():
    with pytest.raises(Exception):
        assert download(URL, '/download')


@pytest.mark.parametrize('code', [403, 404, 500, 501, 502])
def test_errors_response(requests_mock, code):
    url = 'http://test_site.test/' + str(code)
    requests_mock.get(url, status_code=code)
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(Exception):
            assert download(url, temp_dir)


def test_dir_name():
    assert get_dirname(BASE_URL) == 'site-com_files'


def test_file_name():
    assert get_filename(BASE_URL) == 'site-com.html'
