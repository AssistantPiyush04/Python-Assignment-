#print natural number 1 to n using while loop
a=int(input("enter nth number: "))
b=1
while(a>=b):
    print(b)
    b=b+1

#second program..
a=int(input("enter nth number: "))
while(a>0):
    print(a)
    a=a-1

#third program..
char='a'
while(char<='z'):
    print(char, end=' ')
    char=chr(ord(char)+1)

#fourth program..
i=2
while(i<=100):
    if(i%2==0):
     print(i,end=', ')
    i=i+1

#fifth program..
i=int(input("Enter the number: "))
num=1
while(num<=i):
    if(num%2!=0):
     print(num,end=', ')
    i=i+1

#sixth program..
n = int(input("Enter the value of n: "))
sum= 0
for i in range(1, n+1):
    if i % 2 != 0:
        sum+= i
print("The sum of all odd numbers between 1 and", n, "is:", sum)

#seventh program..
num = int(input("Enter a number: "))
count = 0
while num != 0:
    num//=10 
    count=count+1
print("The number of digits is:", count)

#eight program..
num = int(input("Enter a number: "))
sum=0
while num > 0:
    digit = num % 10 
    sum=sum+digit 
    num //= 10
print("The sum of the digits is:", sum)

#nineth program..
num = int(input("Enter a number: "))
last_digit = num % 10
first_digit = num
while (first_digit >= 10):
    first_digit //= 10
print("The first digit is:", first_digit)
print("The last digit is:", last_digit)

#tenth program..
num = int(input("Enter a number: "))
last_digit = num % 10
first_digit = num
while first_digit >= 10:
    first_digit //= 10
sum_of_digits = first_digit + last_digit
print("The sum of the first and last digit is:", sum_of_digits)

#eleventh program..
num = int(input("Enter a number: "))
reverse_num = 0
while num > 0:
    digit = num % 10 
    reverse_num = reverse_num * 10 + digit  
    num //= 10  
print("The reverse of the entered number is:", reverse_num)

#twelth program..
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = 1
for i in range(exponent):
    result *= base
print(f"{base} raised to the power of {exponent} is: {result}")

#thirteen program..
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is: {factorial}")

