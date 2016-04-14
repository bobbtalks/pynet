#!/usr/bin/env python
import yaml
import json
from pprint import pprint as pp

with open ("yaml_list.yml") as f:
    yaml_list = yaml.load(f)

print "\nprinting yaml list from file yaml_list.yml"
pp(yaml_list)

with open("json_list.json") as f:
    json_list = json.load(f)

print "\nprinting json list from file json_list.json\n"
pp(json_list)
