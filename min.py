n=int(input("enter the number of elements"))
list=[]
for i in range(0,n):
    a=int(input("enter the value"))
    list.append(a)
print (list)
min=list[0]
for i in list:
    if(i<min):
        min=i
        print (min)

