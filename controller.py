
import numpy as np
import copy
from collections import deque
import random
from object import *

class controller():
    # W H - screen dim; N - pop dim; D - individ dim
    def __init__(self,W,H,N,D):
        self.__dimW = [W,H]
        self.__pop = []
        self.__dimP = N
        self.__dimE = D
        self.__infNum = 0

    def setDimPop(self, N):
        self.__dimP = N
    def getDimW(self):
        return self.__dimW
    def getDimP(self):
        return self.__dimP
    def getDimE(self):
        return self.__dimE
    def getObj(self,i):
        return self.__pop[i]
    def getInfNum(self):
        return self.__infNum

    # init random pop
    def initPop(self):
        for i in range(self.__dimP):
            obj = object(random.randint(10,self.__dimW[0]-10),random.randint(10,self.__dimW[1]-10))
            obj.setVelocity(np.array([random.randint(-3,3),random.randint(-3,3)],dtype='float64'))
            self.__pop.append(obj)

    # infect N random ind
    def randomInfection(self, N):
        for i in range(N):
            pos = random.randint(0,self.__dimP-1)
            self.__pop[pos].setInfected(True)
        self.__infNum = N

    def update(self):
        for i in range(0, self.__dimP):
            self.__pop[i].update()
        self.checkChangeDirAndInfection()


    def checkChangeDirAndInfection(self):
        # border
        nrI = 0
        W,H = self.__dimW[0], self.__dimW[1]
        for i in range(0,self.__dimP):
            if  self.__pop[i].getInfected() == True:
                nrI += 1
            posO = self.__pop[i].getPosition()

            #border
            if posO[0] < 10 or posO[0] > W-10 :
                self.__pop[i].flipHorizontal()
            if posO[1] < 10 or posO[1] > H-10:
                self.__pop[i].flipVertical()

            # obj@obj check inf
            D = self.__dimE//2
            for j in range(i+1,self.__dimP-1):
                posP = self.__pop[j].getPosition()
                if posO[0] <= posP[0]+D and posO[0] >= posP[0]-D and posO[1] <= posP[1]+D and posO[1] >= posP[1]-D:
                    if self.__pop[i].getInfected() != self.__pop[j].getInfected():
                        self.__pop[i].setInfected(True)
                        self.__pop[j].setInfected(True)

        self.__infNum = nrI

