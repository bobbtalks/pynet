#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

crypt = cisco_cfg.find_objects(r"^crypto map CRYPTO")

# Printing each list item that begins with crypto map CRYPTO and their children entries
for item in crypt:
    print "Printing each item"
    print item
    for child in item.children:
        print child.text

#9 Find all of crypto map entries that are using PFS group2
print "\n Finding all group2"
group2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

for item in group2:
    print item
    for child in item.children:
        print child.text

aes = cisco_cfg.find_objects(r"crypto ipsec transform-set AES")
print "\n Printing all AES Transform Sets"
for item in aes:
    print item
    for child in item.children:
        print child.text
