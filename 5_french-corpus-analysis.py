""" This file analyzes the french news corpus and spits out the number
    of times `de nouveau` and `à nouveau` were used. """
__author__ = 'Kyle Martin'
__email__ = 'me@mkylemartin.com'

import operator
import re
import spacy
print('Loading spacy..')
nlp = spacy.load('fr')


def word_tagger(phrase_tup):
    """ uses spacy to tag words in phrase for pos
        returns a list of tuples:
        [(tok, pos_tag), (tok, pos_tag), (tok, pos_tag)]"""
    annotated_phrase = []
    for token in phrase_tup:
        spacy_word = nlp(token)
        try:
            pos_tag = spacy_word[0].pos_
        except IndexError:
            # print(phrase)
            # print(f'This is the token that threw an error >{token}<')
            pos_tag = token
        annotated_phrase.append((token, pos_tag))
    return annotated_phrase


def phrase_tagger(list_of_phrases, phenom):
    """ `phenom` is a string of the pattern being measured
        Takes a `list_of_phrases` that `my_re` returns then
        Calls `word_tagger` on every phrase
        prints a cute message about its findings.
        `tagged_phrases` is a list of tagged tuple lists
        e.g. `[[phrase], [phrase], [phrase]]`
        where `phrase` equals: `[(word, tag), (word, tag), (word, tag)]`"""
    tagged_phrases = []
    for phrase_tup in list_of_phrases:
        single_tagged_phrase = []
        tuple_list = word_tagger(phrase_tup)
        [single_tagged_phrase.append(tuple) for tuple in tuple_list]
        tagged_phrases.append(single_tagged_phrase)
    phrase_cnt = len(tagged_phrases)
    print(f'Found and tagged {phrase_cnt} instances of {phenom}.')
    return tagged_phrases


def first_word_pos_distribution(tagged_phrases):
    """ takes a list of tagged phrases and calculates the distribution
        (in a dictionary) of the words that occur before `(à|de) nouveau`
        Returns a sorted frequency list."""
    dist = {}
    for phrase in tagged_phrases:
        # getting all the parts of speech for each phrase.
        #   0      1          2          3     4
        # ['AUX', 'à or de', 'nouveau', 'DET', '']
        # the [0] on the end gets the word that occurs before à/de nouveau
        pos = [wordPair[1] for wordPair in phrase][0]
        if pos not in dist.keys():
            dist[pos] = 1
        else:
            dist[pos] += 1
    sorted_dist = sorted(dist.items(),
                         key=operator.itemgetter(1),
                         reverse=True)
    return sorted_dist


def print_dist(distribution):
    """ takes the sorted distribution of the first word and prints it. """
    print('-' * 40)
    print('{:<10}{}'.format('POS', 'COUNT'))
    for k, v in distribution:
        print(f'{k:<10}{v}')

print('Opening and reading in corpus file...')
corpus = open('french-news-corpus.txt', 'r').read()
print('Corpus opened!')

print('\n`re.findall` is searching 24 million '
      'tokens... this might take a sec--')
print('Enjoy a gif: \n   - http://gph.is/2dlFDfo\n')

# regex captures anything that happens around the following pattern
#     `anything` de|à   nouveau `anything`
my_re = r'(\w+) (de|à) (nouveau)(?: (\w+)|(\W))'
matches = re.findall(my_re, corpus, flags=re.IGNORECASE)
print('Example Matches:')
print(matches[:20], sep='\n')
print()

print('filtering à and de...')
à = [match for match in matches if match[1] == 'à']
de = [match for match in matches if match[1] == 'de']

print('tagging phrases...')
à_tagged = phrase_tagger(à, 'à')
de_tagged = phrase_tagger(de, 'de')

print('Example tagged sentences')
print(à_tagged[:25])

dist_of_à = first_word_pos_distribution(à_tagged)
dist_of_de = first_word_pos_distribution(de_tagged)

print('Dist of `à`:')
print_dist(dist_of_à)
print('Dist of `de`:')
print_dist(dist_of_de)
