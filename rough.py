#Find Numbers Divisible by Another Number

a= int(input("Enter the number to divisible: "))
b= int(input("Enter the number to be divisible by: "))

if a % b ==0:
    print (f"{a} is divisible by {b}")
else:
    print (f"{a} is not divisible by {b}")