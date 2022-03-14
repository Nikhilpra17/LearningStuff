# factorial of the number

a = int(input(" Enter the number: "))

def factorial_number(a):
    if a ==0 or a == 1:
        return 1
    else:
        return a*factorial_number(a-1)

t= factorial_number(a)
print (t)
 

