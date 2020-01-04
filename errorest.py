import math

h1=4
h2=8
h3=16
h4=32
x=1

def error (num,num2):
 t=num-num2
 print("The error: ", t)

def approx(f,g,h):
 w=(g-f)/(1/h)
 print (w)
 return w

def approx2 (f,g,h):
 w=(f-g)/(2*(1/h))
 print (w)
 return w

print("sqrt(1+x)")
f=math.sqrt(1+x)
g=math.sqrt(x+(1/h1)+1)
r=math.sqrt(x-(1/h1)+1)
e=1/(2*math.sqrt(2))
th=approx(f,g,h1)
error(e,th)

g=math.sqrt(x+(1/h2)+1)
r=math.sqrt(x-(1/h2)+1)
th=approx(f,g,h2)
error(e,th)

g=math.sqrt(x+(1/h3)+1)
r=math.sqrt(x-(1/h3)+1)
th=approx(f,g,h3)
error(e,th)

g=math.sqrt(x+(1/h4)+1)
r=math.sqrt(x-(1/h4)+1)
th=approx(f,g,h4)
error(e,th)

print("\n")
print("Second Derivative Formula: ")

g=math.sqrt(x+(1/h1)+1)
r=math.sqrt(x-(1/h1)+1)
th=approx2(g,r,h1)
error(e,th)

g=math.sqrt(x+(1/h2)+1)
r=math.sqrt(x-(1/h2)+1)
th=approx2(g,r,h2)
error(e,th)

g=math.sqrt(x+(1/h3)+1)
r=math.sqrt(x-(1/h3)+1)
th=approx2(g,r,h3)
error(e,th)

g=math.sqrt(x+(1/h4)+1)
r=math.sqrt(x-(1/h4)+1)
th=approx2(g,r,h4)
error(e,th)

print ("\n")
print("arctanx")
#arctan function
f=math.atan(x)
g=math.atan(x+(1/h1))
r=math.atan(x+(1/h1))
e=1/2
th=approx(f,g,h1)
error(e,th)

g=math.atan(x+(1/h2))
r=math.atan(x-(1/h2))
th=approx(f,g,h2)
error(e,th)

g=math.atan(x+(1/h3))
r=math.atan(x-(1/h3))
th=approx(f,g,h3)
error(e,th)

g=math.atan(x+(1/h4))
r=math.atan(x-(1/h4))
th=approx(f,g,h4)
error(e,th)

print("\n")
print("Second Derivative Formula: ")

g=math.atan(x+(1/h1))
r=math.atan(x+(1/h1))
th=approx2(g,r,h1)
error(e,th)

g=math.atan(x+(1/h2))
r=math.atan(x-(1/h2))
th=approx2(g,r,h2)
error(e,th)

g=math.atan(x+(1/h3))
r=math.atan(x-(1/h3))
th=approx2(g,r,h3)
error(e,th)

g=math.atan(x+(1/h4))
r=math.atan(x-(1/h4))
th=approx2(g,r,h4)
error(e,th)

print("\n")
print("sin(xpi)")
#sin(xpi)
f=math.sin(math.pi*x)
g=math.sin(math.pi*(x+(1/h1)))
r=math.sin(math.pi*(x-(1/h1)))
e=math.pi*math.cos(math.pi)
th=approx(f,g,h1)
error(e,th)

g=math.sin(math.pi*(x+(1/h2)))
r=math.sin(math.pi*(x-(1/h2)))
th=approx(f,g,h2)
error(e,th)

g=math.sin(math.pi*(x+(1/h3)))
r=math.sin(math.pi*(x-(1/h3)))
th=approx(f,g,h3)
error(e,th)

g=math.sin(math.pi*(x+(1/h4)))
r=math.sin(math.pi*(x-(1/h4)))
th=approx(f,g,h4)
error(e,th)

print("\n")
print("Second Derivative Formula: ")

g=math.sin(math.pi*(x+(1/h2)))
r=math.sin(math.pi*(x-(1/h2)))
th=approx2(g,r,h1)
error(e,th)

g=math.sin(math.pi*(x+(1/h2)))
r=math.sin(math.pi*(x-(1/h2)))
th=approx2(g,r,h2)
error(e,th)

g=math.sin(math.pi*(x+(1/h3)))
r=math.sin(math.pi*(x-(1/h3)))
th=approx2(g,r,h3)
error(e,th)

g=math.sin(math.pi*(x+(1/h4)))
r=math.sin(math.pi*(x-(1/h4)))
th=approx2(g,r,h4)
error(e,th)

print("\n")
print("e^-x")
#e^-x
f=math.exp(-x)
g=math.exp(-x+(1/h1))
r=math.exp(-x-(1/h1))
e=-1*e
th=approx(f,g,h1)
error(e,th)

g=math.exp(-x+(1/h2))
r=math.exp(-x-(1/h2))
th=approx(f,g,h2)
error(e,th)

g=math.exp(-x+(1/h3))
r=math.exp(-x-(1/h3))
th=approx(f,g,h3)
error(e,th)

g=math.exp(-x+(1/h4))
r=math.exp(-x-(1/h4))
th=approx(f,g,h4)
error(e,th)

print("\n")
print("Second Derivative Formula: ")
g=math.exp(-x+(1/h1))
r=math.exp(-x-(1/h1))
th=approx2(g,r,h1)
error(e,th)

g=math.exp(-x+(1/h2))
r=math.exp(-x-(1/h2))
th=approx2(g,r,h2)
error(e,th)

g=math.exp(-x+(1/h3))
r=math.exp(-x-(1/h3))
th=approx2(g,r,h3)
error(e,th)

g=math.exp(-x+(1/h4))
r=math.exp(-x-(1/h4))
th=approx2(g,r,h4)
error(e,th)

print("\n")
print("lnx")
#lnx
f=math.log(x)
g=math.log(x+(1/h1))
r=math.log(x-(1/h1))
e=1
th=approx(f,g,h1)
error(e,th)

g=math.log(x+(1/h2))
r=math.log(x-(1/h2))
th=approx(f,g,h2)
error(e,th)

g=math.log(x+(1/h3))
r=math.log(x-(1/h3))
th=approx(f,g,h3)
error(e,th)

g=math.log(x+(1/h4))
r=math.log(x-(1/h4))
th=approx(f,g,h4)
error(e,th)

print("\n")
print("Second Derivative Formula: ")

g=math.log(x+(1/h1))
r=math.log(x-(1/h1))
th=approx2(g,r,h1)
error(e,th)

g=math.log(x+(1/h2))
r=math.log(x-(1/h2))
th=approx2(g,r,h2)
error(e,th)

g=math.log(x+(1/h3))
r=math.log(x-(1/h3))
th=approx2(g,r,h3)
error(e,th)

g=math.log(x+(1/h4))
r=math.log(x-(1/h4))
th=approx2(g,r,h4)
error(e,th)
