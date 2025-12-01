# Into to tuple :- 
''' Tuple ia also used to store multiple values
Syntax of Tuple - we will parenthesis() to store values indexing similar to list
Tuple slicing is also similar to list 
Using Single is also similar to list 
Using single element in tuple

# tuple
# a=(12,24,"hello",print()) # tuple has hetrogenous nature and tuple has a inmutable we can not cahne a value.
#a=(1,2,3,3,4,5,6,7,7,8,9,10,10) # tuple can store duoplicate values.

# The tuple() constructor - can convert list to tuple 
Tuple unpacking.'''
a,b,c = (10,20,30)
print(b)

# tuple packing
a = (1,)
print(type(a))

# tuple indexing/slicing
a = (10,20,30,40,50)
print(a[:3])

# tuple creating
a = [10,20,30,40]
tup = tuple(a)
print(f"tuple are:- {tup}")

#tuple Traversing:-
'''traversing on the basis of values
traversing on the basis of index(using Range function) '''
# 1st way
t = (10,20,30,40,50)
for i in t:
    print(f" 1st way tuple Traversing:-{i}")
 
 #2nd way 
t = (10,20,30,40,50)
for i in range(len(t)):
    print(t[i])

# tuple methods:- Basic methods of values. General tuple methods(dir/help)
# help(tuple)
a=(10,20,30,40,50,40,40)
print(a.count(40))
print(a.index(30)) # indexing