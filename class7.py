# For loops
#Q1.print numbers from 10 to 40.
'''for i in range(10,40,1):
    print(i)'''

#Q2. print numbers from -10 to 40.
'''for i in range(-10,40,1):
    print(i)'''

#Q3. print numbers from 34 to 5.
'''for i in range(34,5,-1):
    print(i)'''

#Q4.lets take a inputng number and print table.
'''num=int(input("Enter the number you eant to table:- "))
for i in range(num,num*10+1,num):
    print(i)'''
#Q5.print string using for loop.(1st way)
'''s="Hello how are you"
for i in s:
    print(i)'''

# 2nd way
'''s="Hello how are you"
for i in range(0,len(s)):
    print(s[i])'''

# print a number 
'''num=int(input("Please tell me how many times you want print message:-"))
for i in range(num):
    print("hellow world!")'''

#Q. sum of the n numbers
'''n=int(input("Telli your number:-"))
s=0
for i in range(1,1+n):
    s=s+i
print(f"youe sum is{s}")
'''
#Q. factorial of number.
'''num=int(input("Till your number:-"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"your fact is:-  {fact}")'''

#Q. Sum of Even & odd Numbers.
'''n=int(input("Enter your number:- "))
even_sum=0
odd_sum=0
for i in range(1,n+1):
    if n%2 == 0:
        even_sum+=i
    else:
        odd_sum+-i
print(f"even sum is:-{even_sum} \n and your odd sum is :-{odd_sum}")'''

#Q. print all factors of numbers.
'''n=int(input("What number factors I want to find:- "))
for i in range(1,n+1):
    if n % i == 0:
        print(i)'''

#Q.sum of all factors number
'''n=int(input("Sum of number factors:-"))
sum=0
for i in range(1,n+1):
    if n % i == 0:
        sum+=i
print(f"your factors sum is {sum}")'''

#Q.power Calculation(a^b)
#  Input base a and exponent b, and calculate the result using a loop(without using **)
'''a=int(input("tell your value:- "))
b=int(input("tell your exponent:- "))
power=a

for i in range(b-1):
    power*=a
print(f"After power your answer is {power}")'''

#Q.prime number check.
# Accept a number and check if it is divisible only by 1 and itself(i.e, prime or not)
#  First way:-
'''n=int(input("give your number (prime check):-"))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count+=1
if count == 1:
    print("Your number is unity number ")
elif count == 2:
    print("Your number is prime ")
else:
    print("your number is composite")'''



