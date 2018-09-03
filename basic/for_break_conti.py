'''
Created on 03-Sep-2018

@author: Chandan Bharadwaj
'''
#break terminates the loop execution
for a in range(10):
    if a == 3:
        break;
    print(a)
print("--------------")
#continue skips the current execution    
for a in range(10):
    if a == 3:
        continue;
    print(a)