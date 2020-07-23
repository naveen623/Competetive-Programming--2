# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.
sum = 0
def even(n, s):
      if n > 0:
            rem = n % 10
            if rem % 2 == 0:
                  s = s + rem * pow(10, len(str(s)))
            n = n // 10
            return even(n, s)
      else:
            r = s // 10
            s = 0
            return r
		

def fun_recursion_onlyevendigits(l):
      for i in range(len(l)):
            l[i] = even(l[i], s)
      return l
    	
		# return []