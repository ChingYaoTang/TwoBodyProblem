# Tested in VPython IDLE version 2.7a0
# Python version: 2.7.14 Tk version: 8.5
from visual import *
scene = display()
scene.title = "Binary Star"
scene.forward = vector(0, -1, 0) # (0, -0.3, -1)
G = 6.7e-11
au = 1.5e11 #1.5e11
giantX0 = -au/1.5
dwarfX0 = au
giantV0z = -10000
giant = sphere(pos= vector(giantX0, 0, 0), radius=au*0.15,
               color= color.yellow, make_trail= True, trail_type= "curve")
dwarf = sphere(pos= vector(dwarfX0, 0, 0), radius=au*0.08,
               color= color.green, make_trail= True, trail_type= "curve")
giant.mass = 2e+30
dwarf.mass = 1e+30
giant.p = vector(0, 0, 1.*giantV0z)*(giant.mass)
dwarf.p = -giant.p
rR = sphere(pos= dwarf.pos-giant.pos, size= 30000000000*(vector(1, 1, 1)), color= color.white,
              make_trail= True, trail_type= "curve")
center = sphere(pos= vector(0, 0, 0), size= 20000000000*(vector(1, 1, 1)), color= color.white, make_trail= True, trail_type= "points")

dt = 100000
NN=0
while NN<10000000:
    NN= NN+1
    rate(200)
    dist = dwarf.pos-giant.pos
    rR.pos = dist
    force = G*(giant.mass)*dwarf.mass*dist/(pow(mag(dist), 3))
    giant.p = giant.p+force*dt
    dwarf.p = dwarf.p-force*dt
    giant.pos = giant.pos+giant.p/giant.mass*dt
    dwarf.pos = dwarf.pos+dwarf.p/dwarf.mass*dt
