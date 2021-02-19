# -*- coding: utf-8 -*-
"""SOMKel1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k-KDoP5ZHW24GD2_6-bZlz7G-h-Llsdr

**PROGRAM SOM (Self Organizing Maps)**
**BY : KELOMPOK 2**
"""

import math
import numpy as np
import sys

MAX_CLUSTERS = 1 #OUTPUT
VECTORS = int(input('Masukkan Banyaknya masukan : ')) #INPUT
VEC_LEN = int(input('Masukkan Banyaknya pola : ')) #DATA
DECAY_RATE = float(input('Masukkan Fungsi Pembelajaran : ')) #Fungsi Pembelajaran
MIN_ALPHA = float(input('Masukkan Minimum Learning Rate : ')) #Minimum Learning Rate
Alpha = float(input('Masukkan Learning Rate : ')) # Learning Rate


class algoSOM:
    def __init__(self, numVectors, maxClusters, alphaStart, minimumAlpha, decayRate, vectorLength):
        self.mVectors = numVectors
        self.mVecLen = vectorLength
        self.mAlpha = alphaStart
        self.minAlpha = minimumAlpha
        self.decayRate = decayRate
        self.mIterations = 0
        self.maxClusters = maxClusters
        self.mD = [[]] * maxClusters
        self.w = np.random.random((VECTORS,MAX_CLUSTERS))
        print('   ')
        print('Bobot awal (Acak) : ')
        print(self.w)
        print('   ')
    
    def compute_input(self, vectorNumber, trainingTests):
        for i in range(self.maxClusters):
           self.mD[i] = 0.0
        
        for i in range(self.maxClusters):
            for j in range(self.mVectors):
                self.mD[i] += math.pow((self.w[j][i] - trainingTests[vectorNumber][j]), 2)
            print('D[',i,']',self.mD[i])
        return
    
    def train(self, patterns, trainingTests):
        self.mIterations = 0
        
        while self.mAlpha > self.minAlpha:
            self.mIterations += 1
            for i in range(self.mVecLen):
                self.compute_input(i, trainingTests)
                
                # See which is smaller, mD(0) or mD(1)?
                iMin = self.mD[0]
                k=0
                for a in range(self.maxClusters):
                    if (iMin > self.mD[a]):
                       iMin = self.mD[a]
                       dMin = a
                       k+=1
                    else :
                       k=k
                       dMin = 0+k
                print('dMin',dMin)
                
                # Update the weights on the winning unit.
                for j in range(self.mVectors):
                    self.w[j][dMin] = self.w[j][dMin] + (self.mAlpha * (patterns[i][j] - self.w[j][dMin]))
            
                #print weights    
                for b in range(self.maxClusters):
                   for j in range(self.mVectors):
                      print('w [',j,b,'] :',self.w[j][b])
        
            # Reduce the learning rate.
            self.mAlpha = self.decayRate * self.mAlpha
            print('Learning rate : ',self.mAlpha)
            print('  ')
        
        return
    
    def test(self, patterns, trainingTests):
        # Print clusters created.
        print('  ')
        sys.stdout.write("Clusters for training input:\n")
        
        for i in range(self.mVecLen):
            print('  ')
            self.compute_input(i, trainingTests)
            
            iMin = self.mD[0]
            k=0
            for a in range(self.maxClusters):
                if (iMin > self.mD[a]):
                   iMin = self.mD[a]
                   dMin = a
                   k+=1
                else :
                   k=k
                   dMin = 0+k
            
            sys.stdout.write("\nVector ( ")
            
            for j in range(self.mVectors):
                sys.stdout.write(str(patterns[i][j]) + ", ")
            
            sys.stdout.write(") fits into category " + str(dMin) + "\n")
        
        # Print weight matrix.
        sys.stdout.write("\n")
        for i in range(self.maxClusters):
            sys.stdout.write("Weights for Node " + str(i) + " connections:\n")
            
            for j in range(self.mVectors):
                sys.stdout.write("{:03.3f}".format(self.w[j][i]) + ", ")
            
            sys.stdout.write("\n\n")
        
        # Print post-training tests.
        sys.stdout.write("Categorized test input:\n")
        for i in range(self.mVecLen):
            print('  ')
            self.compute_input(i, trainingTests)
            
            iMin = self.mD[0]
            k=0
            for a in range(self.maxClusters):
                if (iMin > self.mD[a]):
                   iMin = self.mD[a]
                   dMin = a
                   k+=1
                else :
                   k=k
                   dMin = 0+k
    
            sys.stdout.write("\nVector ( ")
            
            for j in range(self.mVectors):
                sys.stdout.write(str(trainingTests[i][j]) + ", ")

            sys.stdout.write(") fits into category " + str(dMin) + "\n")
        
        return
    
    def get_iterations(self):
        return self.mIterations

if __name__ == '__main__':
    
    somm = algoSOM(VECTORS, MAX_CLUSTERS, Alpha, MIN_ALPHA, DECAY_RATE, VEC_LEN)
    C=VECTORS #N
    R=VEC_LEN #F
    #normalisasi data

    #INITIALIZATION training_patterns
    training_patterns=[[0]*C for x in range(R)]
    #RECEIVING NEW VALUES TO THE INITIALIZED ARRAY training_patterns
    for i in range(R):
        for j in range(C):
            training_patterns[i][j]=int(input('Masukkan data : '))
    print('   ')
    print('Data Training yang telah diinput : ')
    print(training_patterns)
    print('   ')

    #INITIALIZATION tests
    tests=[[0]*C for x in range(R)]
    #RECEIVING NEW VALUES TO THE INITIALIZED ARRAY tests
    for i in range(R):
        for j in range(C):
            tests[i][j]=int(input('Masukkan data : '))
    print('   ')
    print('Data Test yang telah diinput : ')
    print(tests)
    print('   ')


    somm.train(training_patterns, tests)
    somm.test(training_patterns, tests)
    
    sys.stdout.write("\nIterations: " + str(somm.get_iterations()) + "\n")