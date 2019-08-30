#!/usr/bin/python3

import json
import re
from pprint import pprint


data= json.load(open("/home/fsx/.cf/config.json"))

#pprint(data)

target = str(data["Target"].lstrip('https://'))


regex = re.compile('^api\.(cfy)\.(.*)\.(geo)0\.(your\.domain\.name)$')
regSearch = regex.search(target)

new_regex = re.compile('^api\.cf\.(geo)\.(your\.domain\.name)$')
newRegSearch = new_regex.search(target)

if regSearch:
    env = regSearch.groups()[1]
    shortDatacenter = regSearch.groups()[3]
else:
    env="prod"
    shortDatacenter = newRegSearch.groups()[0]

if shortDatacenter == 'm' or shortDatacenter == 'mts':
    datacenter = 'MTS'
elif shortDatacenter == 'b' or shortDatacenter == 'bgl':
    datacenter = 'BGL'
elif shortDatacenter == 's' or shortDatacenter == 'sph':
    datacenter = 'SPH'


org = data["OrganizationFields"]["Name"]
space = data["SpaceFields"]["Name"]

print (target+' '+env+' '+datacenter+' '+org+' '+space)
