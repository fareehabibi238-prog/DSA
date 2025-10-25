def fun(nums):
    result=[]
    for i in range(len(nums)):
        count=0
        for j in nums:
            if j<nums[i]:
                count+=1
        result.append(count)
    return result
print(fun([8,1,2,2,3]))