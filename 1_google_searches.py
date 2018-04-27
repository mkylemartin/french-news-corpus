""" This script generates google search queries and uses requests to go get
    the HTML from the google search page. This was the most time-consuming
    step in the process. 

    Certain lines are commented out as evidence of debugging and
    to help me remember what I had already done.

    Anyways, this script makes links by week from 2010 to 2016 (included)

    Spits out html files of google searches"""

__author__ = 'Kyle Martin'
__email__ = 'me@mkylemartin.com'

import requests as r
import time
import random

# year_range = range(2014, 2017)
year_range = range(2010, 2013)
month_range = range(1, 13)
weeks = [(1, 7), (8, 14), (15, 21), (22, 28)]

userAgent = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/'
             '537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')

# for week in weeks:
#      print('week ' + str(week) +
#           ' start: ' + str(week[0]) +
#           ' end: ' + str(week[1]))


def get_links(month_range, weeks):
    """
    pass in month and day to write a query that will
    go get all the links on that google search page.
    """
    links = []
    for year in year_range:
        for month in month_range:
            for week in weeks:
                # append to a search_str list
                link_a = ('https://www.google.com/search?q=de&num=100&lr'
                          '=lang_fr&tbs=cdr:1,cd_min:')
                link_b = (str(month) + '/' + str(week[0]) + '/' +
                          str(year) + ',cd_max:' +
                          str(month) + '/' + str(week[1]))
                link_c = '/' + str(year) + ',sbd:1&tbm=nws&cr=countryFR'
                link = link_a + link_b + link_c
                links += [link, ]
    return links


query_list = get_links(month_range, weeks)

""" I used the following lines to track how
    often I was getting blocked by google.
        # 0 - 26 at 10:56 PM mar 15
        # 27 - 48 at 4:38 PM mar 16
        # 48 - 60 at 10:45 AM mar 17
        # stopped at 81 11:52 AM"""
# I had to manually set the index value of my query list whenever the script
# would die out. 
index = 120
for url in query_list[120:len(query_list)]:
    print('GETting {}...'.format(url))
    headers = {'user-agent': userAgent}
    response = r.get(url, headers=headers)
    with open('new-webpages/search_no_' + str(index) + '.txt', 'w+') as f:
        f.write(response.text)
        print('wrote file no. ' + str(index))
    time.sleep(random.uniform(30, 45))
    index += 1
print('done!')
