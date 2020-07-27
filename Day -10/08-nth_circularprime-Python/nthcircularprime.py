# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(n):
      if n > 1:
            for i in range(2,n):
                  if n % i == 0:
                        return False
            return True

def iscircularprime(n):
      i = 0
      c = 0
      if n < 10:
            if isprime(n):
                  return True
            return False
      l = len(str(n))
      while i < l:
            rem = n % 10
            n = n // 10
            n = int((rem * (10 ** (l - 1)) + n))
            if isprime(n):
                  c += 1
            i += 1
      if c == l:
            return True
      return False

def nthcircularprime(n):
      c = 2
      i = 3
      if n == 1:
            return 2
      while True:
            if iscircularprime(i):
                  if c == n:
                        return i
            i += 1
            c +=1
	# Your code goes here
	# pass