import os
import shutil

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

def squash_index():
    rootDir = '.'

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

def lint_markup():
    rootDir = '.'

    env = Environment(loader=FileSystemLoader('../templates'))
    template = env.get_template('document.j2')

    for dirName, subdirList, fileList in os.walk(rootDir):
        for fileName in fileList:
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

            print(template.render(main_content=main_content.prettify()))

def main():
    squash_index()
    lint_markup()


if __name__ == "__main__":
    main()