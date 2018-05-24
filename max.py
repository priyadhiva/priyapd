n=int(input("enter the number of elements"))
list=[]
for i in range(0,n):
    a=int(input("enter the value"))
    list.append(a)
print (list)
max=list[0]
for i in list:
    if(i>max):
        max=i
        print (max)

