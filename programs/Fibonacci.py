'''
Created on 03-Sep-2018

@author: Chandan Bharadwaj
'''
number = input("Enter the fibonacci number")
number = int(number)
n1=0
n2=1
fib=0
fiblist=[1]
while n1+n2<number:
    fib=n1+n2
    fiblist.append(fib)
    n1=n2
    n2=fib
print(fiblist)