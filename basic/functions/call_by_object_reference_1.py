'''
Created On : Mon Sep 10 2018

@author: Chandan Bharadwaj

'''

# call by object reference
def fun(x):
    x.append(100)
    print("inside ",x)

a=[1,2]
fun(a)
print("outside",a)
##inside  [1, 2, 100]
##outside [1, 2, 100]
