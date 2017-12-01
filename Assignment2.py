# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:06:33 2017

@author: Shalini
"""

import numpy as np

filename = "MatrixInput.txt"
beta = 0.85
epsilon=0.0005

#reading file
inputFile = np.genfromtxt(filename,dtype='float')

#getting matrix size
cols = np.amax(inputFile, axis=0)
size = int(np.amax(cols[0:2]))

#create a zero matrix of the above size
initMatrix = np.zeros((size,size))

for row in inputFile:
    i = int(row[0] -1)
    j = int(row[1] -1)
    k = row[2]
    
    initMatrix[j,i] = k

#normalizing rowValues
colSum = initMatrix.sum(axis=0)
#transposing a matrix
transMatrix = np.transpose(initMatrix)
newMatrix = np.zeros((size,size))
#normalizing matrix
for i, (row,colSum) in enumerate(zip(transMatrix,colSum)):
    if colSum !=0:
        newMatrix[i,:] = row / colSum
    else:
        newMatrix[i,:] = row

print("Normalised adjacency Matrix");        
newMatrix = np.transpose(newMatrix);
print(newMatrix)

#create initial row vector
rank0 = np.ones((size,1))
rank0 = rank0 * 1/size;
print("The original page rank vector")
print(rank0)

#iteraions for page rank
cnt =0
cond = False
while cond == False:
    rank1 = beta*np.dot(newMatrix,rank0) + (1-beta)*np.ones((size,1))*(1/size)
    #for row in (rank1,rank0):        
        #diff = sum(abs(rank1-rank0))
    if(sum(abs(rank1-rank0))>epsilon):
       cond = False
       rank0 = rank1 
    else:
       cond = True           
    cnt = cnt +1


print("Final page rank")
print(rank1)

print("Total number of iterations")
print(cnt)
