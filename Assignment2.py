# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:06:33 2017

@author: Shalini
"""

import numpy as np

#filename = "C:\Users\Shalini\Documents\Information Retrival\inputMatrix.txt"
filename = "MatrixInput.txt"
beta = 0.85

#readinf file
inputFile = np.genfromtxt(filename,dtype='float')
#print(inputFile)

#getting matrix size
cols = np.amax(inputFile, axis=0)
size = int(np.amax(cols[0:2]))

#create a zero matrix of the above size
initMatrix = np.zeros((size,size))

for row in inputFile:
    i = int(row[0] -1)
    j = int(row[1] -1)
    k = row[2]
    
    initMatrix[i,j] = k
#print(initMatrix)

#normalizing rowValues
colSum = initMatrix.sum(axis=0)
#transposing a matrix
transMatrix = np.transpose(initMatrix)
newMatrix = np.zeros((size,size))

for i, (row,colSum) in enumerate(zip(initMatrix,colSum)):
    if colSum !=0:
        newMatrix[i,:] = row / colSum
    else:
        newMatrix[i,:] = row

#question 1
print("Normalised adjacency Matrix");        
newMatrix = np.transpose(newMatrix);
print(newMatrix)

#create initial row vector
rank0 = np.ones((size,1))
rank0 = rank0 * 1/size;
#question2
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
    #cond = np.allclose(rank0,rank1)
    if cond == False:
        rank0 = rank1
    cnt = cnt +1

print("Final page rank")
print(rank1)

print("Total number of iterations")
print(cnt)
