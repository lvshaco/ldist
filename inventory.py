#!/usr/bin/env python

import argparse
try:
    import json
except ImportError:
    import simplejson as json

def gen(cfg):
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action = 'store_true')
    parser.add_argument('--host', action = 'store')
    args = parser.parse_args()

    if args.list:
        r = cfg
    elif args.host:
        r = {'_meta': {'hostvars': {}}}
    else:
        r = {'_meta': {'hostvars': {}}}
    print json.dumps(r)
