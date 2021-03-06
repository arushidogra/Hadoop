#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

max=0
for line in sys.stdin:
    data_mapped = line.strip().split()
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        #print oldKey, "\t", salesTotal
        if(oldKey!='/'):
            if(salesTotal>max):
               max=salesTotal
               index=oldKey

        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += 1

if oldKey!=None:
   if(salesTotal>max):
      max=salesTotal
      index=oldKey

print index, "\t", max
