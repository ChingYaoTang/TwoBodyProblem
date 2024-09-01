from visual import *;from numpy import cos,sin
from visual.graph import *;import matplotlib.pyplot as plt
#graph of stars motion
scene = display()
scene.background = (0.2,0.3,0.4)
scene.title = "one body"
scene.forward = vector(0, 0, -1)
#graph of energy
gd=gdisplay(x=600,y=0,width=1000,height=700)
fK=gcurve(color=color.blue)
fU=gcurve(color=color.yellow)
fE=gcurve(color=color.red)

G = 6.7e-11
r1 = 1.5e11
#initial position
x2 = -r1/2 ; x1 = r1
#initial velocity
v1 = 3.3e+4
star2 = sphere(pos= vector(x2, 0, 0), radius=0)
star1 = sphere(pos= vector(x1, 0, 0), radius=0)
m2 = 4e+30 ; m1 = 2e+30
p1 = vector(0, 1.*v1, 0)*(m1) ; p2 = -p1
mu=m1*m2/(m1+m2)#reduce mass
M = sphere(pos = star1.pos-star2.pos, radius=r1*0.1,
               color= color.white, make_trail= True, trail_type= "curve")
L=x1*mag(p1)+-x2*mag(p2)#angular momentum(conserve)
center = sphere(pos= vector(0, 0, 0), color= color.white, make_trail= True, trail_type= "points")

#initial condition
r=mag(M.pos)
rd=((mag(p1)**2/(2*m1)+mag(p2)**2/(2*m2)-L**2/(2*mu*r**2))*2/mu)**(1/2)
phi=0
state=[r,rd,phi]
k=1#k=0.93           ####answer of Ex5, change the power of distance, to change potential(interaction) form.

#runge-kutta method
def f(t, state):
     [r, rd, phi] = state
     R = rd
     Rd = -k*G*m1*m2/(mu*r**(k+1))+L**2/(mu**2*r**3)
     phid = L/(mu*r**2)
     return array([R, Rd, phid])

E=[];U=[];K=[];d=[];T=[];h = 5000;t=0;n=0
#while n<1:
for n in range(8*10**4):
    rate(5000)
    k1 = f(t,state)
    k2 = f(t+h/2, state+h/2*k1)
    k3 = f(t+h/2, state+h/2*k2)
    k4 = f(t+h,  state+h*k3)
    state += h/6 * (k1 + 2*k2 + 2*k3 + k4)
    t += h
    M.pos = (state[0]*cos(state[2]),state[0]*sin(state[2]),0)
    K.append(mu/2*state[1]**2+L**2/(2*mu*state[0]**2)) #1/2*(mu*state[1]**2+1/(mu*(L/state[0])**2))
    U.append(-G*m2*m1/state[0])
    E.append(mu/2*state[1]**2+L**2/(2*mu*state[0]**2)-G*m2*m1/state[0])
    d.append(state[0])
    T.append(t)
#graph the energy as the function of time
    fK.plot(pos=(t,mu/2*state[1]**2+L**2/(2*mu*state[0]**2)))
    fU.plot(pos=(t,-G*m2*m1/state[0]))
    fE.plot(pos=(t,mu/2*state[1]**2+L**2/(2*mu*state[0]**2)-G*m2*m1/state[0]))

plt.subplot(2,1,1)
plt.plot(d,K);plt.plot(d,U);plt.plot(d,E)
plt.title("Eengy  versus  Distance")
plt.ylabel("E(J)")
plt.xlabel("r(m)")

plt.subplot(2,1,2)
plt.plot(T,K);plt.plot(T,U);plt.plot(T,E)
plt.title("Eengy versus Time")
plt.ylabel("E(J)")
plt.xlabel("t(s)")

plt.subplots_adjust(hspace=0.5)
plt.show()
