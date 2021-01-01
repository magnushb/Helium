import numpy as np
import h5py as h5
import matplotlib.pyplot as plt
import time

fname = '\mainchamber_pressure_tmpfix.h5'
pname = "D:\Logs\Pressure"

# load data
with h5.File(pname+fname,'r',libver='latest',swmr=True) as hf:
    t = hf['tstamp']
    pp = hf['PC']
    pa = hf['AC']


    plt.ion()
    
    while True:
        t.id.refresh()
        pp.id.refresh()
        pa.id.refresh()
        timestamp = np.array(t)
        p_prep = np.array(pp)
        p_analysis = np.array(pa)


        plt.semilogy(timestamp,10**(p_prep-11))
        plt.semilogy(timestamp,10**(p_analysis-10))
        plt.xlabel('time')
        #plt.yscale('log')
        plt.ylabel('Pressure (mbar)')
        #plt.legend('Preparation chamber','Analysis chamber')
        plt.draw()
        #plt.yscale('log')
        plt.pause(60)
        plt.clf()
        