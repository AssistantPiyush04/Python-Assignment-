#first..
a=[1,3,4,3,2,1,4,3,]
b=[]
for i in range(1,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            if a[i] not in b:
             b.append(i)
print(b)

#Second
mysets=set({})
myset={1,2,3,4,51,12,2,10,1}
#add use to add only single element..
myset.add(10101)
print(myset)

#Third..
myset.update("hey")
myset.update(["hey",999])
print(myset)

#Fourth..
list1="hii"
list2="hyy"
for i in zip(list1,list2):
    print(i)

#Fifth..
s="pep"
y="ziz"
s_dict={}
y_dict={}
x=0
if(len(s)==len(y)):
    for index in range(0,len(s)):
        if(s[index] in s_dict and s_dict[ s[index] ]!=y[index] ):
         x=1
         break
        s_dict[s[index]]=y[index]
if(x==0):
    print("isomorphic")
else:
    print("not isomorphic")


#Sixth..
mylist=[7,1,5,3,6,4]
profit=0
min_price=mylist[0]
for i in range(len(mylist)):
    profit_margin=mylist[i]-min_price

    profit=max(profit,profit_margin)
    #print(min_price,mylist[i])
    min_price=min(min_price,mylist[i])

print(profit)

