
def fun(nums):
    position=0
    count=0
    for num in nums:
        position+=num
    if position==0:
        count+=1
    print(count)
print(fun([3,2,-3,-4]))