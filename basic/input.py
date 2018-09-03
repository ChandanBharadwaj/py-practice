'''
Created on 03-Sep-2018

@author: Chandan Bharadwaj
'''
# age = input("Enter age")
# print (type(age))
# if age>10:
#   print("more than 10")
# else:
#   print("less than 10")

# What is true in python?
#True - Any non zero value, " ",[1],1,-1,"hello",True
#false - Any zero value, "",[],{},0,false,None
if None:
    print("if")
else:
    print("else")
# elif
age = input("Enter age")
age = int(age)
if age > 10:
    print("if")
elif age == 10:
    print("elif")
else:
    print("else")
