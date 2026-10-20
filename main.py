def calculategmean(a,b):
    if a>b:
        print("1st number is greater")
    elif a<b:
        print("2nd number is greater ")
    else:
        print("both are equal")
    gmean=(a*b)/(a+b)
    print(gmean)
    
calculategmean(9,8)
calculategmean(8,10)




