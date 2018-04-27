""" This script reads in the file of links and prints a
    frequency distribution of the domains to show where the
    articles are coming from. """
__author__ = 'Kyle Martin'
__email__ = 'me@mkylemartin.com'

import re
import operator

re_domain = r'https?://((?:www\.)?.*?\..*?)/'

# open the list of links
links = open('20mar-links.txt', 'r').readlines()

# create a list of domains
domain_list = []
for link in links:
    domain_list.append(re.search(re_domain, link).group(1))

# create a distribution of domains
d_dist = {}
# `d_dist` => {'domain': article count}
for domain in domain_list:
    if domain not in d_dist.keys():
        d_dist[domain] = 1
    else:
        d_dist[domain] += 1

# sort the distribution of domains in `d_dist`
sorted_d_dist = sorted(d_dist.items(),
                       key=operator.itemgetter(1),
                       reverse=True)

# output results
print('{:<50}{:<7}{:<7}'.format('DOMAIN', 'COUNT', 'perc. of articles'))
for k, v in sorted_d_dist:
    p = round(v / len(domain_list), 7)
    print('{:50}{:<7}{:<7}'.format(k, v, p))


print('# of domains: ', len(d_dist.items()))
