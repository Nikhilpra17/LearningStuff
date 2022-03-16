#Find HCF or GCD of two number

def HCF_function(a,b):

    if a>b:
        smaller = b
    else:
        smaller = a

    for i in range (1, smaller+1):
        if ((a % i == 0) and (b % i == 0)):
            return i
r= 54
t= 24

print('The HCF ', HCF_function(r,t))