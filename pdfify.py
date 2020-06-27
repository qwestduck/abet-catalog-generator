#!/usr/bin/python3

import os
import pdfkit

from jinja2 import Environment, FileSystemLoader

print(f'cwd={os.getcwd()}')

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

if not os.path.exists('.config'):
    os.makedirs('.config')

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('document.j2')

files = []

# Generate TOC for complete corpus if it does not yet exist
if not os.path.exists('.config/corpus.toc'):
    print('Generating initial .config/corpus.toc')
    with open('.config/corpus.toc', 'w') as f:
        for dirName, subdirList, fileList in os.walk('.cache/catalog.olemiss.edu'):
            for fileName in fileList:
                if fileName.endswith('.html'):
                    stripped_dirName = remove_prefix(dirName, '.cache/catalog.olemiss.edu')
                    stripped_dirName = remove_prefix(stripped_dirName, '/')
                    if stripped_dirName != '':
                        stripped_dirName = f'{stripped_dirName}/'
                    f.write(f'{stripped_dirName}{fileName}\n')


# Build file list from TOC
with open('.config/computerScience-2020.toc') as f:
    files = f.readlines()

# Remove newline characters from filenames
files = [l.strip('\n\r') for l in files]

# Render cover
with open('.cache/cover.html', 'w') as f:
    f.write(template.render(
        main_content=""""
        <h1>University of Mississippi<br>
        School of Engineering<br>
        2020 Catalog</h1>
        """
    ))

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'outline-depth': 2
}

print('Generating document catalog.pdf. This will take on the order of minutes.')
os.chdir('.cache/catalog.olemiss.edu')
pdfkit.from_file(files, '../../catalog.pdf', options=options, cover='../cover.html')
