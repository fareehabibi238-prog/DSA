def fun(nums):
  freq={}
  arr=[]
  for i in nums:
    if i in freq:
      freq[i]+=1
      arr.append(i)
    else:
      freq[i]=1
  print(arr)
print(fun([7,1,5,4,3,4,6,0,9,5,8,2]))