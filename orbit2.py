from math import sqrt
from drawtraj import drawtraj

def force(x,y,m,mstar):
    r2=x**2+y**2
    r32=r2*sqrt(r2)
    fx=-x*m*mstar/r32
    fy=-y*m*mstar/r32
    return fx,fy

def integrate(x,y,vx,vy,fx,fy,m,dt):
    ax,ay=fx/m,fy/m
    vx+=ax*dt
    vy+=ay*dt
    x+=vx*dt
    y+=vy*dt
    return x,y,vx,vy

# Main part of the program
mstar=100
m=1
nsteps=100000
dt=0.01
r=50
x,y=0,r
vx,vy=1.2,0
trajx,trajy=[],[]
star_x, star_y = 0, 0  # x and y position of star
star_vx, star_vy = 0, 0  # velocity of the star
star_trajx, star_trajy = [], []  # list to store the star's trajectory


for t in range(nsteps):
    fx,fy=force(x,y,m,mstar)
    x,y,vx,vy=integrate(x,y,vx,vy,fx,fy,m,dt)
    trajx.append(x)
    trajy.append(y)
    star_x, star_y, star_vx, star_vy = \
        integrate(star_x, star_y, star_vx, star_vy, -fx, -fy, mstar, dt)
        # calculate new star position and velocity
    star_trajx.append(star_x)  # put star x position in list
    star_trajy.append(star_y)  # put star y position in list

drawtraj(trajx, trajy, star_trajx, star_trajy, 10*r)