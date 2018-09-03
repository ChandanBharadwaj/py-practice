'''
Created on 03-Sep-2018

@author: Chandan Bharadwaj
'''
# else only gets executed when loop has iterated over all items.
# if loop breaks in bw looping, else wont execute. 

a ="chandan"
for item in a:
    print(item+"- chandan")
    if item =="n":
        break
else:
    print("done")

a =[1,2,3,4,5,6]
for a in a:
    print(a+10)