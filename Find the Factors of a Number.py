#Find the Factors of a Number

def factors(a):
    qaaa= []
    for i in range (1, a+1):
        if a % i ==0:
            qaaa.append(i)
    print (qaaa)

    

e = 42
factors(e)