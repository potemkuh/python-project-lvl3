import os.path
import requests


'''
    link = os.path.split(link)
    link = link[0].replace('https://', '') + '-' + link[1]
    file = link.replace('.', '-')
    return dir + '/' + file + '.html'
'''


dir = 'download_html'
link = 'https://ru.hexlet.io/courses'
def path(link):
    link = os.path.split(link)
    link = link[0].replace('https://', '') + '-' + link[1]
    file = link.replace('.', '-')
    return file + '.html'


def download(link, dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
    l = requests.get(link)
    html = l.text
    file = path(link)
    with open(file, 'w') as f:
        for index in html:
            f.write(index)


