#program to solve quadratic equations
import cmath
 
m= int(input("enter the cofficient of x^2: "))
n= int(input("enter the cofficient of x: "))
o= int(input("enter the value of constant: "))
print (f"The quadratic expression looks like {m}x^2 + {n}x + {o}")

if ((n*n)-(4*m*o))> 0:
    def quad_equation(a1,b1,c1):
        d = ((b1*b1)-(4*a1*c1))
        r1 = ((-b1)+(d**0.5))/(2*a1)
        r2 = ((-b1)-(d**0.5))/(2*a1)
        return r1, r2
else:
    print ("roots are imaginary")

t1 = quad_equation(m,n,o)
print (f"The roots of the quadratic equation is {t1} ")