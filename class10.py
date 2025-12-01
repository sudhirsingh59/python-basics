#  Into to Data Structures:-
'''Data structures are a type of storage in which we can store multiple values.
In bulit Data Structure:- List,Duple,Dictonary,Set'''
# Customized Data Structure:- Stack,Queue,Linked List , Trees, Graphs....
#? List
a=[23,45,76,87,21]
print(len(a))
print(type(a))

#? List:- list is a mutable 
a = [10,20,30,45,50]
a[3] = 40
print("change list value:-",a)

#? Traversing method 1
a=[10,20,30,40]
for i in a:
    print(i)

#? Travasing method 2 (based on (indexing))
a=[10,20,30,40,50]

for i in range(len(a)):
    print("Length of index:-",i)
    print("Number of index:-",a[i])

# ? List method:- basic method of list(append(),pop(),reverse()) .
# Genral method list help(dir/help)
# help(list)

#Q1. append()
a=[10,20,30,40]
a.append(50)
print("Append:- ",a)

#Q2. clear
a=[10,20,30,40]
a.clear()
print("Clear a list:- ",a)

#Q3. copy
a = [10,20,30,40,50]
b = a.copy()
print("Copied list:- ",b)

#Q4.count
a = [10,20,30,40,50,20,20,20]
print(f"counting number of 20 is :- {a.count(20)} times")

#Q5.index
a=[10,20,30,40,50]
print(f"The indexing value 10 is :- {a.index(10)}")

#Q6. insert
a=[10,20,30,40]
a.insert(2,25)
print("The insert value between 20 to 30 is :-",a)

#Q7. pop
a = [10,20,30,40,50,20]
poped = a.pop(5)
print("pop index :- ",a)
print("poped index :- ",poped)

#Q8. sort
a=[21,43,7,34,87,45,879,21,34,32]
a.sort()
print("The sorting of list :- ",a)

