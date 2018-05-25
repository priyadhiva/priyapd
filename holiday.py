x=input('day1')
y=input('day2')
a=['Monday','Tuesday','Wednesday','Thursday','Friday']
b=['Saturday','Sunday']
if x in b:
  print ("holiday")
elif x in a:
  print("working day")
if y in a:
  print("working day")
elif y in b:
  print ("holiday")
