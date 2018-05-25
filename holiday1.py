x=input('day1')
y=input('day2')
a=['Monday','Tuesday','Wednesday','Thursday','Friday']
b=['Saturday','Sunday']
if x in b:
  print ("yes")
elif x in a:
  print("no")
if y in a:
  print("no")
elif y in b:
  print ("yes")
