""" This script takes the list of downloaded html articles from the golang
    script and removes all the boilerplate and returns just the text """
__author__ = 'Kyle Martin'
__email__ = 'me@mkylemartin.com'

from glob import glob
import time
import justext

# a file with all the links
PAGE_GLOB = glob('/Users/Kyle/desktop/corpus-linguistics/'
                 'french-news-html/goscraper/20mar-links/*')
# this is a super cute counter, hi there little guy!
i = 1

print('Loaded corpus directectory.\n')


def get_text(page):
    """This function takes an html page from a glob, for exmaple,
       and reads it and uses the justext module remove all boilerplate"""

    # reads the file
    page_string = open(page, 'rb').read()
    # creates a justext object
    paragraphs = justext.justext(page_string,
                                 justext.get_stoplist("French"))
    pageText = ''
    # if not boilerplate, adds to `pageText`
    for p in paragraphs:
        if not p.is_boilerplate:
            pageText += p.text + ' '
    return pageText


def thou_counter(i):
    """a little counter that only does cool stuff """
    thousands = [num * 1000 for num in range(0, 26)]
    if i in thousands:
        print(i)

# This made me feel really official to push enter: https://gph.is/28LijSn
input('press [enter] to create corpus file')
print('creating corpus file . . .')
with open('french-news-corpus.txt', 'w+') as corpus:
    for page in PAGE_GLOB:
        article = get_text(page)
        corpus.write(article)
        corpus.write('\n\n')
        print('.', end='', flush=True)  # show progress; print 1 dot per file
        thou_counter(i)
        i += 1
