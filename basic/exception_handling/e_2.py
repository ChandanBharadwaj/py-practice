'''
Created On : Tue Sep 11 2018

@author: Chandan Bharadwaj

'''
#with exception handling
def funcWith():
      try :
        a ={1:11,2:22}
        print(a[100])
      except :
        print("i can catch all exceptions")

print("start")
funcWith()
print("end")
# start
# i can catch all exceptions
# end