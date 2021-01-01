#import PyDAQmx
#from PyDAQmx import Task
import numpy as np
import nidaqmx as ni
import time
import h5py as h5

now = int(time.time())

fname = '\mainchamber_pressure_tmpfix.h5'
pname = "D:\Logs\Pressure"

columns = ['ind','tstamp','PC','AC']
col_dtypes = ['<i4','<i4','<f4','<f4']

with h5.File(pname+fname, 'w',libver='latest') as hf:
    for i in range(0,len(columns)):
        hf.create_dataset(columns[i],shape=(0,),maxshape=(None,),dtype=col_dtypes[i],chunks=True)
    hf.swmr_mode = True

    with ni.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        task.ai_channels.add_ai_voltage_chan("Dev1/ai1")
        flag = 0
        ind = 0
        while flag < 1:
            tmp = task.read()
            hf['ind'].resize((hf['ind'].shape[0] + 1), axis = 0)
            hf['tstamp'].resize((hf['tstamp'].shape[0] + 1), axis = 0)
            hf['PC'].resize((hf['PC'].shape[0] + 1), axis = 0)
            hf['AC'].resize((hf['AC'].shape[0] + 1), axis = 0)

            hf['ind'][ind] = ind
            hf['tstamp'][ind] = int(time.time())
            hf['PC'][ind] = tmp[1]
            hf['AC'][ind] = tmp[0]
            hf.flush()
            data = [ind,int(time.time()),tmp[0],tmp[1]]
            ind += 1
            print(data)

            #if time.time() > now+120:
            #    flag = 1
            time.sleep(1)
        
        
