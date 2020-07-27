# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def istidy(n):
    n = str(n)
    x = sorted(list(map(int, n)))
    oc = ""
    for i in x:
        oc += str(i)
    return n == oc


def fun_nth_tidynumber(n):
    c = -1
    i = 1
    while True:
        if istidy(i):
            c += 1
            if c == n:
                return i
        i += 1
    # return 0