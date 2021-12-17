import os
import wget
import requests


OBO_URL = 'https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/main/src/ontology/doid.obo'


def download(url=OBO_URL, out=None):
    wget.download(url, out=out)


def get_iter_lines(obo_file=None):
    obo_file = obo_file or OBO_URL
    if os.path.isfile(obo_file):
        return open(obo_file)
    print(f'request from url: {obo_file}')
    resp = requests.get(obo_file, stream=True)
    return resp.iter_lines(decode_unicode=True)


def parse_version(lines):
    for line in lines:
        linelist = line.strip().split(': ', 1)
        if linelist[0] == 'data-version':
            version = linelist[1].split('/')[1]
            return version


def parse_term(lines):
    term = {}
    for line in lines:
        linelist = line.strip().split(': ', 1)
        if linelist[0] == '[Term]':
            if term:
                yield term
                term = {}
        elif linelist[0] == 'id':
            term['id'] = linelist[1]
        elif linelist[0] == 'name':
            term['name'] = linelist[1]
        elif linelist[0] == 'def':
            term['def'] = linelist[1]
        elif linelist[0] == '[Typedef]':
            yield term
            break
    

if __name__ == "__main__":
    lines = get_iter_lines()
    print('data version:', parse_version(lines))

    download()
    lines = get_iter_lines('doid.obo')
    print('data version:', parse_version(lines))
