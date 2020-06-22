#!/usr/bin/python3

import os
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

rootDir = '.'

env = Environment(loader=FileSystemLoader('../templates'))
template = env.get_template('document.j2')

for dirName, subdirList, fileList in os.walk(rootDir):
    for fileName in fileList:
        with open(f'{dirName}/{fileName}') as f:
            soup = BeautifulSoup(f, 'html.parser')
            main_content = soup.select('#main-content')[0].prettify()

            print(template.render(main_content=main_content))