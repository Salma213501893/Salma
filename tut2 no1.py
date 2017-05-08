# -*- coding: utf-8 -*-
"""
Created on Sat May 06 18:22:51 2017

@author: Salma Khan
"""

import numpy
from numpy.fft import fft
from numpy.fft import ifft
from matplotlib import pyplot as plt

def conv(x,n=0):
    vector=0*x  
    vector[n]=1
    vectorft=fft(vector)
    xft=fft(x)
    return numpy.real(ifft(xft*vectorft))

if __name__=='__main__':
    x=numpy.arange(-20,20,0.1)
    sigma=2
    y=numpy.exp(-0.5*x**2/sigma**2)
    yshift=conv(y,y.size/2)
    
    plt.plot(x,y)
    plt.plot(x,yshift) 