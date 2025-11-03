def fun(n):
    x=7
    w=1
    y=0
    while n>0:
     for i in range(w,x+1):
            print(i)
            y+=i
            n-=1
            if n==0:
               break
     if n>0:
        w+=1
        x+=1
              
    print(y)
print(fun(10))