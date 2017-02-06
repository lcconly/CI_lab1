#!/usr/bin/env python
# coding=utf-8
#************************************************************************
#	> File Name: KNN.py
#	> Author: liucheng
#	> Mail: lcconlycs@gmail.com 
#       > Created Time: Mon 06 Feb 2017 19:27:44 PM PST
#*************************************************************************

import os,time
import numpy
from scipy.sparse import csr_matrix
#####get upper path of code
__location__=os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
#*********************** two method to load data *****************************#
#**************** method one take 1.344956s to load data *********************#
'''
#####using numpy to read original data and store as an array, get former 3 item
time1=time.time()
lines=numpy.loadtxt(os.path.join(__location__,"100k.dat"),delimiter=',',dtype=bytes)
#####it will contain "b'xxxxx'" when dtype is str
#data_arr=lines[1:,:3].astype('int')
#####using function csr_matrix((data,(row,col)),shape) to initial mtx
row=[]
col=[]
data=[]
for index,line in enumerate(lines):
    row.append(int(line[0]))
    col.append(int(line[1]))
    data.append(int(line[2]))
mtx=csr_matrix((data,(row,col)))
time2=time.time()
print("index:%d  time:%f shape:%d  %d"%(mtx.nnz,time2-time1,mtx.shape[0],mtx.shape[1]))
#print(mtx)
'''

#**************** method two take 0.268281s to load data *********************#
#time1=time.time()
#####read line by line to get values
lines = [line.split(',') for line in open(os.path.join(__location__,"100k.dat"))]
row=[]
col=[]
data=[]
for index,line in enumerate(lines):
    row.append(int(line[0]))
    col.append(int(line[1]))
    data.append(int(line[2]))
mtx=csr_matrix((data,(row,col)))
#time2=time.time()
#print("index:%d  time:%f shape:%d  %d"%(mtx.nnz,time2-time1,mtx.shape[0],mtx.shape[1]))

