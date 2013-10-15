#!/usr/bin/python2.7
'''
gets mean profit from prices
counts to 18 while comparing numbers
determines if a list is really a list

## TT 20130923
from math import sqrt

static = 12

a=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']

# profit = revenue - cost
prices=[50, 35, 16, 23, 10, 5, 12, 42, 27]

mean = sum(prices) /len(prices)
print "mean: %s\n" % mean

def Profit(prices):
    bestProfit = 0;
    for i in range(0, len(prices)):
        for j in range (i + 1, len(prices)):
            bestProfit = max(bestProfit, prices[j] - prices[i])

    return bestProfit

print "bruteforce profit:", Profit(prices)

print "\nSimple counter:\n"
for i in a:
  if i != '%s' % static:
    print "%s is not %s\n" % (i,static)
  elif i == '%s' % static:
    print "%s is %s\n" % (i,static)
  
print "List comprehension:"
print "found", a.count('12'), "number which equals %s\n" % static
print "%s is" % a, len(a), "items long\n"
print "List append:"
b=len(a)+1
a.append(b)
print "Updated length of 'a' is:", len(a)

print "\nIs %s a list?" % a
if list(a):
  print "Yes, %s" % a, "is a list\n"
else:
  print "No, %s" % a, "is not a list\n"

