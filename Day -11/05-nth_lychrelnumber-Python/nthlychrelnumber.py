# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def reverse(n):
      x = 0
      while n > 0:
            rem = n % 10
            x = (x * 10) + rem
            n = n // 10
      return x

def isLychrel(n):
      for i in range(20):
            n = n + reverse(n)
            if n == reverse(n):
                  return False
      return True
    			
def nthlychrelnumbers(n):
      c = 0
      i = 196
      while True:
            if isLychrel(i):
                  c += 1
                  if c == n:
                        return i
            i += 1
	# your code goes here
	# pass