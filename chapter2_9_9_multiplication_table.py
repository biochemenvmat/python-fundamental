# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 23:58:44 2022

@author: 18427
"""

#9*9 multiplication table
#complexity o(n^2)
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end=' ')
    print()
