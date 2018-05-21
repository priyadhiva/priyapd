x=int(input("enter a year"))
if (x%400==0):
  print("leap year")
elif (x%4==0):
  print("leap year")
elif(x%100!=0):
  print("leap year")
else:
  print("non leap year")
