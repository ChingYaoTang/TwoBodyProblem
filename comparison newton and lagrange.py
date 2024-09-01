from visual import *;from numpy import cos;from numpy import sin
scene = display()
scene.background = (0.2,0.3,0.4)
scene.title = "single particle"
scene.forward = vector(0, 0, -1)

G = 6.7e-11
r1 = 1.5e11
x2 = -r1/2 #initial position
x1 = r1 
v1 = 3.3e+4 #initial velocity
star2 = sphere(pos= vector(x2, 0, 0), radius=0)
star1 = sphere(pos= vector(x1, 0, 0), radius=0)
m2 = 4e+30
m1 = 2e+30
p1 = vector(0, 1.*v1, 0)*(m1)
p2 = -p1
center = sphere(pos= vector(0, 0, 0), size= 20000000000*(vector(1, 1, 1)), color= color.white, make_trail= True, trail_type= "points")
rR = sphere(pos= star1.pos-star2.pos, radius=r1*0.1, color= color.white,
              make_trail= True, trail_type= "curve")

mu=m1*m2/(m1+m2)#reduce mass
M = sphere(pos = star1.pos-star2.pos, radius=r1*0.1,
               color= color.yellow, make_trail= True, trail_type= "curve")
L=x1*mag(p1)+-x2*mag(p2)#angular momentum(conserve)
#initial condition
r=mag(M.pos)
rd=((mag(p1)**2/(2*m1)+mag(p2)**2/(2*m2)-L**2/(2*mu*r**2))*2/mu)**(1/2)
phi=0
phid = L/(mu*r**2)
k=1

dt = 5000
n=0
while n<1:
    rate(5000)
    r = r+dt*rd
    rdd = -k*G*m1*m2/(mu*r**(k+1))+L**2/(mu**2*r**3)
    rd = rd+dt*rdd
    phi = phi+dt*phid
    phid = L/(mu*r**2)
    M.pos = (r*cos(phi),r*sin(phi),0)

    dist = star1.pos-star2.pos
    force = k*G*(m2)*(m1)*dist/(pow(mag(dist), 2+k))
    p2 = p2+force*dt
    p1 = p1-force*dt
    star2.pos = star2.pos+p2/m2*dt
    star1.pos = star1.pos+p1/m1*dt
    rR.pos = dist
    
    
