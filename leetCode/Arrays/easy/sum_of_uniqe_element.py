def fun(nums):
    freq={}
    count=0
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for x in freq:
        if freq[x]==1:
            count+=x
    print(count)
print(fun([1,2,3,2]))