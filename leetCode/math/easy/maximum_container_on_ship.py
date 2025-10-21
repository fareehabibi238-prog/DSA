def fun(n,w,maxWeight):
    x=maxWeight//w
    if x<n*n:
        print(x)
    else:
        print(n*n)
print(fun(2,3,15))