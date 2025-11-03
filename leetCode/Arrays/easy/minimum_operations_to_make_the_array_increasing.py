def fun(nums):
    count=0
    for i in range(len(nums)-1):
        if nums[i]>=nums[i+1]:
            x=nums[i]-nums[i+1]+1
            nums[i+1]+=x
            count+=x  
    print(count)
print(fun([1,5,2,4,1]))