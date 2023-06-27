# 1)Write a program that takes a user input (an integer) and determines whether it is positive, negative, or zero.
num=int(input("Enter the number: "))
if num>0:
    print("Number is positive.")
elif num<0:
    print("Number is negative.")
else:
    print("Number is zero")

# 2)Write a program that prints out the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#For numbers that are multiples of both three and five, print "FizzBuzz".
for i in range (1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

# 3)Write a program that takes an integer as input and prints out all the factors of that integer.
number= int(input("Enter the number: "))
factor=1
for i in range (1,number+1):
    factor=factor*i
print(factor)


# 4)Create calculator: Ask user to provide 2 numbers and one operation to be performed (*,/,+.- or %). If the operation  provided does not match one of these, the program should print 
# "Operation provided isn't valid, please,try again" - in this case, the program should ask for the operation to be provided again
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("What operation should performed? Enter *,/,+.- or % : ")
    if op == '*':
        result = num1 * num2
        break
    elif op == '/':
        if num2 == 0:
            print("Division by 0 can not be executed.")
            continue
        else:
            result = num1 / num2
            break
    elif op == '+':
        result = num1 + num2
        break
    elif op == '-':
        result = num1 - num2
        break
    elif op == '%':
        result = num1 % num2
        break
    else:
        print("Operation provided isn't valid, please try again.")
        continue
print(f"Operation result is {result}")

# 5)Write a program that takes an integer as input and prints out whether that integer is prime or not.
number_check=int(input("Enter the number: "))
if num < 2:
    print("The number is not prime.")
else:
    # Check if the number is divisible by any integer between 2 and the square root of the number
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")