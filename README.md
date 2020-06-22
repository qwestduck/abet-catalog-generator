# Roadmap

## Spider catalog.olemiss.edu

This is by far the best task to focus optimization efforts on. Naive approaches can take a week to retrieve a corpus.

Implemented optimizations:
- Omit PDFs
- Do not crawl external to catalog.olemiss.edu
- Do not crawl catalog.olemiss.edu/(\d\d\d\d)

Todo:
- 303 See Other should be symlinks

## Resolve directory layout quirks

- Rename sibling documents
- Remove bad nodes

## Lint content

- Remove references to external documents

## Map document content onto a template

- Write a satisfactory stylesheet

## Convert to PDF

```wkhtmltopdf cover derpy.html toc --xsl-style-sheet default.xsl rarity.html twilight.html spike.html equestriadaily.pdf```