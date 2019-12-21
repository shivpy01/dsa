
'''
def rec(n):
    if n == 0:
        return 0
    return n + rec(n-1)

print(rec(4))




def sum_func(n):
    if n < 10:
        return n
    return n%10+sum_func(n//10)

print(sum_func(4321))

''' 

def reverse(s):
    
    if len(s)<=1:
        return s
    
    else:
        m = len(s)//2
        return reverse(s[m:]) + (reverse((s[:m])))

print(reverse('hello world'))


