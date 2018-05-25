l=int(input("enter a number1"))
r=int(input("enter a number2"))
c=0
for num in range(1,r+1) :
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            c+=1
print (c)           
                
