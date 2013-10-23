#!/usr/bin/python2.7 -Wd

import math
from collections import OrderedDict

print "Open and read an external file:"
f = open('external_file', 'r')
#print "There %s lines in %s" % (counter,f) 
for line in f:
  print "%s" % line

print "\nFile line counts:\n"
with open("external_file") as f:
  lines = sum(1 for line in f)
  print "There are %s lines\n" % lines

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

f.close()
