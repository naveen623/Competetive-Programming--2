# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
      sp = sum(len(row) for row in L)
      s = set()
      for i in L:
            for j in i:
                  s.add(j)
      if len(s) != sp:
            return True
      else:
            return False
    	
	# Your code goes here
	# pass