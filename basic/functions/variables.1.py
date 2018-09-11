'''
Created On : Mon Sep 10 2018

@author: Chandan Bharadwaj

'''

a="i am global"

def fun():
    b="i am local"
    print(a)
    print(b)
    
fun()
print(a)