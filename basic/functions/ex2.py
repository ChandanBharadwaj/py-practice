'''
Created On : Mon Sep 10 2018

@author: Chandan Bharadwaj

'''

# call by object reference
def fun(x):
    x=[3,4]
    print("inside ",x)

a=[1,2]
fun(a)
print("outside",a)

#inside  [3, 4]
#outside [1, 2]
