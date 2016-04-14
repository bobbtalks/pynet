#!/usr/bin/env python
import yaml
import json

my_list = range(8)
my_list.append('a string')
my_list.append('another string')
my_list.append({})
# print my_list

my_list[-1]['address_group'] = 'remote_networks'
my_list[-1]['hosts'] = ['10.1.1.0/24','10.10.1.0/24']
my_list[-1]['hosts'].append('1.1.1.1') 

print "Printing my list"
print my_list

print "dumping in yaml expanded form"
print yaml.dump(my_list, default_flow_style=False)

with open("yaml_list.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))



print "printing json format"
print json.dumps(my_list)

with open("json_list.json", "w") as f:
    json.dump(my_list, f)
