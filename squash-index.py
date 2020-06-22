#!/usr/bin/python3

import os

rootDir = '.'

bad_files = ['robots.txt.html']
bad_dirs = ['css', 'js']

for dirName, subdirList, fileList in os.walk(rootDir):
    for subdir in subdirList:
        if f'{subdir}.html' in fileList:
            print(f'{subdir} has a sibling document in {dirName}')
            
            sibling_name_old = f'{dirName}/{subdir}.html'
            sibling_name_new = f'{dirName}/{subdir}/index.html'

            os.rename(sibling_name_old, sibling_name_new)
