def fun(nums):
    nums.sort()
    arr=[]
    for i in range(0,len(nums),2):
        Alice=nums[i]
        bob=nums[i+1]
        arr.append(bob)
        arr.append(Alice)
    print(arr)
print(fun([3,5,4,2]))