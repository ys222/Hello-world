n=int(input("enter the number of elements to be inserted : "))
a=[]
for i in range(n):
    elem=int(input("enter element:"))
    a.append(elem)
avg=sum(a)/n
print("average of elements in the list",round(avg , 2))
