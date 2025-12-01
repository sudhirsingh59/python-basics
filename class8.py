# while loop
#Q1.pritn a value for 1 to 10
'''a=1
while a<11:
    print(a)
    a+=1'''

#Q2. print a value  10 to 1.
'''a=10
while a >= 0:
    print(f" 10 to 1:- {a}")
    a-=1'''

#Q. print ach digit(Reverse of digit)
'''a=145
while a > 0:
    print(a % 10)
    a=a//10'''
#Q. sum of digits(Add all the digits of a number 123-> 1+2+3).
'''n=int(input("Enter your number:- "))
sum=0
while n > 0:
    sum=sum+n%10
    n=n//10
print(f"the sum of its digit is:-{sum}")'''

#Q.Reverse of number(input a number and its digit 123->321)
'''a=int(input("Enter the number :- "))
rev=0
while a > 0:
    rev=rev * 10 + a%10
    a=a//10
print(f"Your number reverse is :-{rev}")'''

#Q. print a number which is palindromice number.
'''a=int(input("plese tell your number:- "))
rev=0
copy=a
while a > 0:
    rev=rev * 10 + a%10
    a=a//10
if rev == copy:
    print("yes your number is palindrome")
else:
    print("Sorry your number is not palindrome")'''
#Q.Automorphic Number(A  number is automophice if its square ends with the number itself)
a=7
dup=a
squre=a ** 2
count=0
while a > 0:
    count=count+1
    a=a//10
extract = squre % (10 ** count)
if extract == dup:
    print("Your number is automorphic")
else:
    print("Sorry not an automorphic number")