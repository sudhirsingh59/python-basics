# Dictonary
#? Intro to Dictonary
'''Dictonary is also used to store multiple values, but unlike sets, it stores data in key value pairs.
Syntax of Dictonary:- We use {} to denote a dictonary, with each item in the format key:value.'''
"Example:- "
d = {10:100,20:200,30:300,40:400} # dict also print a key:value pair
print(d[10])

'''Dictionaries are unordered in older python version(before 3.7) but in morden python,they maintain insertion order.
Dictionaries are mutable, which means you can change,add,or remove items after creation.'''
d = {10:100,20:200,30:300,40:400} 
d[10]=1000
print(f"dict change value :- {d}")

'''Dictonaries do not allow duplicate keys, but values can be duplicated.'''
d = {10:100,20:200,30:300,10:400}
print(d[10])

'''The dict() constructor: you can create a dictonary using dict() as well.'''
d = dict([("name","sudhir"),("age",24)])
print(d)

#? Dictionary Traversing:- Dictionary Traversing can be done on the basis of keys aswell values.
a = {10:100,20:200,30:300,40:400}
for i in a.values():
    print(i)

#? Dictonary Methods:- There are not much methods of dictonary lets see some in action
# help(dict)
# get methods()
a = {10:100,20:200,30:300,40:400}
print(f"Result for get method :- {a.get(20)}")

# items
a = {10:100,20:200,30:300,40:400}
print(f"dictonary items:- {a.items()}")

# keys()
a = {10:100,20:200,30:300,40:400}
print(f"Result of keys :-{ a.keys()}")

# pop()
a = {10:100,20:200,30:300,40:400}
# print(f"pop your value :-{a.pop(30)}")
# and your poped your value.
popped = a.pop(30)
print(f"Here saved your popped value :- {popped}")

#Defult()
a = {10:100, 20:200, 30:300, 40:400}
a.setdefault(12, 1200)
print(f"Here your default value :- {a}")

# update
a = {10:100,20:200,30:300,40:400,50:500}
b = {60:600,70:700,80:800,90:900,100:1000}

a.update(b)
print(f"Here update :-{a}")