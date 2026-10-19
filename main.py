for i in range(10):
    if (i+1)==5:
        break
    else:
        print("5 X ",i+1,"=",5*(i+1))
print("it will end in 5")



for i in range(10):
    if (i+1)==5:
        continue
    print("5 X ",i+1,"=",5*(i+1))
print("it will ignore in 5")



i=0
while True:
    i=i+1
    if i%10==0:
        continue
    print(i)
    
