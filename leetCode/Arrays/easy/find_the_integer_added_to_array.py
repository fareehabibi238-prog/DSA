def fun(nums1,nums2):
    nums1.sort()
    nums2.sort()
    x = nums2[0] - nums1[0]
    # Optional check:
    if all(a + x == b for a, b in zip(nums1, nums2)):
        return x
    else:
        raise ValueError("No consistent integer x makes nums1 equal to nums2.")

print(fun([2,6,4], [9,7,5]))