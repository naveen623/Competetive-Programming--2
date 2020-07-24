# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

def ldt(l):
      c = 1
      lst = list()
      for i in range(l, len(l) + 1):
            if i < len(l) and l[i - 1] == l[i]:
                  c += 1
            else:
                  lst.append((c, l[i - 1]))
                  c = 1
      return lst
def longestdigitrun(n):
      l = list(map(int, str(abs(n))))
      lst = ldt(l)
      x = y = 0
      for i in lst:
            if i[0] > x:
                  x = i[0]
                  y = i[1]
            if i[0] == x and y > i[1]:
                  y = i[1]
      return y
	# Your code goes here
	# pass