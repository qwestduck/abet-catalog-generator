# Roadmap

## ABET requirements

- Self-referencing (no links to external content)
- Printable in physical document form

## Spider catalog.olemiss.edu

This is by far the best task to focus optimization efforts on. Naive approaches can take a week to retrieve a corpus.

Done:
- Omit PDFs
- Do not crawl external to catalog.olemiss.edu
- Do not crawl catalog.olemiss.edu/(\d\d\d\d) (catalogs from previous years)
- Crawl only if there is not a local corpus archive

Todo:
- 303 See Other should be symlinks

## Resolve directory layout quirks

Done:
- Rename sibling documents
- Remove bad nodes
- Remove soft-404 content

## Lint content

Done:
- Remove references to external documents

## Map document content onto a template

Done:
- Retrieve primary content region from document (excluding headers, footers, navigation, etc)

Todo:
- Write a satisfactory stylesheet

## Convert to PDF

Done:
- Generate a catalog composed of documents in unspecified order

Todo:
- Specify ordering of documents within the catalog **Department input required**
