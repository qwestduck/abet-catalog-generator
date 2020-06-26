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

Producing a printed document from an web-focused medium requires resolving two major ambiguities:
1. What content should be included in the printed document?
1. What order should the included content be presented in?

These two issues should be answered by either the school or department. To make this specification, the concept of TOC (table of content) files are used.

Table of content files reference one catalog.olemiss.edu document per line. You can view the referenced content in a browser by visiting ```catalog.olemiss.edu/<line_text>```. Most lines identify their content well from text alone--for example--"engineering/computer-science/academics".

Each line in TOC file represents a page from catalog.olemiss.edu that will be included in the generated PDF. The ordering of these lines coincides with the order that the pages from catalog.olemiss.edu will be rendered in the PDF document.

A sample TOC file for a snapshot of the entirety of catalog.olemiss.edu can be viewed at ~/.config/corpus.toc.

A sample user-modified TOC file formed by grepping corpus.toc for the string "engineering" can be viewed at ~/.config/engineering-sample.toc.

The department or school will need to generate this TOC file before an appropriate document can be rendered.

Done:
- Generate a catalog composed of documents in unspecified order

Todo:
- Specify ordering of documents within the catalog **Department input required**
