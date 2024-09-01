from visual import *;import matplotlib.pyplot as plt;from visual.graph import *
#graph of stars motion
scene = display()
scene.background = (0.2,0.3,0.4)
scene.title = "Binary Star"
scene.forward = vector(0, 0, -1)
#graph of energy
gd=gdisplay(x=600,y=0,width=1000,height=700)
fK=gcurve(color=color.blue)
fU=gcurve(color=color.yellow)
fE=gcurve(color=color.red)
G = 6.7e-11
r1 = 1.5e11
#initial position
x2 = -r1/2;x1 = r1
#initial velocity
v1 = 3.3e+4 
star2 = sphere(pos= vector(x2, 0, 0), radius=r1*0.15,
               color= color.yellow, make_trail= True, trail_type= "curve")
star1 = sphere(pos= vector(x1, 0, 0), radius=r1*0.08,
               color= color.green, make_trail= True, trail_type= "curve")
m2 = 4e+30
m1 = 2e+30
p1 = vector(0, 1.*v1, 0)*(m1)
p2 = -p1
print "initial position of star2=",star2.pos ####answer of Ex1
print "initial velocity of star2=",p2/m2 ####answer of Ex1
rR = sphere(pos= star1.pos-star2.pos, radius=r1*0.05, color= color.white,
              make_trail= True, trail_type= "curve")
center = sphere(pos= vector(0, 0, 0), size= 20000000000*(vector(1, 1, 1)), color= color.white, make_trail= True, trail_type= "points")
pos2=m2*star2.pos ; pos1=m1*star1.pos
state=[pos2, pos1, p2, p1]

k=1
#Runge-Kutta method
def f(t, state):
     [pos2, pos1, p2, p1] = state
     dis = pos1/m1-pos2/m2
     P2 = p2 ; P1 = p1
     force = k*G*(m2)*(m1)*dis/(pow(mag(dis), 2+k))
     return array([P2,  P1, force, -force])

t=0 ; h = 5000 ; NN=0
#while NN<1:
for n in range(8*10**4):
    rate(5000)
    k1 = f(t,state)
    k2 = f(t+h/2, state+h/2*k1)
    k3 = f(t+h/2, state+h/2*k2)
    k4 = f(t+h,  state+h*k3)
    state += h/6 * (k1 + 2*k2 + 2*k3 + k4)
    t += h    
    star2.pos = state[0]/m2
    star1.pos = state[1]/m1
    dist = star1.pos-star2.pos ; rR.pos = dist
    K=mag(state[2])**2/(2*m2)+mag(state[3])**2/(2*m1)
    U=-G*m2*m1/mag(dist)
    E=K+U
#graph the energy as the function of distance ####answer of Ex2
    fK.plot(pos=(mag(dist),K))
    fU.plot(pos=(mag(dist),U))
    fE.plot(pos=(mag(dist),E))
