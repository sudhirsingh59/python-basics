# FUNCTIONS
#  Print vs Return
# 1. print
'''def Greet():  # defining a function
    print("Hello greetings from sudhir")
Greet() # this is calling the function
Greet()
Greet()'''

# 2. return
'''def greet():
    return "i am sudhir singh"
print(greet())
'''
# parameters and arguments.
'''def add(a,b):  # This is a parameters
    print(a+b)
add(2,5) # This is a arguments
add(5,7)
add(34,6)'''

# check your number is pallindrome.
'''def pallindrome(x):
    rev=0
    copy=x
    while x > 0:
        rev=(rev*10)+(x%10)
        x=x//10
    if rev == copy:
        return True
    else:
        return False
print(pallindrome(343))
print(pallindrome(123))
print(pallindrome(333))'''

# keyword argument
'''def addition(a,b):
    print(a+b)
addition(b=23,a=99)  # thins is keyword argument''' 