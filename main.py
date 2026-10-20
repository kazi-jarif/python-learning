#default argument
def names(sirname="kazi",name="jarif"):
    print("the name is",sirname , name)
names(name="rana")
names()
names(name="rakib")



#Arbitrary Positional Arguments
def average(*num):
    #num named tupple has been created with peramitter number.Like (2,3).
    sum=0
    for i in num:
        sum=sum+i
    print(sum/len(num))
average(2,3)



#return statement
def average(*num):
    #num named tupple has been created with peramitter number.Like (2,3).
    sum=0
    for i in num:
        sum=sum+i
    return (sum/len(num))
c=average(2,3)
print(c)