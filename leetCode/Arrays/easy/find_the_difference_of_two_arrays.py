nums1 = [1,2,3,3]
nums2 = [2,4,6,4]
nums1=list(set(nums1))
nums2=list(set(nums2))
arr1=[]
arr2=[]
for i in range(len(nums1)):
    if nums1[i] not in nums2:
        arr1.append(nums1[i])
for i in range(len(nums2)):
    if nums2[i] not in nums1:
        arr2.append(nums2[i])
print([arr1,arr2])