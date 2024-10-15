from math import *
from tkinter import *
import keyboard

root=Tk()
root.title("1-D time dependent Schrodinger eq")
root.geometry("1920x1080")
graph=Canvas(root,width=300,height=200,bg="black")
graph.pack(fill="both",expand=True)

def convert(coords,obs,theta):
    x,y,z=coords[0],coords[1],coords[2]
    
    x,z,y=x,y,z
    obsx,obsy,obsz=obs[0],obs[1],obs[2]

    xr=x-obsx
    yr=y-obsy
    zr=z-obsz
    
    dyz=((yr)**2+(zr)**2)**.5
    dxz=((xr)**2+(zr)**2)**.5

    xp,yp=500,500
    
    if dyz>0:
        xp=1920*(xr/(2*dyz)*tan(theta)+.5) #magic
    if dxz>0: 
        yp=1080*(yr/(2*dxz)*tan(theta)+.5)

    #if abs(xp)>1920 or abs(yp)>1080:
        #xp,yp=0,0
        
    a=[xp,yp]
    return a

T=[]
nx=20
ny=20
for i in range(nx):
    add=[]
    for j in range(ny):
        if i==0 or i==nx-1:
            add.append([i,j,10])
        else:
            add.append([i,j,0])
    T.append(add)


dt=.1
ds=1
Tinf=-10
alp=.5
k=.5
h=.4

obs=[50,30,-140]
theta=120*pi/180
speed=.5
oval=5
cont=1

while cont==1:
    for i in range(1,nx-1):
        for j in range(ny):
            if j==0:
                #lap=(T[i-1][j][2]+T[i+1][j][2]+T[i][j+1][2]-4*T[i][j][2])/(2*ds)
                T[i][0][2]+=(h * (Tinf - T[i][0][2])) * dt#+=(alp*lap+h*(T[i][j][2]-Tinf))*dt

            if j==ny-1:
                #lap=(T[i-1][j][2]+T[i+1][j][2]+T[i][j-1][2]-4*T[i][j][2])/(2*ds)
                T[i][ny-1][2]+=(h * (Tinf - T[i][ny-1][2])) * dt#+=(alp*lap+h*(T[i][j][2]-Tinf))*dt
                
            else:
                lap=(T[i-1][j][2]+T[i+1][j][2]+T[i][j-1][2]+T[i][j+1][2]-4*T[i][j][2])/(ds**2)
                T[i][j][2]+=alp*lap*dt
    
    for i in range(nx):
        for j in range(ny):
            xp,yp=convert([T[i][j][0],T[i][j][1],T[i][j][2]],obs,theta)
            graph.create_oval(xp,yp,xp+oval,yp+oval,fill="red")

    if keyboard.is_pressed("up arrow"):
        obs[1]+=speed
    if keyboard.is_pressed("down arrow"):
        obs[1]-=speed
    if keyboard.is_pressed("left arrow"):
        obs[0]+=speed
    if keyboard.is_pressed("right arrow"):
        obs[0]-=speed
    if keyboard.is_pressed("w"):
        obs[2]+=speed
    if keyboard.is_pressed("s"):
        obs[2]-=speed
    
    root.update()
    graph.delete("all")

    if keyboard.is_pressed("q"):
        cont=0
        root.destroy()








              
