def fun(nums,k):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                if (i*j)%k==0:
                    count+=1
    print(count)
print(fun([1,2,3,4],1))