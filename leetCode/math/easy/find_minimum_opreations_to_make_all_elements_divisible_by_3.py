def fun(nums):
 count=0
 for i in nums:
   if i%3 !=0:
     count+=1
 print(count)
print(fun([1,2,3,4]))