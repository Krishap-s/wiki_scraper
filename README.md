# Wiki Scraper

Scraps data from wikipedia pages and stores data in an object.

## Import project

''' from scrapper import scrap '''

## Create Scrapped page

''' WikiPage = scrap.scrapWikiPage(topic) '''

## Get a list of subsections

''' print(WikiPage.section_names) '''

## Get text stored in section

''' WikiPage.text '''

## Get subsection object

''' subsection = Wikipage.getSection(section_name)

