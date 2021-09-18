from page_loader import download


def test_download():
    data = download('https://ru.hexlet.io/courses', 'var/tmp')
    assert data == 'var/tmp/ru-hexlet-io-courses.html'
