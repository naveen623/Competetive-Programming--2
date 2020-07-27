# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def kaprekar(n):
    if n == 1:
        return 1
    oc = n * n
    c = 0
    while oc != 0:
        c += 1
        oc //= 10
    oc = n * n

    for i in range(1, c):
        Avi = int(math.pow(10,i))
        if Avi == n:
            continue
        x = int(oc/Avi) + int(oc % Avi)
        if x == n:
            return True
    return False

def fun_nth_kaprekarnumber(n):
    c = 0
    i = 9
    if n == 0:
        return 1
    while True:
        if kaprekar(i):
            c += 1
            if c == n:
                return i
        i += 1