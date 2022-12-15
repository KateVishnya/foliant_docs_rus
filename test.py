import re
import urllib
from shutil import rmtree
from io import StringIO
from hashlib import md5
from pathlib import Path
from subprocess import run, CalledProcessError, PIPE, STDOUT

from foliant.preprocessors.base import BasePreprocessor
from foliant.preprocessors import escapecode
from foliant.meta.tools import remove_meta

url = 'https://raw.githubusercontent.com/foliant-docs/foliantcontrib.admonitions/master/README.md'
repo_url = 'https://github.com/foliant-docs/foliantcontrib.admonitions'
path = 'path/to/doc.md'
revision = 'master'
incl = '<include repo_url="https://github.com/foo/bar.git" path="path/to/doc.md"></include>'

def full_link(repo_url: str, path: str, revision: str):

    if repo_url.endswith('.git'):
        repo_url = repo_url[:-4]
    
    repo_url=repo_url+'/tree/'+revision+ '/'+path.rpartition('/')[0]

    print(repo_url)

def create_link_repo_url(repo_url:str):
    dict_new_link = {}
    regexp_find_link = re.compile('\[.+?\]\(.+?\)')
    regexp_find_path = re.compile('\(.+?\)')

    old_found_link = regexp_find_link.findall(downloaded_content)

    for line in old_found_link:
        exceptions_simbols = re.findall(r'http|@|:',line)
        if exceptions_simbols:
            continue
        else:
            relative_path = regexp_find_path.findall(line)
            sub_relative_path = re.findall(r'\[.+?\]', line)
            dict_new_link[line] = sub_relative_path[0] + '(' + repo_url + '/' + relative_path[0].partition('(')[2]

    for line in dict_new_link:
        downloaded_content = downloaded_content.replace(line, dict_new_link[line])

def create_link_url(url):
    dict_new_link = {}
    regexp_find_link = re.compile('\[.+?\]\(.+?\)')
    regexp_find_path = re.compile('\(.+?\)')

    old_found_link = regexp_find_link.findall(downloaded_content)

    for line in old_found_link:
        exceptions_simbols = re.findall(r'http|@|:',line)
        if exceptions_simbols:
            continue
        else:
            relative_path = regexp_find_path.findall(line)
            sub_relative_path = re.findall(r'\[.+?\]', line)
            dict_new_link[line] = sub_relative_path[0] + '(' + url.rpartition('/')[0].replace('raw', 'blob')+'/'+ relative_path[0].partition('(')[2]

    for line in dict_new_link:
        downloaded_content = downloaded_content.replace(line, dict_new_link[line])

full_link(repo_url, path, revision)