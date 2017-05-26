# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:20:01 2017

@author: Salma Khan
"""

import numpy
import matplotlib
matplotlib.use('TkAgg')
from matplotlib  import pyplot as plt
import matplotlib.animation as animation

# Question 1

#create a class
class nBody:
    def __init__(self,m=1.0,x=0,y=0,npart=1000,G=1.0,soft=0.03,dt=0.1):
        self.dict={}
        self.dict['n']=npart
        self.dict['G']=G
        self.dict['soft']=soft

    def get_potential(self):
        self.fx=numpy.zeros(self.dict['n'])
        self.fy=0*self.fx
        potential=0
        for i in range(0,self.dict['n']):
            dx=self.x[i]-self.x
            dy=self.y[i]-self.y
            rsqr=dx**2+dy**2
            r=numpy.sqrt(rsqr)
            r3=1.0/(r*rsqr)
            self.fx[i]=-numpy.sum(self.m*dx*r3)*self.dict['G']
            self.fy[i]=-numpy.sum(self.m*dy*r3)*self.dict['G']
            potential+=self.dict['G']*numpy.sum(self.m/r)*self.m[i]
        return -0.5*potential 
        
# Question 2a
        
#method used to initialize the number of particles with random positions in 2D
        self.x=numpy.random.randn(self.opts['n'])
        self.y=numpy.random.randn(self.opts['n'])
        self.m=numpy.ones(self.opts['n'])*1.0/self.dict['n']
        self.vx=numpy.zeros(self.dict['n'])
        self.vy=numpy.zeros(self.dict['n'])  

# Question 2b

    def get_forces(self):
        self.fx=numpy.zeros(self.dict['n'])
        self.fy=0*self.fx
        potential=0
        for i in range(0,self.dict['n']):
            dx=self.x[i]-self.x
            dy=self.y[i]-self.y
            rsqr=dx**2+dy**2
            soft=self.dict['soft']**2
            rsqr[rsqr<soft]=soft
            rsqr=rsqr+self.dict['soft']**2
            r=numpy.sqrt(rsqr)
            r3=1.0/(r*rsqr)
            self.fx[i]=-numpy.sum(self.m*dx*r3)*self.dict['G']
            self.fy[i]=-numpy.sum(self.m*dy*r3)*self.dict['G']
            
# Question 2c

    def updatedict(self, dt):
          self.dict['dt']=dt        
          self.x=self.x+self.vx*dt
          self.y=self.y+self.vy*dt
          potential=self.get_potential()
          self.get_forces()
          self.vx=self.vx+self.fx*dt
          self.vy=self.vy+self.fy*dt
          kinetic=0.5*numpy.sum(self.m*(self.vx**2+self.vy**2))
          return potential+kinetic 

# Question 2d

if __name__=='__main__':
    plt.ion()
    n=1500
    oversamp=5
    part=nBody(m=1.0/n,npart=n,dt=0.1/oversamp)
    plt.plot(part.x,part.y,'*')
    plt.show()
    
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-5, 5), ylim=(-5, 5))
    line, = ax.plot([], [], '*', lw=2)

    #for i in range(0,10000):
    def animate_points(crud):
        global part,line,oversamp
        for ii in range(oversamp):
            energy=part.updatedict()
        print energy
        line.set_data(part.x,part.y)
        
    ani = animation.FuncAnimation(fig, animate_points, numpy.arange(30),
                              interval=25, blit=False)
    plt.show()           