nums=[11,7,2,15]
mn=min(nums)
mx=max(nums)
count=0
for x in nums:
    if mn<x<mx:
        count+=1
print(count)