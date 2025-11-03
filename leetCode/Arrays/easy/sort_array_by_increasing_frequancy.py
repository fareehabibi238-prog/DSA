nums=[1,1,2,2,2,3]
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
nums.sort(key=lambda x:(freq[x] ,-x))
print(nums)