# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

l = list()
def powers3(number):
      if number > 1 and number % 3 == 0:
            return powers3(number // 3)
      elif n == 1:
            return True
      return False


def recursion_powersof3ton(n):
      n = int(n)
      if n > 0:
            global l
            if powers3(n):
                  l.append(n)
            else:
                  return recursion_powersof3ton(n - 1)
      elif len(l) > 0:
            x = sorted(l)
            l = list()
            return x
      return None
    	
	# Your code goes here
	# pass
