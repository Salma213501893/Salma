# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:21:16 2017

@author: Salma Khan
"""

# Question 3
           
import numpy 
import matplotlib.pyplot as plt

n=300
x=numpy.linspace(0,2*numpy.pi,n)
y=numpy.sin(x)
z=numpy.cos(x)

data=y+numpy.random.randn(x.size)
order=10

A=numpy.zeros([x.size,order])
A[:,0]=1.0
for i in range(1,order):
    A[:,i]=A[:,i-1]*x

A=numpy.matrix(A)
d=numpy.matrix(data).transpose()
LHS=A.transpose()*A
RHS=A.transpose()*d
fitp=numpy.linalg.inv(LHS)*RHS
pred=A*fitp

plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,data,'x')
plt.plot(x,pred,'r')

plt.draw()