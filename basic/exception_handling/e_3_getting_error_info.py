'''
Created On : Tue Sep 11 2018

@author: Chandan Bharadwaj

'''
import sys
#with exception handling
def funcWith():
      try :
        a ={1:11,2:22}
        print(a[100])
      except :
        print("i can catch all exceptions")
        err_class,err_msg,err_trace=sys.exc_info();
        print(err_class)
        print(err_msg)
        print(err_trace.tb_lineno)

print("start")
funcWith()
print("end")

# start
# i can catch all exceptions
# <class 'KeyError'>
# 100
# 12
# end
