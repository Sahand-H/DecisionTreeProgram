import operator as op
import functools
import math

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

'''
Method to create a Geometric random var and assign a PMF to it
n is the number of failures, so given n=2 trials, the first and second are a failure but the third is a success, and
probability that is calculated is the probability of the third trial being a success (or rather, that there are only 2 
failures)
'''
def GeoVar(n,p):
    x = {i: ((1-p)**(n-1))*p for i in [1,n]}
    return x

X = GeoVar(3,0.6)
print(X)

'''
Method to create a Poisson random var with parameter p (lambda) and assign a pmf to it:
ASSUME: P>0
'''
def PoVar(n,p):
    x = {i: ((math.exp(-p))*((p**i)/(math.factorial(i)))) for i in range(n+1)}
    return x

X = PoVar(3,1.5)
print(X)

