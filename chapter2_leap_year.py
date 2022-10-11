# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 00:15:18 2022

@author: 18427
"""

#leap year determination
n=eval(input())
if n%400==0:
    print('%d是闰年'%n)
elif n%100==0:
    print('%d不是闰年'%n)
elif n%4==0:
    print('%d是闰年'%n)
else:
    print('%d不是闰年'%n)