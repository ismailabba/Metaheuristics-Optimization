#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:59:25 2020

@author: Ismailam
"""


n=6 #number of TSP nodes
w =[[0,5,7,2,6,5],
    [5,0,3,4,2,7],
    [7,3,0,4,4,3],
    [2,4,4,0,2,7],
    [6,2,4,2,0,4],
    [5,7,3,7,4,0]]

s=[1, 2,3,4,5,6]
#s = randperm(6) #initial solution
#Calculate Cost of Distances
def cost(n,s,w):
    cost=0;
    for i in range(0, n-1):
        
        print("index: ", s[i]-1, s[i])
        print ("value", w[s[i]-1][s[i]])
        cost=w[s[i]-1][s[i]]+cost;
        # print("cost: ", cost)
    cost=w[s[n-1]-1][s[0]]+cost;
    return cost
    # print("fcost: ", cost)


z = cost(n,s,w);
sstar=s
zstar=z
i = 1

while(1):
    
    for i in range(1, n-1):
        j=i+1;
        while j<=n:
            sprime=s
            temp=sprime[i]
            
            sprime[i]=sprime[j]
            sprime[j]=temp
            print(sprime)
            zprime=cost(n,sprime,w);
            print(zprime)
            if (zprime >= zstar and j<n):
                j=j+1;
            else:
                j=j+1;
                if(zprime<zstar):
                    sstar=sprime;
                    zstar=zprime;
      
    if s == sstar:
        break
    else:
        s=sstar;
        z=zstar;



print(sstar);
print(zstar);

#toc

