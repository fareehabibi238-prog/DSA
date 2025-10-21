def fun(nums):
     x=min(nums)
     y=max(nums)
     arr=[]
     for i in range(1,x+1):
        if x%i==0 and y%i==0:
            arr.append(i)
     print(max(arr))
print(fun([2,3,4,5,6,10]))