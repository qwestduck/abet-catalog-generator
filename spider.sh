#!/bin/bash

mkdir -p cache
cd cache

wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --domains catalog.olemiss.edu \
     --exclude-directories "/20*" \
     --reject '*.pdf' \
     --no-parent \
        https://catalog.olemiss.edu/

# python3 squash-index.py