#!/usr/bin/python2.7 -Wd

import math
from collections import OrderedDict

print "Open and read an external file:"
f = open('external_file', 'r')
for line in f:
  print line,

##f.close()

print "\nFile to Dictionary:\n"
with open("external_file") as f:
  d = dict(x.rstrip().split(',',1) for x in f)
  print "%s\n" % d

print "\nUn-sorted dictionary keys:\n"
print d.keys()

print "\nUn-sorted dictionary values:\n"
print d.values()

print "\nSorted by dictionary keys:\n"
print OrderedDict(sorted(d.items(), key=lambda t: t[0]))

print "\nSorted by dictionary values:\n"
print OrderedDict(sorted(d.items(), key=lambda t: t[1]))

print "\nSorted dictionary by key length:\n"
print OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))

print "\nSorted dictionary by value length:\n"
print OrderedDict(sorted(d.items(), key=lambda t: len(t[1])))

