def fun(nums,k):
    freq = {}
    count = 0
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in nums:
        if freq[i] % k == 0:
            count += i
    print(count)
print(fun([1,2,3,2],2))