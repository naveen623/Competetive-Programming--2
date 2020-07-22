# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def is_prime(n):
      for i in range(2, n):
            if n % i == 0:
                  return False
            else:
                  return True


def fun_nth_additive_prime(n):
      if n == 0:
            return 2
      c = 0
      i = 3
      
      while c != n:
            if is_prime(i):
                  sum = 0
                  temp = i
                  while temp != 0:
                        r = temp % 10
                        s += r
                        temp = temp // 10
                  if is_prime(sum):
                        c += 1
                  if c == n:
                        return i
                        
            i += 1
      return False