# etymology-and-derivation-dataset
Trying to make sense of Gerard de Melo's etymological wordnet
***

# Obtaining and scrubbing the data
The source of the original data can be found [here](http://www1.icsi.berkeley.edu/~demelo/etymwn/), I am using the "2013-02-08" version, the .tsv for which is 298.76 MB.
***

# Exploring and Scrubbing the data
The file of tab seperated values does not feature a header and consists of three columns (all containing key-value pairs). 

The first and third columns store an ISO 639-3 code for a language and a corresponding word therein; the second column stores the relationship between the first and third word in any given row.
```console
$ head etymwn.tsv 
aaq: Pawanobskewi	rel:etymological_origin_of	eng: Penobscot
aaq: senabe	rel:etymological_origin_of	eng: sannup
abe: waniigan	rel:etymological_origin_of	eng: wangan
abe: waniigan	rel:etymological_origin_of	eng: wannigan
abs: beta	rel:etymological_origin_of	zsm: beta
adt: yuru	rel:etymological_origin_of	eng: euro
afr: -heid	rel:etymological_origin_of	afr: moontlikheid
afr: -ig	rel:etymological_origin_of	afr: denkbeeldig
afr: -ig	rel:etymological_origin_of	afr: tydig
afr: -ing	rel:etymological_origin_of	afr: verbuiging
```

The file initially contained 6031431 rows/entries.
```console
$ wc -l etymwn.tsv 
6031431 etymwn.tsv
```

There are only eight unique relationships in the second column with there being apparent symmetry in the relations 'is_derived_from' and 'has_derived_form' as well as 'etymology' and 'etymological_origin_of'.
```console
$ grep -o "rel:[a-Z_]*" etymwn.tsv | sort | uniq -c | sort -nr
2264744 rel:is_derived_from
2264744 rel:has_derived_form
 538558 rel:etymologically_related
 473433 rel:etymology
 473433 rel:etymological_origin_of
  16516 rel:variant
      2 rel:derived
      1 rel:etymologically
```

In exploring the data, it became evident that being primarily constructed from wiktionary many entries referenced phrases, not words, 172765 entries concern english phrases - a sample of which are shown.

While these are interesting, they add considerable complexity to working with this dataset, for this they've been scrubbed.

Words are nice and atomic and while it is unfortunate to lost information on multiple word nouns such as Kuala Lumpur and Hong Kong, the etmology of many of these phrases such as 'thank you' or 'sit down' should be easily inferred by looking at the constituent words.
```console
$ grep -E 'eng: \w+ \w+' etymwn.tsv && !! | wc -l
...
tpi: sindaun	rel:etymology	eng: sit down
tpi: singaut	rel:etymology	eng: sing out
tpi: tenkyu	rel:etymology	eng: thank you
tpi: tumas	rel:etymology	eng: too much
tpi: watpo	rel:etymology	eng: what for
tur: Kuala Lumpur	rel:etymology	eng: Kuala Lumpur
...
yid: אוי וויי	rel:etymological_origin_of	eng: oy vey
yid: באבע מעשה	rel:etymological_origin_of	eng: bubbe meise
yid: געפֿילטע־פֿיש	rel:etymological_origin_of	eng: gefilte fish
yue: baahk báai	rel:etymological_origin_of	eng: pak pai
yue: 雜碎	rel:etymological_origin_of	eng: chop suey
yue: 飲茶	rel:etymological_origin_of	eng: yum cha
yue: 香港	rel:etymological_origin_of	eng: Hong Kong
yxg: dili	rel:etymological_origin_of	eng: dilly bag
zsm: Big Mac	rel:etymology	eng: Big Mac
172765
```

All instances of the variant relationships between words are orthographic.
```console
$ grep "rel:variant" no_phrases.tsv | wc -l
16516
$ grep "rel:variant:orthography" no_phrases.tsv | wc -l
16516
```

eytmologically_related does not seem like a helpful relationship as the following command bears testament to.
Such relationships might be helpful if trying to graph the entire English language.
```console
$ grep -E "eng: \w+   rel:etymologically_related" etymwn.tsv
...
eng: Americanization	rel:etymologically_related	eng: American
eng: Americanization	rel:etymologically_related	eng: Americanize
eng: Americanize	rel:etymologically_related	eng: Americanism
eng: Americanize	rel:etymologically_related	eng: Americanization
...
eng: France	rel:etymologically_related	eng: Franco-
eng: France	rel:etymologically_related	eng: Francophilia
eng: France	rel:etymologically_related	eng: Francophobia
eng: France	rel:etymologically_related	eng: Francophone
eng: France	rel:etymologically_related	eng: Frankland
eng: France	rel:etymologically_related	eng: French
eng: France	rel:etymologically_related	eng: Frenchman
eng: France	rel:etymologically_related	eng: New France
eng: France	rel:etymologically_related	eng: Tour de France
eng: France	rel:etymologically_related	eng: francophobe
```

Further analysis revealed phrases that contain punctuation weren't identified using the previous regex and so survived the culling, but it's all right :^)
```console
$ grep "eng: [a-Z'\.-]* " scrubbed.tsv
...
eng: iron-sulphur cluster	rel:is_derived_from	eng: sulfur
eng: it's a jungle out there	rel:is_derived_from	eng: jungle
eng: it's a matter of time	rel:is_derived_from	eng: time
eng: it's a question of time	rel:is_derived_from	eng: time
eng: it's about time	rel:is_derived_from	eng: time
eng: it's all Greek to me	rel:is_derived_from	eng: Greek
eng: it's all grist to the mill	rel:is_derived_from	eng: grist
eng: it's all right	rel:is_derived_from	eng: right
...
```
