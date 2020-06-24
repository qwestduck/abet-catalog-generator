#!/usr/bin/python3

import os
import shutil

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

def file_contains_string(fileName, string):
    with open(fileName) as f:
        if string in f.read():
            return True

    return False

def purge_404_content(root):
    pattern = 'Page not found'

    counter = 0

    for dirName, subdirList, fileList in os.walk(root):
        for fileName in fileList:
            if file_contains_string(f'{dirName}/{fileName}', pattern):
                counter = counter + 1
                os.remove(os.path.join(dirName, fileName))

    print(f'Removed {counter} soft-404 content pages')

def squash_index():
    rootDir = '.'
    os.chdir('.cache/catalog.olemiss.edu')
    print(f'cwd={os.getcwd()}')

    # Remove bad nodes
    bad_files = ['robots.txt.html']
    bad_dirs = ['css', 'js']

    for i in bad_dirs:
        shutil.rmtree(i)

    for i in bad_files:
        os.remove(i)

    for dirName, subdirList, fileList in os.walk(rootDir):
        for subdir in subdirList:
            if f'{subdir}.html' in fileList:
                # Rename sibling documents
                print(f'{subdir} has a sibling document in {dirName}')

                sibling_name_old = f'{dirName}/{subdir}.html'
                sibling_name_new = f'{dirName}/{subdir}/index.html'

                os.rename(sibling_name_old, sibling_name_new)

    os.chdir('..')

def lint_markup():
    rootDir = '.'
    print(f'cwd={os.getcwd()}')

    file_counter = 0
    chunk_counter = 0

    env = Environment(loader=FileSystemLoader('../templates'))
    template = env.get_template('document.j2')

    for dirName, subdirList, fileList in os.walk(rootDir):
        for fileName in fileList:
            file_counter = file_counter + 1
            if file_counter == 100:
                chunk_counter = chunk_counter + 1
                file_counter = 0
                print(f'Periodic render update: {dirName}/{fileName} ({chunk_counter}/{155} chunks)')

            with open(f'{dirName}/{fileName}') as f:
                soup = BeautifulSoup(f, 'html.parser')

            # Retrieve primary content region from document (excluding headers, footers, navigation, etc)
            main_content = soup.select('#main-content')[0]

            # Remove references to external documents
            for a in main_content.find_all('a', href=True):
                if a['href'].startswith("http"):
                    a.unwrap()

            for a in main_content.find_all('a', href=False):
                a.unwrap()

            with open(f'{dirName}/{fileName}', 'w') as f:
                f.write(template.render(main_content=main_content.prettify()))

def main():
    purge_404_content('.cache/catalog.olemiss.edu')
    squash_index()
    lint_markup()


if __name__ == "__main__":
    main()
