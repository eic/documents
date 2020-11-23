#!/usr/bin/env python3

import yaml

print("hello")
with open("zenodo_keywords.yml", 'r') as stream:
    items = None
    try:
        items = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print(items)

