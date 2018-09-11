'''
Created On : Tue Sep 04 2018

@author: Chandan Bharadwaj

'''
#f= open('hello.txt')
#FileNotFoundError: [Errno 2] No such file or directory: 'hello.txt'
#f.close()

# w: opens the file for writing only. Overwrites the file if exists.
#If file doesnot exist, creates a new file for writing.
f =open('hello.txt','w')
f.close()