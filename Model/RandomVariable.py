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
p = probability of the success event
'''
def BernVar(p):
    x = {0: (1-p), 1: p}
    return x

X = BernVar(1/2)
print(X)
