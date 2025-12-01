'''# CONDITIONAL STATEMENT
#Q1.Take two user inputs and determine which number is greater or if they are equal.
num1=int(input("tell 1st digit:- "))
num2=int(input("tell 2nd digit:- "))

if num1 >= num2:
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")

#Q2.Accept a gender input('m' or 'f') and print a greeting like "Hello sir  or "Hello ma'am".
gender=input("Tell your gender(m/f):- ")

if gender == 'm' or gender == 'M':
    print("Hello sir!")
elif gender =='f' or gender =='F':
    print("Hello Ma'am!")
else:
    print("Invalid input ! Plese enter the 'm' or 'f'")

#Q3.Accept a number from the user and check whether it's even or odd using mudulo(%)
num=int(input("enter the number:- "))
if num%2 == 0:
    print("even")
else:
    print("odd")

#Q4. input name and age. if age >= 18, print "eligable to vote".if not,print how many years are left to become eligible.
name=input("enter your name:- ")
age=int(input("enter your age:- "))

if age >= 18:
    print("you are eligable")

#Q5.Take an integer (1-7) and print the crresponding weekday(1=monday,2=Tuesday..7=sunday).handle invilad input too.
day=int(input("Enter a digit:- "))

if day == 1:
    print("Monday")

elif day == 2:
    print("Tuesday")

elif day == 3:
    print("Wednesday")

elif day == 4:
    print("Thursday")

elif day == 5:
    print("Friday")

elif day == 6:
    print("Saturday")

elif day == 7:
    print("Sunday")

else:
    print("Please ! enter a day for week")

#Q6.Accept the three number and find the greatest one among them using nasted if else.
num1=int(input("Enter your 1st digit:- "))
num2=int(input("Enter your 2nd digit:- "))
num3=int(input("enter your 3rd digit:- "))
if num1 > num2:
    if num1 > num3:
        print("The greatest number is:-",num1)
    else:
        print("The greatest number is:-",num3)
else:
    if num2 > num3:
        print("The greatest number is:-",num2)
    else:
        print("The greatest number is:-",num3)

#Q7.Accept an integer and check leap year
year=int(input("enter the year:- "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

#Q8.Ask for purchase amount. Apply discounts based on threshold: above 1000 -> 10%
# off, above 5000 -> 20% off. print final bill.(you can also design a shop-like interface later)

amount=float(input("Enter your purchase amount:- "))

if amount > 1000:
    discount = amount * 0.10

elif amount > 5000:
    discount = amount * 0.20

else:
    discount=0

final_amount=amount - discount

print("Purchase amount:- ",amount)
print("Discount amount:- ",discount)
print("Final amount:- ",final_amount)

#Q9.Accept a single alphabet and check if its a vowel (a,e,i,o,u,A,E,I,O,U) also hnadle invalid  charchters.
char=input("Enter a single alphabet: :- ")
if len(char)==1 and char.isalpha():
    if char in 'aeiouAEIOU':
        print("you are enter vowel")
    else:
        print("you are enter consonant")
else:
    print("Invalid input! Please enter only one alphabet")'''

#Q10.write a program that checks whether a given number is positive,negative, or zero
'''num=int(input("Enter the number:- "))
if num > 0:
    print("it's positive number")
elif num < 0:
    print("it's negative number")
else:
    print("its Zero or Invaild")'''