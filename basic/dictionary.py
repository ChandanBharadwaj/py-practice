'''
Created On : Tue Sep 04 2018

@author: Chandan Bharadwaj

'''

# Dictionary : un-ordered collection of objects. 
# items are stored and fetched by key instead of position/index.

d={1:11} # here 1 is key and 11 is value.
# key can not exist with value, vice versa.
# Can have a duplicate key, it gives the latest value
# Keys must be immutable, numbers,strings,tuples
# can't have the list or any mutable objects

x="a"

d ={1:11,"1":23,(1,2):"hello",x:"some"}

print(d[1]) # 11
print(d["1"]) # 23
# to find length
print(len(d)) # 1

for a in d:
    print(d[a])#hello 11 23 some

#Update
x={1:2,3:4}
y={11:22,33:44}
print(x.items()) #dict_items([(1, 2), (3, 4)])
x.update(y)
print(x.items()) #dict_items([(11, 22), (1, 2), (3, 4), (33, 44)])
z={1:123}
x.update(z)
print(x.items()) #dict_items([(11, 22), (1, 123), (3, 4), (33, 44)])

#POP
x.pop(1)
print(x)#{11: 22, 3: 4, 33: 44}