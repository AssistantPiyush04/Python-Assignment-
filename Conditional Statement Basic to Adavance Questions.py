#find out wheather it can triangle or not..
angle1=int(input("Enter first angle: "))
angle2=int(input("Enter second angle: "))
angle3=int(input("Enter third angle: "))
if(angle1+angle2+angle3==180):
    print("The angles can form a triangle")
else:
    print("The angles can not form a triangle")


#determine weather when the value of temperature and humidity is provided by the user..
temprature=int(input("Enter Temperature: "))
humidity=int(input("Enter Humidity: "))
if(temprature>=30 and humidity>=90):
    print("Weather is hot and humid")
elif(temprature>=30 and humidity<90):
    print("Weather is hot")
elif(temprature<30 and humidity>=90):
    print("Weather is cool and humid")
elif(temprature<30 and humidity<90):
    print("Weather is cool")
else:
    print("please enter temperatue and humidity!!")

#take user input of cost price and selling price and determines whether its a loss or a profit..
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"You made a profit of: {profit} Ruppes")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"You have a loss of: {loss} Rupees")
else:
    print("No profit, no loss.")

#tell the number of dogs and chicken are there when the user will provide the value of total heads and legs..
head=int(input("Enter total number of heads: "))
legs=int(input("Enter total number of legs: "))
chickens=(4*head-legs)//2
dog=head-chickens
if chickens>=0 and dog>= 0 and 2*chickens+4*dog==legs: 
    print(f"There are {chickens} chickens and {dog} dogs.")
else: 
    print("The input values are not valid.")

#check whether a number is divisible by 5 and 11 or not
num=int(input("Enter the number: "))
if(num%5==0 and num%11==0):
    print("number is divisible by 5 and 11")
else:
    print("number is not divisible by 5 and 11")

#check whether triangle is valid or not if angles are given..
angle1=int(input("Enter angle1: "))
angle2=int(input("Enter angle2: "))
angle3=int(input("Enter angle3: "))
if(angle1==angle2==angle3):
    print("vaild Triangle")
else:
    print("not vaild Triangle")

#check whether triangle is equilateral, scalene or isosceles..
angle1=int(input("Enter angle1: "))
angle2=int(input("Enter angle2: "))
angle3=int(input("Enter angle3: "))
if(angle1==angle2==angle3):
    print("Equilateral Triangle")
elif(angle1==angle2 or angle1==angle3 or angle2==angle3):
    print("Isosceles Triangle")
elif(angle1!=angle2 and angle1!=angle3 and angle2!=angle3):
    print("Scalene Triangle")

#enter basic salary and calculate gross salary of an employee..
salary=int(input("Enter employees salary: "))
if(salary<=10000):
    hra=salary/100*20 
    da=salary/100*80  
    gross_salary=salary+hra+da
    print("gross salary is: ",gross_salary)
elif(salary>=10001 and salary<=20000):
    hra=salary/100*25 
    da=salary/100*90  
    gross_salary=salary+hra+da
    print("gross salary is: ",gross_salary)
elif(salary>=20001):
    hra=salary/100*30 
    da=salary/100*95  
    gross_salary=salary+hra+da
    print("gross salary is: ",gross_salary)
else:
    print("please enter vaild salary!!")

#calculate the total electricity bill..
units = float(input("Enter the total number of units consumed: "))
total_bill = 0
if(units <= 50):
    total_bill = units * 2
elif(units <= 150):
    total_bill = 50 * 2 + (units - 50) * 5
elif(units <= 300):
    total_bill = 50 * 2 + 100 * 5 + (units - 150) * 10
else:
    total_bill = 50 * 2 + 100 * 5 + 150 * 10 + (units - 300) * 15
print(f"The total electricity bill is: {total_bill} Rs")

#check whether any year is a leap year or not..
year = int(input("Enter a year: "))
if (year%4== 0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
