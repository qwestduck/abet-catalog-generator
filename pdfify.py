#!/usr/bin/python3

import os
import pdfkit

print(f'cwd={os.getcwd()}')

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

if not os.path.exists('.config'):
    os.makedirs('.config')

files = []

if not os.path.exists('.config/corpus.toc') or True:
    with open('.config/corpus.toc', 'w') as f:
        for dirName, subdirList, fileList in os.walk('.cache/catalog.olemiss.edu'):
            for fileName in fileList:
                if fileName.endswith('.html'):
                    stripped_dirName = remove_prefix(dirName, '.cache/catalog.olemiss.edu')
                    stripped_dirName = remove_prefix(stripped_dirName, '/')
                    if stripped_dirName != '':
                        stripped_dirName = f'{stripped_dirName}/'
                    f.write(f'{stripped_dirName}{fileName}\n')

                    files.append(f'{stripped_dirName}{fileName}')

os.chdir('.cache/catalog.olemiss.edu')
pdfkit.from_file(files, '../../catalog.pdf')
