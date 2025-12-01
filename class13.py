#   SET 
#? intro to set :- 
'''Set is also used to store multiple values.
Synatx of set we use ({}) to denote set.
Set has unordered nature thaa means there is no index points but still it is mutable lets see how.
Set also not allow any duplicate values.
The set() Constructor.'''

s={10,20,30,40,50}
print(type(s))

s={10,"hello",(1,2,3),12.5,True,print()} # you can only store hashable values inside set
print(type(s))

# unordered natrure 
s = {10,40,50,20,60,80}
print(s)

# you cannot have duplicate values
s = {10,10,10,20,20,202,30,30,30,40,50}
print(s)

# Set constructor
a = {10,10,10,20,20,202,30,30,30,40,50}
s = set(a)
print(s)

# Set Traversing 
'''Traverse on the basis of values- it will run on the basis of hash values.
unordered traversing always
No index values so no traversing on the basis of index '''

# traversing on the set
s={12,34,56,12,12,78,23}
for i in s:
    print(i)

# Set methods
'''Sets heavily depends on methods 
General methods(dir/help)'''
"WE are use some set method "
#  add
s = {10,20,30,40}
s.add(70)
print(f"add the set :-{s}")

# clear
s = {10,20,30,40}
s.clear()
print(f"clear the set:- {s}")

# copy
s = {10,20,30,40}
s.copy()
print(f"copy your set:- {s}")

# diffrence()
s1 = {10,20,30,40,50}
s2 = {30,40,50,60,70}

print(f" diffrent parts sets are:- {s2.difference(s1)}") # 1st way to print diffrent methods of sets 
print(f"diffrent parts sets are:- {s2 - s1}") # 2nd way to print diffrent methods of sets 

# discard()
s1 = {10,20,30,40,50}
s1.discard(10)
print(f"Discrad your 1st sets method :-{s1}")

# intersection()
s1 = {10,20,30,40,50}
s2 = {30,40,50,60,70}
print(f"intersection value are:- {s1 & s2}")

# pop()
s = {10,20,30,40,50}
s.pop()
print(f"pop value :-{s}")

# symmetric_diffrence()
s1 = {10,20,30,40,50}
s2 = {30,40,50,60,70}
print(f"symmetric_diffrence are:- {s1 ^ s2}")

# union
s1 = {10,20,30,40,50}
s2 = {30,40,50,60,70}
print(f"union are:- {s1 | s2}")