def fun(nums):
 count=0
 for i in nums:
    x=str(i)
    if len(x)%2==0:
        count+=1
 return count
print(fun([12,345,2,6,7896]))