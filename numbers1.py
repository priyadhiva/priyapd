a = input("Input a string")
d=0
for c in a:
    if c.isdigit():
        d=d+1
print("numbers", d)
