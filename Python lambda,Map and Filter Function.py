#syntax of lambda function..
#lambda parame,pa2,p3 : expression
#lambda x,t : x+t
print(lambda num: num*2)

#example of lambbda function..
out=lambda num:num*2
print(out(10))

lambda x:"piyush"+ y: "sharma"


#Map Function
map(len,["hey","hello"])

#second question..
mylist=["hey","hello"]
list(map(len,mylist))

list(map(lambda x: len(x),["hey","hello"]))

list(map(lambda x: x%2==0,[10,20,56]))


#Third example of Map Function..
def gr(x):
        if x%2==0:
            print(True)
        else:
            print(False)
list(map(gr,[10,20,34,12,77]))

#Filter Function..
#First Example of filter..
list(filter(lambda x: x%2==0,[10,11,13,16]))


#Second Example of filter..
numbers = [ 1, -2, 3, -4, 5, -6 ]  
# Using filter() to remove negative numbers from the list  
result = list(filter(lambda x: x >= 0, numbers))  
print(result)  


#Third Example of filter with creating own fuction using def...
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)


