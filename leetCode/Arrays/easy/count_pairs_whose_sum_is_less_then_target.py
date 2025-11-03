def fun(nums,target):
    nums.sort()
    count = 0
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1

    return count

print(fun([-10,-6,6,-3,10,-6,4,-8],-9))