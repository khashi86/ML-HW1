import sys
import numpy as np
import matplotlib.pyplot as plt


# Khashayar Kotobi May 23 2017

def Costfun(x,z,t1,t0):

    hx= t0+t1*x
    test=(hx-z)*(hx-z)
    cost= np.sum(test)/(2*len(x))
    return cost

def UpdateT(x,z,t1,t0,alpha):
    myt0 = t0- (alpha/(len(x)))* np.sum(((t0+t1*x)-z))
    myt1 = t1 - (alpha / (len(x))) * np.sum(((t0 + t1 * x) - z) * x)
    return(myt1,myt0)

def gradCom(x,y,t1,t0,alpha,iterations):
    m=len(x)
    myJ=[]
    myt1=t1
    myt0=t0
    for i in range(iterations):
        myJ.append(Costfun(x,y,myt1,myt0))
        [myt1,myt0]= UpdateT(x,y,myt1,myt0,alpha)

    return (myt1,myt0,myJ)

def main():

    file_in = open('ex1data1.txt', 'r')
    x=[]
    z=[]
    i=0
    for y in file_in.readlines():
        i += 1
        floats = [float(x) for x in y.split(',')]
        x.append(floats[0])
        z.append(floats[1])
    w=2
    data = [[0]*5 for i in range(5)]
    dataset_list = x
    dataset_array = []

    myx = np.asarray(x)
    myz = np.asarray(z)
    test=myx*myz+1000
    print('test test',len(test),(test)[0])
    t1=0
    t0=0
    alpha=0.01
    iterations= 1500

    print(len(x), type(x), x)
    print(len(z), type(z), z)
    myt1, myt0,myJ = gradCom(myx,myz,t1,t0,alpha,iterations);
    print(myt1,myt0,myJ[iterations-1])
    print('final answer')
    print(len(myx), type(myx))
    print(gradCom(myx,myz,t1,t0,alpha,iterations))
    plt.plot(x, z, 'ro', x, (myt1*x)+myt0,'r--')
    plt.show()

if __name__ == "__main__": main()