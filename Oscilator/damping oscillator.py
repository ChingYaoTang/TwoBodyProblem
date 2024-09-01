from numpy import sin;from numpy import cos;from numpy import e;from numpy import array
def a(t):
    return e**(-t/4)*(cos(15**(1/2)*t/4)+1/15**(1/2)*sin(15**(1/2)*t/4))
#def g(t):
#    return e**(-t/4)*((-1/4)*(cos(15**(1/2)*t/4)+1/15**(1/2)*sin(15**(1/2)*t/4))+-(15)**(1/2)/4*sin(15**(1/2)*t/4)+1/4*cos(15**(1/2)*t/4))
v=0 ; x=1 ; m=1 ; k=1 ; c=0.5 ; n=200 ; h=0.01 #v(0)=0;x(0)=1
state=[1,0]
def f(t, state):
     [x, dx] = state
     y = dx #dx/dt==y
     dy = -((c/m)*dx+(k/m)*x)
     return array([y,dy])
print("%5s,%15s,%15s,%15s"%("t","x(anal)","x(Euler)","x(RK4)"))
print("%5.2f,%15.8f,%15.8f,%15.8f"%(0,a(0),x,state[0]))
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
    print("%5.2f,%15.8f,%15.8f,%15.8f"%(t,a(t),x,state[0]))
