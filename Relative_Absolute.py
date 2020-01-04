import math

def approx(n):
 ans=2*math.pi*n
 ans=math.sqrt(ans)
 ans2=n/math.e
 ans2=math.pow(ans2,n)
 ans= ans*ans2
 return ans

def absol(x,y):
 x=(-1)*(x-y)
 return x

def rela(x,y):
 x=x/y
 return x

for x in range (1,11):
 real=math.factorial(x)
 print(x)
 x=approx(x)
  abserr=absol(x,real)
 print(abserr)
 relerr=rela(abserr,real)
 print(relerr)
 print(x)
