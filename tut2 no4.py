# -*- coding: utf-8 -*-
"""
Created on Sat May 06 19:55:55 2017

@author: Salma Khan
"""

import numpy
from numpy.fft import fft
from numpy.fft import ifft
from matplotlib import pyplot as plt

def conv_nowrap(x,y):
    assert(x.size==y.size)  
    xx=numpy.zeros(2*x.size)
    xx[0:x.size]=x

    yy=numpy.zeros(2*y.size)
    yy[0:y.size]=y
    xxft=fft(xx)
    yyft=fft(yy)
    vec=numpy.real(ifft(xxft*yyft))
    return vec[0:x.size]

if __name__=='__main__':
    x=numpy.arange(-20,20,0.1)
    sigma=2
    y=numpy.exp(-0.5*x**2/sigma**2)
    y=y/y.sum()

    yconv=conv_nowrap(y,y)
    plt.plot(x,y)
    plt.plot(x,yconv)
    