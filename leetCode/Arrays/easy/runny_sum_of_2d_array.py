def fun(nums):
    arr=[]
    count=0
    for i in nums:
        count+=i
        arr.append(count)
    return arr
print(fun( [1,2,3,4]))
        