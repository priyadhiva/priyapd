x=int(input("enter a number"))
def count(x):
  while(x>0):
    x=x//10
    count=count+1
  print count 
count(x)  
