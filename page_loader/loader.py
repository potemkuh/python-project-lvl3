from os import name
import os.path
import requests
import re

link = 'https://ru.hexlet.io/courses'
def download(link, dir=None):
    if dir is None:
        dir =   os.getcwd()
    html = requests.get(link)
    html = html.text

    url = link.replace("https://", "")
    file_name = re.sub(r'[/.]', '-', url) + '.html'
    path = os.path.join(dir, file_name)
    with open(path, 'w') as f:
        f.write(html)
    return path
