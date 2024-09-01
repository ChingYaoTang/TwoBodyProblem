from math import sin;from math import cos;from math import e
def h(t):
    return e**(-t/4)*(cos(15**(1/2)*t/4)+1/15**(1/2)*sin(15**(1/2)*t/4))
def g(t):
    return e**(-t/4)*((-1/4)*(cos(15**(1/2)*t/4)+1/15**(1/2)*sin(15**(1/2)*t/4))+-(15)**(1/2)/4*sin(15**(1/2)*t/4)+1/4*cos(15**(1/2)*t/4))
v=0 ; x=1 ; m=1 ; k=1 ; c=0.5 ; n=100 ; h=0.01 #v(0)=0;x(0)=1
def f(x,y):
    return -((c/m)*y+(k/m)*x)
def g(x,)
def k1(h,f,x,y):
    return h*f(x,y)
def k2(h,f,x,y):
    return h*f(x+h/2,y+k1(h,f,x,y)/2)
def k3(h,f,x,y):
    return h*f(x+h/2,y+k2(h,f,x,y)/2)
def k4(h,f,x,y):
    return h*f(x+h,y+k3(h,f,x,y))



print("%5s,%10s,%10s,%10s,%10s,%10s"%("t","x(anal)","x(Euler)","x(RK4)","v(anal)","v(num)"))
#print("%5.2f,%10.4f,%10.4f,%10.4f,%10.4f,%10.4f"%(0,h(0),x,x,g(0),v))
for i in range(1,n+1):
    z=x
    t=i*h
    x=x+h*v#x(i+1)=x(i)+h*v(i)
    v=v+h*-((c/m)*v+(k/m)*z)#v(i+1)=v(i)+h*v'(i)
    k1 = f(t, state)
    k2 = f(t+h/2, state+h/2*k1)
    k3 = f(t+h/2, state+h/2*k2)
    k4 = f(t+h,  state+h*k3)
    state += h/6 * (k1 + 2*k2 + 2*k3 + k4)
    w=state[0]
    print("%5.2f,%10.8f,%10.8f,%10.8f,%10.8f"%(t,h(t),x,g(t),v))
