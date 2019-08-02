#!/usr/bin/python

# CMS TLV file to JSON converter, 2019-07-04/pro cabales

import re
import sys
import json

for line in sys.stdin:
    # print line
    workArray = line.split('id=')   # data separator

    valueMap = {}

    for S in workArray:

        if re.search(r'type=.+\s+route', S):
            # handle type and route fields
            for y in S.split(' '):
                tmp = y.split('=')
                valueMap.update({ tmp[0] : tmp[1] })
        else:
            # use the id as keys, then value as values
            m = re.search('(.+)len=.+value=(.+)', S)

            if m:
                valueMap.update({ m.group(1) :  m.group(2) })

    # handle encoding issue
    try:
        print json.dumps(valueMap, sort_keys=True)
    except UnicodeDecodeError:
        print json.dumps(valueMap, sort_keys=True, encoding='ISO-8859-1')
