'''
Created On : Tue Sep 04 2018

@author: Chandan Bharadwaj

'''
aa="chandan"
a= set(aa) #{'a', 'n', 'd', 'c', 'h'}
print(a)
b=set("sai")
print(b)#{'a', 's', 'i'}

#Union
c=a | b
print(c)#{'a', 'n', 'i', 'd', 'h', 'c', 's'}

#Intersection
print(a & b) #{'a'}

