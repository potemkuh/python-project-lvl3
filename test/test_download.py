from page_loader.loader import download
import tempfile
import os


def test_download():
    url = 'https://ru.hexlet.io/courses'
    with tempfile.TemporaryDirectory() as temp_dir:
        test_path = os.path.join(temp_dir, 'ru-hexlet-io-courses.html')
        assert download(url, temp_dir) ==  test_path