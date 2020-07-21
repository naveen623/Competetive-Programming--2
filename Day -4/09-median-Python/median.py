# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
      if len(a) == 0:
            return None
      if len(a) % 2 == 0:
            return (a[len(a)//2 - 1] + a[len(a)//2]) / 2
      else:
            return a[(len(a) - 1) // 2]
    	
	# your code goes here
	# pass