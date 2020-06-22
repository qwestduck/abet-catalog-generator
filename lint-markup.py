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
            main_content = soup.select('#main-content')[0]

            for a in main_content.find_all('a', href=True):
                if a['href'].startswith("http"):
                    a.unwrap()

            for a in main_content.find_all('a', href=False):
                a.unwrap()

            print(template.render(main_content=main_content.prettify()))