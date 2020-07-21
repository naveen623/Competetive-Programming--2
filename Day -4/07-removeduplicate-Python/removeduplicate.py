# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.
# from collections import OrderedDict
def removeduplicate(text):
      l = list()
      for i in text:
            if i in l:
                  continue
            l.append(i)
      return "".join(l)
    	# return "".join(OrderedDict.fromkeys(text))
	# Your code goes here
	# pass