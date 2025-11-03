nums=[2,2,3,3]
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for j in freq:
    if freq[j]==(len(nums)//2):
      print(j)  