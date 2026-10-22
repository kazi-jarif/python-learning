def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number : "))
print(factorial(n))


def fibanachi(fn):
    if fn==0 or fn==1:
        return fn
    else:
        ans=fibanachi(fn-1)+fibanachi(fn-2)
        return ans
fn=int(input("enter the number : "))
for i in range(int(fn+1)):
    print(fibanachi(i), end=" ")