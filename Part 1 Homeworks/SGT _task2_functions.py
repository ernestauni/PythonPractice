"""1. .Create a program that asks the user to enter their age and whether or not they have a driver's license. 
If the user is at least 18 years old and has a driver's license, the output should be as follows "You are able to drive : True
If not, then "You are able to drive : False"""

age= int(input("Enter your age: "))
license =input("Do you have a drivers' license? ")

result= ((age)>=18) and (license=='yes')
print(f"You are able to drive: {result}")

"""2.(Explore some String functions).
Create a program that asks the user for a password, and checks if it meets the following criteria: at least 8 characters long
If the password meets all of these criteria, print "Password accepted : True", otherwise print "Password accepted : False"."""

psw=input("Enter password: ")

result= len(psw)>=8
print(f"Password accepted : {result}")

"""3. Write a program that asks the user to enter two integers and checks if they are both even. 
If they are, print "Both numbers are even : True", otherwise print "Both numbers are even : False".
If at least one is even print "At least one number is even : True", else "At least one number is even : False".
Hint : use modulo operator % here"""

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

both_even= (num1 % 2==0) and (num2 % 2==0)
print(f"Both numbers are even: {both_even}")

at_least1=(num1 % 2==0) or (num2 % 2==0)
print(f"At least one number is even: {at_least1}")

"""4. Write a program that asks the user to enter a year and checks if it is a leap year. 
A leap year is defined as a year that is divisible by 4 but not by 100, or a year that is divisible by 400. 
If the year is a leap year, print "Leap year : True", otherwise print "Leap year : False". """

date=int(input("Enter date: "))
leap= (date%4==0) and (date%100!=0) or (date%400==0)
print(f"Leap year: {leap}")

"""(task with a star, optional) 5.Create the program which asks to enter the date (day, month, year). 
If the date is valid print : "Date valid : True" else "Date valid : False" """

day,month,year=input("Enter date (day,month,year): ").split()
day=int(day)
month=int(month)
year=int(year)

date= 0<day<32 and 0<month<13 and year>0
print(f"Date valid: {date}")