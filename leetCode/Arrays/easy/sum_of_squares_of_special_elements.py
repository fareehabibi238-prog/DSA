def fun(nums):
    x=0
    for i in range(1,len(nums)+1):
        if len(nums)%i==0:
            x+=nums[i-1]**2
    print(x)
print(fun([2,7,1,19,18,3]))