# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:58:27 2018

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
def mean(x):
    return float(sum(x)/len(x))

def var(x):
    a=0
    for i in x:
        a+=(i-mean(x))**2
        
    return float(a/len(x))
 
def estimate_coef(x,y):
    a=np.array(x)
    b=np.array(y)
    p=a*b
    
    val=float(sum(p)/len(p))
    
    num=val-(mean(x)*mean(y))
    den=sqrt(var(x))*sqrt(var(y))
    
    r=float(num/den)
    
    b0=r*(sqrt(var(y))/sqrt(var(x)))
    #b1=r*(sqrt(var(x))/sqrt(var(y)))
    
    return(b0,0)
    
 
def plot_regression_line(x, y, b):
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
    
    y_pred=[]
    for i in range(0,len(x)):
        
        y_pred.append(b[0]*(x[i]-mean(x))+mean(y))
 
    plt.plot(x, y_pred, color = "g")
 
    plt.xlabel('x')
    plt.ylabel('y')
 
    plt.show()

import pandas as pd
df = pd.read_excel("C://Users//HP//Desktop//IETE//tech team tests//linearreg//Glucose Levels.xlsx")
df=df.values
l=[]
m=[]
for i in range(0,len(df)-1):
    l.append(df[i][1])
    m.append(df[i][2])
 
def main():
    # observations
    x = l
    y = m
 
    # estimating coefficients
    b = estimate_coef(x,y)
    b0=b[0]
    b1=mean(y)-b[0]*mean(x)
    #b=[b0,b1]
    print("Estimated coefficients:"+str(b0)+"  "+str(b1))
 
    # plotting regression line
    plot_regression_line(x, y, b)
 
if __name__ == "__main__":
    main()
    

    
        



