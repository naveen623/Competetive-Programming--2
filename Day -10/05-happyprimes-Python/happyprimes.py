# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def sumOfSquaresOfDigits(n):
    sum = 0
    while n > 0:
        rem = n % 10
        sum += rem * rem
        n = n // 10
    return sum

def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isHappyNumber(n):
    l = list()
    while True:
        if n == 1:
            return True
        if n == 4:
            return False
        if n not in l:
            print(n)
            l.append(n)
            x = sumOFSquaresOfDigits(n)
            print(n)
        else:
            return False

def ishappyprimenumber(n):
    if isHappyNumber(n) and isprime(n):
        return True
    return False
    # Your code goes here
    pass