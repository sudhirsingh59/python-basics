# Exception Handling
'''when we run a program in pyton there are various exceptions that can e raised
like- syntaxError,NameError,zero ZeroDivisionError etc'''

'''Exception are raised when the program is syntactically correct,
but the code result in an error.this error not 
stop the execution of the program,however,it changes the
normal flow of the program.'''

'''so you cannot handle the syntax error.but if there is no syntax error.elsebut if there is no 
syntax reeoe you can handle them.'''

# Exception Handling Functionalities
'''Try:- This will catch the exception if any and pass to
Except - Except will deal with exception you can have custom Executed or universal catcher.'''
a = int(input("prvide your 1st number:- "))
b = int(input("provide your 2nd number:-"))
try:
    print(a/b)
except Exception as err:
     print(f"Sorry sn frror occured as {err}")
print(a+b)
'''Else - Else will be executed if no exception ocurs or it wont be exected.
finally - This will definitely  no matter what happens
Raise - Raise a custom error as yu need'''
try:
    age = int(input("enter your age :-"))
    if age < 18:
        raise Exception("you must be 18+")
    print("Access granted")
except Exception as e:
    print("Error:",e)