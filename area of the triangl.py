#program to find the area of the triangle
 
a= float(input("enter the 1st side of triangle: "))
b= float(input("enter the 2nd side of triangle: "))
c= float(input("enter the 3rd side of triangle: "))

if a>(b+c) or b>(a+c) or c>(a+b):
    print ("Triangle is invalid")
else:
    def area_of_triangle(a1,b1,c1):
        s= (a1+b1+c1)/2
        return ((s*(s-a1)*(s-b1)*(s-c1))**0.5)

t1 = area_of_triangle(a,b,c)
print (f"The area of the triangle is {t1} ")