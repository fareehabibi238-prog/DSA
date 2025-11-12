nums=[1,13,10,12,31]
rev=[int(str(num)[::-1]) for num in nums]
nums.extend(rev)
print(len(set(nums)))