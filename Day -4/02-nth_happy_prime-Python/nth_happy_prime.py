# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def squares(n):
      sum = 0
      while n > 0:
            r = n % 10
            sum += r * r
            n = n // 10
      return sum

def ishappynumber(n):
      l = list()
      if n == 1:
            return True
      elif n > 0:
            while True:
                  n = squares(n)
                  if n == 1:
                        return True
                  elif n in l:
                        return False
                  else:
                        l.append(n)
      else:
            return False

def isprime(n):
      if n > 1:
            for i in range(2, n // 2):
                  if n % i == 0:
                        return False
                  else:
                        return True
    					 

def fun_nth_happy_prime(n):
      c = 0
      i = 1
      if n > 0:
            while count != n + 1:
                  while True:
                        i += 1
                        if ishappynumber(i) and isprime(i):
                              break
                  c += 1
            return i
      else:
            return 7
	# return 0