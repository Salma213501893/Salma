# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:21:43 2017

@author: Salma Khan
"""

# Question 4

import numpy

def sim_gaussian(t,sig=0.5,amp=1.0,centre=0):
    dat=numpy.exp(-0.5*(t-centre)**2/sig**2)*amp
    dat+=numpy.random.randn(t.size)
    return dat

def sim_lorentzian(t,a=1,b=1,centre=0):
    dat=a/(b+(t-centre)**2)
    dat+=numpy.random.randn(t.size)
    return dat

class Gaussian:
    def __init__(self,t,sig=0.5,amp=1.0,centre=0,offset=0):
        self.t=t
        self.y=sim_gaussian(t,sig,amp,centre)+offset
        self.err=numpy.ones(t.size)
        self.sig=sig
        self.amp=amp
        self.centre=centre
        self.offset=offset
        
                
class Lorentzian:
    def __init__(self,t,a=1,b=1,centre=0,offset=0):
          self.t=t
          self.y=sim_lorentzian(t,a,b,centre)+offset
          self.err=numpy.ones(t.size)
          self.a=a
          self.b=b
          self.centre=centre
          self.offset=offset

    def get_chisq(self,vec):
        sig=vec[0]
        amp=vec[1]        
        centre=vec[2]
        offset=vec[3]
       
        pred=offset+amp*numpy.exp(-0.5*(self.t-centre)**2/sig**2)
        chisq=numpy.sum((self.y-pred)**2/self.err**2)
        return chisq

def run_mcmc(data,start_pos,nstep,scale=None):
    nparam=start_pos.size
    params=numpy.zeros([nstep,nparam+1])
    params[0,0:-1]=start_pos
    cur_chisq=data.get_chisq(start_pos)
    cur_pos=start_pos.copy()
    if scale==None:
        scale=numpy.ones(nparam)
    for i in range(1,nstep):
        new_pos=cur_pos+get_trial_offset(scale)
        new_chisq=data.get_chisq(new_pos)
        if new_chisq<cur_chisq:
            accept=True
        else:
            delt=new_chisq-cur_chisq
            prob=numpy.exp(-0.5*delt)
            if numpy.random.rand()<prob:
                accept=True
            else:
                accept=False
        if accept: 
            cur_pos=new_pos
            cur_chisq=new_chisq
        params[i,0:-1]=cur_pos
        params[i,-1]=cur_chisq
    return params

if __name__=='__main__':
    
    t=numpy.arange(-5,5,0.01)
    dat=Gaussian(t,amp=2.5)

    guess=numpy.array([0.2,1.2,0.3,-0.2])
    scale=numpy.array([0.1,0.1,0.1,0.1])
    nstep=100000
    chain=run_mcmc(dat,guess,nstep,scale)
    nn=numpy.round(0.2*nstep)
    chain=chain[nn:,:]
    
    param_true=numpy.array([dat.sig,dat.amp,dat.centre,dat.offset])
    for i in range(0,param_true.size):
        val=numpy.mean(chain[:,i])
        scat=numpy.std(chain[:,i])
        print [param_true[i],val,scat]
        
        
    print("Lorentzian")
    dat_lor=Lorentzian(t)
    chain_lor=run_mcmc(dat_lor,guess,nstep,scale)
    chain_lor=chain_lor[int(nn):,:]

    param_true=numpy.array([dat_lor.a,dat_lor.b,dat_lor.centre,dat_lor.offset])
    for i in range(0,param_true.size):
        val=numpy.mean(chain[:,i])
        scat=numpy.std(chain[:,i])
        print [param_true[i],val,scat]
        
# Bonus
import numpy 

def sim_gaussian(t,sig=0.5,amp=1.0,centre=0):
    dat=amp*numpy.exp(-0.5*(t-centre)**2/sig**2)
    dat+=numpy.random.randn(t.size)
    return dat
    
def get_trial_offset(sigs):
    return sigs*numpy.random.randn(sigs.size)
    
class Gaussian:
    def __init__(self,t,sig=0.5,amp=1.0,centre=0,offset=0):
        self.t=t
        self.sig=sig
        self.amp=amp        
        self.centre=centre
        self.offset=offset
        self.y=sim_gaussian(t,sig,amp,centre)+offset
        self.err=numpy.ones(t.size)
        
    def get_chisq(self, vec):
        sig=vec[0]
        amp=vec[1]
        centre=vec[2]
        offset=vec[3]

        pred=offset+amp*numpy.exp(-0.5*(self.t-centre)**2/sig**2)
        chisq=numpy.sum((self.y-pred)**2/self.err**2)
        return chisq
        
def run_mcmc(data,start_pos,nstep,scale=None):
    nparam=start_pos.size
    params=numpy.zeros([nstep,nparam+1])
    params[0,0:-1]=start_pos
    cur_chisq=data.get_chisq(start_pos)
    cur_pos=start_pos.copy()
    totaccept=0
    totreject=0
    if scale==None:
        scale=numpy.ones(nparam)
        
    for i in range(1,nstep):
        new_pos=cur_pos+get_trial_offset(scale)
        new_chisq=data.get_chisq(new_pos)
        if new_chisq<cur_chisq:
            accept=True
        else:
            delt=new_chisq-cur_chisq
            prob=numpy.exp(-0.5*delt)
            if numpy.random.rand()<prob:
                accept=True
            else:
                accept=False
        if accept:
            totaccept=totaccept+1
            cur_pos=new_pos
            cur_chisq=new_chisq
        else:
            totreject=totreject+1
        params[i,0:-1]=cur_pos
        params[i,-1]=cur_chisq
        accept_frac=totaccept/(totaccept+totreject)
    return params,accept_frac
    
    
if __name__ == '__main__':
    
    t=numpy.arange(-5,5,0.01)
    data=Gaussian(t,amp=2.5)
    guess=numpy.array([0.4,0.3,1.2,-0.2])
    nstep=1000
    scale=numpy.array([0.1,0.1,0.1,0.1])
    chain,accept =run_mcmc(data,guess,nstep,scale)
    nn=int(numpy.round(0.0*nstep))
    chain=chain[nn:,:]
    
    scale2=numpy.std(chain[:,0:-1],0) 
    nstep2=100000
    chain2,accept2=run_mcmc(data,chain[-1,0:-1],nstep2,scale2)
    nn2=int(numpy.round(nstep2*0.2))
    chain2=chain2[nn2:,:]

    print ("Accept fraction for short chain = " + repr(accept))
    print ("Accept fraction for long chain = "+ repr(accept2))
   
    real_param=numpy.array([data.sig,data.cent, data.amp,data.offset])
    for i in range (0, real_param.size):
        val=numpy.mean(chain2[:,i])    
        scat=numpy.std(chain2[:,i])
        print(real_param[i],val,scat)