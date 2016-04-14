#!/usr/bin/env python
import yaml

my_list = range(8)
my_list.append('a string')
my_list.append('another string')
my_list.append({})
# print my_list

my_list[-1]['address_group'] = 'remote_networks'
my_list[-1]['hosts'] = ['10.1.1.0/24','10.10.1.0/24']
my_list[-1]['hosts'].append('1.1.1.1') 

print my_list

print "dumping my yaml list"
print yaml.dump(my_list)

print "dumping in expanded form"
print yaml.dump(my_list, default_flow_style=False)


