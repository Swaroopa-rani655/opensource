def rev(n):
    INT_MIN= -2**31
    INT_MAX= 2**31-1
    neg=n<0
    if neg:
        n=-n
    rev_n=int(str(n)[::-1])
    if neg:
        rev_n= -rev_n
    if rev_n<INT_MIN or rev_n>INT_MAX:
        return 0
    return rev_n
n=int(input())
print(rev(n))
