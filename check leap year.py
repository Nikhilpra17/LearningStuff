# check leap year


a= int(input("Enter the year: "))

if (a%4) !=0 or (a%400)!=0:
    print (f"{a} is not a Leap Year")
else:
    print (f"{a} is a Leap Year")