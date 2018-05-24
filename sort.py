n=int(input("enter the number of elements in the list"))
list=[]
for i in range(0,n):
    a=int(input("enter the value"))
    list.append(a)
    list.sort()
print (list)
