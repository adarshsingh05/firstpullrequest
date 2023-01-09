#1. for sum of 1 - n numbers which are even only
maximum = int(input(" Please Enter the Maximum Value : "))
total = 0
number = 1
 
while number <= maximum:
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number
    number = number + 1

print("The Sum of Even Numbers from 1 to N = {0}".format(total))






# 2.for the factorial of number

num = int(input("enter the no"))


factorial = 1


if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)






#3. for factorial of a number


n = int(input("Enter Number: "))

sum = 0
for i in range(n+1):
  sum += i**2
  

print("Sum of squares of first {} natural numbers:",sum)