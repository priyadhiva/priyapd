x=int(input("enter a number"))
fact=1
for i in range (1,x+1):
    while i<=x:
        fact=fact*i
        i=i+1
        break
print (fact)
