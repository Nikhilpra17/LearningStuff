#Program to Check Prime Number
#prime number are divided by one and itelf only.

a= int(input("Enter the number: "))
prime =  True

for i in range (2,a): # DOUBT IN THIS LINE
    if ( a % i) == 0:
        prime = False
        break


if prime == True:
    print (f"{a} is the Prime Number")
else:
    print (f"{a} is not a Prime Number")