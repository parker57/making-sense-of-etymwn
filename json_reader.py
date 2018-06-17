#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def loader():
    with open('etymologies.json') as f:
        return json.load(f)

e = loader()

roots = lambda word: e['eng'][word]

print(roots('seen'))
