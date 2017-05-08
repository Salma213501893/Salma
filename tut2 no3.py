# -*- coding: utf-8 -*-
"""
Created on Sat May 06 19:38:40 2017

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

def correlation(x,y):
    assert(x.size==y.size)  
    xft=fft(x)
    yft=fft(y)
    yftconj=numpy.conj(yft)
    return numpy.real(ifft(xft*yftconj))

if __name__=='__main__':
        x=numpy.arange(-20,20,0.1)
        sigma=2
        y=numpy.exp(-0.5*x**2/sigma**2)
        
        ycorr=correlation(y,y)
        yshift=conv(y,y.size/4)
        yshiftcorr=correlation(yshift,yshift)
        meanerr=numpy.mean(numpy.abs(ycorr-yshiftcorr))
        print 'the mean difference between the two correlation functions is ' + repr(meanerr)
        plt.plot(x,ycorr)
        plt.plot(x,yshiftcorr)        
        