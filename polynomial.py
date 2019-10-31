class Polynomial:
    def __init__(self,*args):
        self.x = list(args)

    def compute(self,list,xo,func):
        x = 0
        for i in range(len(list)):
            x += func(list,xo,i,n=len(self.x)-i-1)


        return x

    def epsilon(self):
        epsilon = 1.0
        r = 1.0 + epsilon
        while r > 1.0:
            epsilon = epsilon / 2.0
            r = 1.0 + epsilon
        return epsilon

def generateFunctionAns(a,xo,i,n):
        if(n==0):
            return (a[i])*(xo)**(0)
        else:
            return (a[i])*(xo)**(n)




p = Polynomial(1,-3.0,4.0,-2.0)
def bisection(a,b,p):
    r = p.compute(p.x,a,generateFunctionAns) * p.compute(p.x,b,generateFunctionAns)
    if (r > 0.0):
        print("No root in the interval (",a,",",b,")")
    else:
        m =  float((a+b)/2.0)
        proceed = True
        while(proceed):
            r =  p.compute(p.x,a,generateFunctionAns) * p.compute(p.x,m,generateFunctionAns)
            if(r < 0.0):
                b = m
            else:
                a = m

            print(m)

            mnew = float((a+b)/2.0)
            m2 = mnew - m
            if(m2 <10.0 * p.epsilon() and m2 > 0.0):
                proceed = False

            m = mnew
        return m


from math import exp
def f(x):
    return exp(x) - x


def bisection_V2(a,b):
    r = f(a) * f(b)
    if (r > 0.0):
        print("No root in the interval (",a,",",b,")")
    else:
        m =  float((a+b)/2.0)
        proceed = True
        while(proceed):
            r =  f(a) * f(m)
            if(r < 0.0):
                b = m
            else:
                a = m

            print(m)

            mnew = float((a+b)/2.0)
            m2 = mnew - m
            if(m2 <10.0 * p.epsilon() and m2 > 0.0):
                proceed = False

            m = mnew
        return m

print(bisection_V2(0.0,1.0))

def Regula_Falsi(a,b):
    num =  (a * f(b) )-(f(a) * b)
    denum = (f(b) - f(a))
    w = float(num/denum)
    return w
