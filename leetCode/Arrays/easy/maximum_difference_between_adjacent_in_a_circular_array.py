nums = [2,1,0]
arr=[]
for i in range(len(nums)-1):
    x=abs(nums[i]-nums[i+1])
    arr.append(x)
m=abs(nums[-1]-nums[0])
arr.append(m)
print(max(arr))