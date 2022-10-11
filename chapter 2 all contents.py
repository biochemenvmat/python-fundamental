# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:04:40 2022

@author: 18427
"""
#exchange variables vablue

x,y=5,10
x,y=y,x
print(x,y)

#string

id='leehsiaolong' 
print(id[2:4])
#string intercepting.
#string is immutable type, but intercepting some elements is allowed.
#sequence from 0 to n-1, -1 to -n in reverse.

#tuple

dasi=(2200,'test1','a','b',True,[5,6,7])
print(dasi[2])
#True是布尔代数值，是常量，1+3j是复数，元组不能切片
#True is a Boolean value and constant;
#1 + 3j is a complex number;
#tuple cannot be sliced.

#import operation
import sys
sys.float_info
#查看浮点数精度和范围
#check the specification and range of float number in pythons

#list operation

dasi=[2200,'test1','a','b',True,[5,6,7]]
print (dasi[1:])
#list sequence start from 0 to n-1, and -1 to -n in reverse.
#so it prints 'test' to list [5, 6, 7]

dasi=[2200,'test1','a','b',True,[5,6,7]]
dasi[2:4]=[1]
print(dasi)
#List is a mutable type, so it is easy to change the elements inside.
#change 3rd and 4th element to only one element, 1.

dasi=(2200,'test1','a','b',True,[5,6,7])
dasi[5][2]=8
print(dasi)
#change the 2nd element of nested list in list dasi.

#set

a={10,2.5,True,'pigeon',10+6j,}
b=set('hellow')
c=set(['a','b','c','d'])
print(a)
print(b)
print(c)
#set do not allow duplicated elements, all elements should be hashable.

#dictionary

list(zip(['one','two','three'],[1,2,3]))
#create key-value pair list

info={'name':'张三','age':19,'height':'180cm','weight':'75kg','score':{'python':90,'math':95}}
print(info['name'])
print(info['age'])
print(info['height'])
print(info['weight'])
print(info['score'])
print(info['score']['python'])
#字典的查询使用键，不能用下标
#access to elements can only be conducted by searching keys, not subscript.

#placeholder operator and arithmetic operator

s1='%s本次的数学成绩为%d,上次为%d,提升幅度为%f'%('小明',90,85,5/85)
print(s1)
s2='%s本次的数学成绩为%5d,上次为%5d,提升幅度为%08.2f'%('小明',90,85,5/85)
print(s2)
#%后加数字为占位符，
#%5d and %08.2f are placeholders.
s3='%s本次的数学成绩为%5d,上次为%5d,提升幅度为%08.2f%%'%('小明',90,85,500/85)#表示百分数需要写成%%，前一个表示占位符，后一个表示百分号
print(s3)
#%% represent actual % symbol.

print(5.2//2)
#// represents Quotient operation.

f1,f2=1.5,3.2
print(f1*f2)
#十进制数字在存储为二进制时产生精度损失，导致数值为4.800000000000001
#it will cause specification loss when converting decimal number to binary.

#assignment operator
i1=10 
i2=3
i1+=i2
print(i1)

#comparison operator
i1,i2,i3=10,9,8
print(i1==i2)
print(i1!=i2)
print(i1<i2)
print(i2>i3)
print(i1<=i3)
print(i2>=i3)

#logical operator
a=100
n=80
print(a>n and a<120)
print(a<=n or a>+90)
print(not(a!=90 and a>95 ))

#bitwise operator
print(7^10)
#bitwise XOR
print(7&10)
#bitwise AND
print(7|10)
#bitwise OR
print(7<<1)
#left shift
print(7>>1)
#right shift

#identity operator
#is determines whether two objects reflect the same memory
#is not in reverse
x,y=15,15
a=[1,2,3]
b=[1,2,3]
print(x is y)
print(x is not y)
print(a is b)
print(a is not b)
print(x is 15)#这两行会报语法警告，但我们查的是内存空间是否一致，所以不需要管
print(y is 15)#
print([1,2,3] is a)

#sequence operator and operaotr priority
#+ and * can be applied to sequences.
#+ connects 2 sequences together, * duplicates sequence multiple times and  connect them.
x,y=[15,True,'abc'],[213,False,'network']
z=x+y
print(z)
a,b='我喜欢学习','vba'
c=a+b
print(c)
x_3=x*3
print(x_3)
c_3=c*3
print(c_3)

#conditional statements 
#if else
b=eval(input('请输入你的成绩:'))
if b<60:
    print('不及格')
else:
    print('及格')

#if elif*n else
b=eval(input('请输入你的成绩:'))
if b<60:
    print('不及格')
elif b<70:
    print('及格')
elif b<80:
    print('中等')
elif b<90:
    print('良好')
elif b<=100:
    print('优秀')
else:
    pass

#if
score=59

if score<60:

    print('成绩为%d'%score,end='，')

print('不及格')

#loop statement
#for in
ls=['python','java','php','vba','c','c++','golang','ruby']
for k in ls:
    print(k)

#while
b=eval(input('请输入一个数字：'))
sum,i=0,1
while i<=b:
    sum+=i
    i+=1
print(sum)
print(i)
