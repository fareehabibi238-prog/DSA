def fun(nums):
     arr=[]
     for i in nums:
        for n in str(i):
            arr.append(int(n))
     return arr
print(fun([13,25,83]))        