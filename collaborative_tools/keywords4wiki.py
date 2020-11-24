#!/usr/bin/env python3

import argparse
import yaml

# Example:
#{| class="wikitable"
#|-
#! style="text-align:left;"|Keyword
#!|Description
#|-
#|EIC
#|Electron-Ion Collider
#|}

#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i", "--input", required=True, help="the input file with keywords (YAML)")
    parser.add_argument("-c", "--category", required=False, help="the category to be selected")
    args = parser.parse_args()

    items = None
    with open(args.input, 'r') as stream:
        try:
            items = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    output='''
{| class="wikitable"
|-
! style="text-align:left;"|Keyword
!|Description
'''
    names = []
    for item in items:
        if ((args.category is None) or (item['category']==args.category)):
            names.append(item['name'])

        names.sort()
    for name in names:
        for item in items:
            if(item['name']!=name): continue
            output+="|-\n|%s\n|%s\n" % (item['name'], item['description'])
    
    output+="|}\n"
    print(output)
    
