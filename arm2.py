a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
for num in range(a,b+1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print (num)
   
