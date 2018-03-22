#!/usr/bin/python2.7
# Import all required libraries
import json
import hashlib
from time import strftime
from utils import config

import json

location_brahms_dump = config.get('location_brahms_dump')
jsondumpfile = open(location_brahms_dump, "r")
for line in jsondumpfile:
    a = json.loads(line)
    unique_id = a[u'unitID'] + '@BRAHMS'
    a[u'id'] = unique_id
    hash = hashlib.md5(json.dumps(a)).hexdigest()
    timestamp = strftime('%Y-%m-%d %H:%M:%S')
    print(hash)
