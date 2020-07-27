# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def isautomorphic(n):
      st = n * n
      while n > 0:
            if n % 10 != st % 10:
                  return False
            n //= 10
            st //= 10
      return True 

def nthautomorphicnumbers(n):
      i = 0
      c = 0
      while True:
            if isautomorphic(i):
                  c += 1
                  if c == n:
                        return i
            i += 1
    	
	# Your code goes here
	# pass