#!/usr/bin/env python


import random
# gives a random number between the two specified
#r = random.randint(1,100)
#print r

nums = range(0,100,10)
print nums

key = 40
lo = nums[0]
hi = len(nums)

print lo, hi

while lo < hi:   
    mididx = (lo + hi)/2
    mid = nums[mididx]
    print "Checking in the range [%d, %d] mididx[%d]=%d" % (lo, hi, mididx, mid)
    if (mid == key):
        print "Hooray, found it at %d" % (mididx)
        break
    elif (key > mid):
        lo = mididx + 1
    else:
        hi = mididx
    
    
    #print "scanning the %dth number is %d" % (i, v)
