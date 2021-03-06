import requests
from datetime import datetime

from gxpkgd_python.utils import parse_pkg


def github_handler(url):

    def get_pkg(author, name):
        url = 'https://raw.githubusercontent.com/{}/{}/master/gerbil.pkg'.format(author, name)
        r = requests.get(url).text # strip leading ( and ending )\n and split between spaces
        return r

    def get_license(author, name):
        url = 'https://api.github.com/repos/{}/{}/license'.format(author, name)
        r = requests.get(url).json()
        return r['license']['spdx_id']

    def get_forks(author, name):
        url = 'https://api.github.com/repos/{}/{}/forks'.format(author, name)
        r = requests.get(url).json()
        return [{'login': i['owner']['login'], 'name': i['name'], 'html_url': i['html_url']} for i in r]

    # [i['owner']['login'], i['name'], i['html_url']] for i in data
    # Retrieve the metadata from github and return a dict
    urlinfo = url.split('/')
    author = urlinfo[3]
    name = urlinfo[4]
    last_updated = str(datetime.now())
    try:
        license = get_license(author, name)
        forks = get_forks(author, name)
        meta = parse_pkg(get_pkg(author, name))
    except Exception as e:
        return e
    return {
        'author': author,
        'name': name,
        'license': license,
        'last_update': last_updated,
        'description': meta['description:'] if 'description:' in meta.keys() else 'Package has no description.',
        'runtime': meta['runtime:'] if 'runtime:' in meta.keys() else 'No runtime specified.',
        'repo': url
    }, forks


