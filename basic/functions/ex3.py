'''
Created On : Mon Sep 10 2018

@author: Chandan Bharadwaj

'''
def fun(list1, list2):
    list2=list1
    list1.append(list2[0])
    print("list1",list1)
    print("list2", list2)

list1=["a"]
list2=["b"]
fun(list1,list2)
print(list1)
print(list2)
'''
list1 ['a', 'a']
list2 ['a', 'a']
['a', 'a']
['b']
'''