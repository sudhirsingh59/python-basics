#! lambda expression
# Q. square of a number
square = lambda a: print(f"square of number :-{a**2}")
square(12)
#Q. add two number
add = lambda a,b : a+b
print(add(12,13))
# Some advance stuff
"In this class we are going to see some of the advance stuff that can be used in python lets one by one."
"But before these things you must know lambda expression."
#!1) Map:- Purpose Apply function to every item of an iterable and return a new iterable "
def square(x):
    return x**2
a=[1,2,3,4]
l=map(square,a)
print(f"Square of a number by using of map:- {list(l)}")

#!2) Filter :- Filter items from an iterable based on a condtion"
#? Syntax:- filter(function,iterable)
a = [1,2,3,4,5,6]
l = filter(lambda x : x%2 == 0,a)
print(list(l))

#!3) Zip:- Combine multiple iterables into pairs of element"
name = ["sudhir","Rahul","Priya"]
age = [22,24,23]

comb = zip(name,age)
print(f"comb of name or age by using zip:-{(dict(list(comb)))}")

"Now lets see some short tricks of writing code:-"
"1)List Comprehensions"
a = [1,2,3,4,5,6,7,8,9]
l = [i for i in a if i%2 == 0]
print(f"List Comprehensions:- {l}")

"2)Dictionary Comprehensions"
a = [1,2,3,4,5,6,7,8,9]
l = {i:i**2 for i in a if i%2 == 0}
print(f"Dictionary Comprehensions :-{l}")

"3)Set Comprehensions"
a = [1,2,3,4,5,6,7,8,9]
l = {i for i in a if i%2 == 0}
print(f"Set Comprehensions:-{l}")

#! generators
"what is generators"
"Generators function(yield)"
"Generators Expression "
"compression in generators"
def my_generator():
    for i in range(5):
        yield i
gen = my_generator()
print(f"1st num generator:- {(next(gen))}")
print(f"2nd num generator:- {(next(gen))}")
print(f"3rd num generator:- {(list(gen))}")

# ganerate random numbers
#  