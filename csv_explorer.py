import csv
import re
from collections import Counter

# TODO: It would be VERY good to keep the orthographic relationships
# ^woule be essential for anlaysis of pre-lexicographic texts

with open("scrubbed.tsv") as scrubbed:
    tsv = csv.reader(scrubbed, delimiter='\t')
    words = list(tsv)

# Removing orthographic relationships
words = [w for w in words if w[1][4:] != 'variant:orthography']

def languages():
    # Returns list of languages in data
    return list(set([re.search(r'[^:]*', word[0]).group(0) for word in words]))

def by_lang():
    # All languages and number of entries therein
    return Counter([re.search(r'[^:]*', word[0]).group(0) for word in words])

# Retreive a list of all entries in any given language
of_lang = lambda lang : [word for word in words if re.search(r'[^:]*', word[0]).group(0)==lang]

# Retreive words ONLY from a given language
words_from = lambda lang: [w[0].split(' ',1)[1] for w in of_lang(lang)]

def relations():
    # Returns list of relationships in data
    return list(set([rel[1][4:] for rel in words]))

def word_counter(lang='eng'):
    # Counts the words in a given language
    return(len([word for word in words if re.search(r'[^:]*', word[0]).group(0)==lang]))

def by_relation(rows = words, relationship='variant:orthography'):
    # Returns words with any given relation
    # The three relations are variant:orthogrpahy, etymology, and is_derived_from
    return [[word[0],word[2]] for word in rows if word[1][4:] == relationship]


def print_by_lang():
    cumulative = 0
    total = len(words)
    d = by_lang()
    langs = sorted(d, key=d.get, reverse=True)
    for lang in langs:
        cumulative += d[lang]
        perc = cumulative/total * 100
        perc = str(perc)[:5] + '%'
        print(perc, lang,', +', str(d[lang]), 'words')


