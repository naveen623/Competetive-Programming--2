# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

def is_prime(n):
      for i in range(2, n):
            if n % i == 0:
                  return False
            else:
                  return True
    	

def fun_hasnoprimes(l):
      for i in l:
            for j in i:
                  if is_prime(j):
                        return False
      return True
    	
	# return True

