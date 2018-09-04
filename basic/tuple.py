'''
Created on 03-Sep-2018

@author: Chandan Bharadwaj

Tuple - A tuple is immutable list.
    - Can't be changed in any way once it is created.
    - enclosed in parantheses instead on square brackets
    - same as list, but methods available for list which modifies the tuple wont be available for tuple.
'''
a=tuple()
a=(1,2,3,"33")
for i in a:
    print(i)