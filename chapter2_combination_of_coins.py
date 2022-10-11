# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 00:25:09 2022

@author: 18427
"""

n=eval(input())
a=n//10
b=(n-10*a)//5
c=n-10*a-5*b
count=1
print(a,b,c)
while a>0:
    a-=1
    b+=2
    print(a,b,c)
    count+=1
    while b>0:
        b-=1
        c+=5
        print(a,b,c)
        count+=1
print(count)