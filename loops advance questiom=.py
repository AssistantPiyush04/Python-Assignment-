#lcm of two values..
'''n1=int(input("Enter first value: "))
n2=int(input("Enter second value: "))
greater= max(n1,n2)
while(greater%2!=0)or(greater%2!=0):
    greater=greater+1
print(f"the LCM of {n1} and {n2} is: ",greater)'''

#check whether a number is Prime number or not..
'''num=int(input("Enter the number: "))
isprime=True
for i in range(2,num):
    if num%i==0:
        isprime=False
        break
if num>1 and isprime:
    print(f"{num} is prime number")
else:
    print("{num} is not prime number")'''

#print all Prime numbers between 1 to n.
'''n = int(input("Enter the value of n: "))
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=', ')'''

#find all prime factors of a number..
'''a=int(input("Enter the number: "))
fact=2
while(a>1):
    if a%fact==0:
        print(fact,end=' ')
        a=a//fact
    else:
        fact=fact+1'''

#check whether a number is an Armstrong number or not.
'''a=int(input("enter the number: "))
temp=a
sum=0
while(a>0):
    rem=a%10
    sum=sum+rem*rem*rem
    a=a//10
if temp==sum:
    print("armstrong number")
else:
    print("not armstrong number")'''

#check wheather number is strong number or not..
'''n=int(input("Enter the number: "))
sum=0
temp=n
while(n):
    i=1
    f=1
    r=n%10
    while(i<=r):
        f=f*i
        i=i+1
    sum=sum+f
    n=n//10
if(sum==temp):
    print("strong number")
else:
    print("not strong number")'''

#positive number check..
a=int(input("Enter the number: "))
sum=0

