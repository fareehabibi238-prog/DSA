def arraySign(nums):
    x=1
    for i in nums:
        x*=i
    if x==0:
        return 0
    if x>0:
        return 1
    if x<0:
        return -1
print(arraySign([-1,-2,-3,-4,3,2,1]))