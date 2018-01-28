import operator as op
import functools
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = functools.reduce(op.mul, range(n, n-r, -1))
    denom = functools.reduce(op.mul, range(1, r+1))
    return numer//denom

class RandomVariable(object):
        def __init__(self,type):
            self.type = type
            self.parameter = parameter

'''
Method to create a uniform random variable and assign a PMF to it
note: n is the interval [a,n) starting with a zero index
'''
def UniformVar(n):
    x = {x: (1/n) for x in range(n)}
    return x

X = UniformVar(3)
print(X)

'''
Method to create a bernoulli random var and assign a PMF to it
p = probability of the success event.
'''
def BernVar(p):
    x = {0: (1-p), 1: p}
    return x

X = BernVar(1/2)
print(X)

'''
Method to create a binomial random var and assign a PMF to it
uses the ncr method copied from https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
'''
def BinVar(n,p):
    x = {i: ((ncr(n,i))*(p**i)*((1-p)**(n-i))) for i in range(n+1)}
    return x

X = BinVar(4,0.5)
print(X)
