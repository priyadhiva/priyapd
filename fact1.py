a=int(input("enter a number"))
fact=1
for i in range (1,a+1):
    while i<=a:
        fact=fact*i
        i=i+1
        break
print (fact)
