#!/bin/bash

rm -rf .cache
mkdir -p .cache

# Crawl only if there is not a local corpus archive
if [ ! -f "corpus.tar.gz" ]; then
    # Spider catalog.olemiss.edu
    cd .cache

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

    # Archive corpus
    echo "Compressing corpus..."
    tar zcf ../corpus.tar.gz * && cd ..

    rm -rf .cache
    mkdir -p .cache
fi

# Build cache from corpus archive
cd .cache
echo "Decompressing corpus..."
tar xzf ../corpus.tar.gz
cd ..

python3 pipeline.py
