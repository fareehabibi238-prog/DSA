def fun(nums):
   return min(sum(int(d) for d in str(n)) for n in nums)
print(fun([100,99,20]))