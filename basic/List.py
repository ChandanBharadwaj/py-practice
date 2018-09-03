'''
Created on 03-Sep-2018

@author: Chandan Bharadwaj
'''
'''
    -> list type is a container which 
    holds a number of other objects in given order
    -> index based
    -> index starts with 0
'''

# creating list

a=list()
b=[]
c=[1,3,7,"cb",(1,2),"x"]

#access value based on index
print(c[2])

#length of list.
print(len(c))

#slicing
print(c[1:5])

#access last value in 2 ways
print(c[len(c)-1])#x
print(c[-1])#x
