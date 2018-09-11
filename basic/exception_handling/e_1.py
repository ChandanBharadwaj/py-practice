'''
Created On : Tue Sep 11 2018

@author: Chandan Bharadwaj

'''
#without exception handling
def funcWithOut():
      a = {1:11,2:22}
      print(a[1111])

'''
Traceback (most recent call last):
  File "c:\chandan\workspace\photon\py\py-practice\basic\exception_handling\1.py", line 10, in <module>
    print(a[1111])
KeyError: 1111
'''

#with exception handling
def funcWith():
      try :
        a ={1:11,2:22}
        print(a[100])
      except KeyError:
        print("error occured")

print("start")
#funcWithOut()
funcWith()
print("end")
# start
# error occured
# end


