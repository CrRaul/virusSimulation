
import numpy as np
import cv2
import copy
from collections import deque
from controller import *
import matplotlib.pyplot as plt

H,W = 600,1300 # screen
N = 120 # pop
E = 5 # dim ind pix
ctrl = controller(W,H,N,E)
ctrl.initPop()
ctrl.randomInfection(10)

# draw border and star/end point rect
def draw(img):
    shape = img.shape 
    H,W = shape[0], shape[1]

    cv2.line(img,(10,10),(10,H-10),(255,255,255),10)
    cv2.line(img,(10,10),(W-10,10),(255,255,255),10)
    cv2.line(img,(W-10,H-10),(10,H-10),(255,255,255),10)
    cv2.line(img,(W-10,H-10),(W-10,10),(255,255,255),10)

    return img

def main():
    global H,W,N,E
    # simulate
    
    infNr = []

    t = 0
    while True:
        img = np.zeros((H,W), np.uint8)
        img = draw(img)
            
        for i in range(N):
            obj = ctrl.getObj(i)
            pos = obj.getPosition()

            if obj.getInfected():
                color = (90,90,90)
            else:
                color = (240,240,240)

            cv2.circle(img, (int(pos[0]),int(pos[1])), E, color,-1)

        if t%10==0:
            infNr.append(ctrl.getInfNum())
        ctrl.update()

        t+=1

        cv2.imshow('virus-CrRaul', img)
        ch = cv2.waitKey(1)
        if ch == 27:
            break

    print(infNr)
    t = [i for i in range(len(infNr))]
    print(t)
    plt.plot(t,infNr)
    plt.axis([0, t[-1], 0, infNr[-1]])
    plt.xlabel('Time')
    plt.ylabel('#inf')
    plt.show()



if __name__ == '__main__':
    main()

cv2.destroyAllWindows()
cv2.waitKey(1)