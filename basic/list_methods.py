'''
Created on 03-Sep-2018

@author: Chandan Bharadwaj
'''
a=list()

a.append("1") # add value to list
print(a)#['1']
a.extend([2,3]) # extend a list
print(a)#['1', 2, 3]

#insert value at particular location
a.insert(2, "object")
a.insert(-20000, "object-1")
a.insert(999999, "object-2")
print(a) #['object-1', '1', 2, 'object', 3, 'object-2']

#Remove : removes only first occurrence of the list
a.append("1")
a.remove("1")
print(a) #['object-1', 2, 'object', 3, 'object-2', '1']

# pop() remove based on index. Returns the removed value
a.append("1")
a.pop(0)
print(a) #[2, 'object', 3, 'object-2', '1', '1']

'''Searching in lists'''
a.index("1") # returns the index of the value at the first occurrence
print(a.index("1")) # 4

#print(a.index(9999)) # Python raises exception if not found.

#use "in" before finding in the list.
print(9999 in a) #False