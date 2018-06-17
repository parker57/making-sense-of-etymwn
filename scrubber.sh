#!/bin/bash

# Bash script to partially scrub the original .tsv file

# Remove all phrases for all languages (should maybe do just for English)
grep -vE ": \w+ \w+|: [[:alnum:][:punct:]]* " $1 > no_phrases.tsv
echo "Removed phrases"

# Standardize relations
sed -in "s/rel:derived/rel:is_derived_from/;
	s/rel:etymologically	/rel:etymology	/" no_phrases.tsv
echo "Standardized relations"

# Get rid of one random troll new line character
sed -in "s/ang:  sǣliglic	rel:is_derived_from	ang: sælig/ang: sǣliglic	rel:is_derived_from	ang: sælig/" no_phrases.tsv
echo "Not today Anglo-Saxons :^)"

# Remove unhelpful categories
grep -vE 'rel:has_derived_form|rel:etymological' no_phrases.tsv > scrubbed.tsv
echo "Removed unhelpful categories"

# Remove no_phrase files
rm no_phrases.tsv*

