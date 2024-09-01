from visual import *;import matplotlib.pyplot as plt
scene = display()
scene.background = (0.2,0.3,0.4)
scene.title = "Binary Star"
scene.forward = vector(0, 0, -1)
G = 6.7e-11
r1 = 1.5e11
star2X0 = -r1/2 #initial position
star1X0 = r1 
star1V0y = 3.3e+4 #initial velocity
star2 = sphere(pos= vector(star2X0, 0, 0), radius=r1*0.15,
               color= color.yellow, make_trail= True, trail_type= "curve")
star1 = sphere(pos= vector(star1X0, 0, 0), radius=r1*0.08,
               color= color.green, make_trail= True, trail_type= "curve")
star2.mass = 4e+30
star1.mass = 2e+30
star1.p = vector(0, 1.*star1V0y, 0)*(star1.mass)
star2.p = -star1.p
rR = sphere(pos= star1.pos-star2.pos, radius=r1*0.05, color= color.white,
              make_trail= True, trail_type= "curve")
center = sphere(pos= vector(0, 0, 0), size= 20000000000*(vector(1, 1, 1)), color= color.white, make_trail= True, trail_type= "points")

k=1
dt = 5000 ; NN=0
while NN<1:
    rate(5000)
    dist = star1.pos-star2.pos
    rR.pos = dist
    force = k*G*(star2.mass)*(star1.mass)*dist/(pow(mag(dist), 2+k))
    star2.p = star2.p+force*dt
    star1.p = star1.p-force*dt
    star2.pos = star2.pos+star2.p/star2.mass*dt
    star1.pos = star1.pos+star1.p/star1.mass*dt
    K=mag(star2.p)**2/(2*star2.mass)+mag(star1.p)**2/(2*star1.mass)
    U=-G*star2.mass*star1.mass/mag(dist)
    E=K+U


