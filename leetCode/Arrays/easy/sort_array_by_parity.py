def fun(nums):
   even=[x for x in nums if x%2==0]
   odd=[x for x in nums if x%2 !=0]
   return even+odd
print(fun([3,1,2,4]))