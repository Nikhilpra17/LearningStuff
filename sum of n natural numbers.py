#Sum of n natural numbers

a = int(input("Enter the number "))

def summing(a):
    if a == 0 :
        return 0
    return (a + (summing(a-1)))

t = summing(a)
print (f"The sum of numbers till {a} is {t}")
