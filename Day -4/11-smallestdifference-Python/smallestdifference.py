# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
      if len(a) == 1:
            return a[0]
      elif len(a) > 0:
            l = sorted(a)
            a = l[1] - l[0]
            for i in range(1, len(l) - 1):
                  a1 = l[i + 1] - l[i]
                  if a > a1:
                        a = a1
            return a
      else:
            return -1
	# Your code goes here
	# pass