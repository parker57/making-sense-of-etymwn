#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re
import codecs
import json


#list(set(words_from('eng'))) unique words in English.

with codecs.open('scrubbed.tsv', encoding='utf-8',) as scrubbed:
    tsv = csv.reader(scrubbed, delimiter='\t')
    word_rows = list(tsv)

# Removing orthographic relationships and converting lists to strings
# words = [w[0]+'@#&'+w[2] for w in words if w[1][4:] != 'variant:orthography']
words = []
for wr in word_rows:
    try:
        if wr[1][4:] != 'variant:orthography':
            words.append(wr[0]+'@#&'+wr[2])
    except:
        print('!',wr)
        
# Conversion to strings allows for removing duplicate entries
# Many have the same associations stored in etymology and is_derived_from relations
words = list(set(words))

# Back into original form
words = [w.split('@#&') for w in words]

def languages():
    # Returns list of languages in data
    return list(set([re.search(r'[^:]*', word[0]).group(0) for word in words]))

roots = {}
for l in languages():
    roots[l] = {}

def add_row(row):
    try:
        w = row[0].split(' ',1)[1]
        w_lang = re.search(r'[^:]*', row[0]).group(0)
        rw = row[1].split(' ',1)[1]
        rw_lang = re.search(r'[^:]*', row[1]).group(0)
        if w in roots[w_lang]:
            roots[w_lang][w].append({rw:rw_lang})
        else:
            roots[w_lang][w] = [{rw:rw_lang}]
    except:
        print('!',row)

def write(json_file='etymologies.json'):
    for w in words:
        add_row(w)

    with codecs.open(json_file, 'w', encoding='utf-8') as f:
        json.dump(roots, f)
    

write()


