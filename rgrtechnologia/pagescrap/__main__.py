import sys
import os

from pagescrap import init_app

list_urls = []
local_path = 'result.json'

if os.path.exists(local_path):
    os.remove(local_path)

if not sys.stdin.isatty():
    for i in sys.stdin.readlines():
        list_urls.append(i.replace('\n', ''))
else:
    raise ValueError('URL list is empty, please check the entry')

if list_urls is None:
    raise ValueError('URL list is empty, please check the entry')

init_app(list_urls)

with open(local_path, 'r') as file:
    print(file.read())
