#Largest among the three number

a= int(input("Enter the First number: "))
b= int(input("Enter the Second number: "))
c= int(input("Enter the Third number: "))

if a>b and a>c:
    print (f"{a} is the largest number among the following")
elif b>a and b>c:
    print (f"{b} is the largest number among the following")
else:
    print (f"{c} is the largest number among the following")