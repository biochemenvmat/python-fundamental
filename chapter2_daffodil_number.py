# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 00:26:49 2022

@author: 18427
"""

#水仙花数
#daffodil number
#Find all 3-digit integers whose cubic sum of 
#the numbers in the three positions is equal to the number itself
count=0
a=eval(input('请输入起始值：'))
b=eval(input('请输入截止值：'))
for n in range(a,b+1):
    x=n//100
    y=((n-100*x)//10)
    z=(n-100*x-10*y)
    if n==(x**3+y**3+z**3):
        count+=1
        print(n,end=' ')
        n+=1
    else:
        n+=1
if count!=0:
    print(count)
else:
    print('not found')