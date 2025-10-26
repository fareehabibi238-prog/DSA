def fun(nums):
     freq={}
     for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
     for n in freq:
        if freq[n]==1:
            return n
print(fun([1,2,2,1,4]))