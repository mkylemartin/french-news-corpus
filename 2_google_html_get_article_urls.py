""" This script can be placed in a directory of downloaded google searches
    and will get all the links to actual websites out of each file.

    Then it takes all of those links and writes them to a file which can
    be passed into the golang script of awesomeness."""
__author__ = 'Kyle Martin'
__email__ = 'me@mkylemartin.com'

import re
from glob import glob
""" I executed this script from the directory containing 
    all downloaded google searches which I saved as a .txt file instead of 
    HTML. I no longer remember why I chose .txt over .html"""
webpage_list = glob('*.txt')

link_re = r'<h3 .*?<a .*?href="(.*?)"'

links = []
for webpage in webpage_list:
    with open(webpage, 'r') as file:
        raw_html = file.read()
        links += re.findall(link_re, raw_html)

with open('news-story-links.txt', 'w+') as f:
    for link in links:
        print(link, file=f)