""" You have an array of floating point numbers averages which is initially empty.
You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages. """
def fun(nums):
    arr=[]
    x=len(nums)//2
    while x:
        m=min(nums)
        n=max(nums)
        avg=(m+n)/2
        arr.append(avg)
        nums.remove(m)
        nums.remove(n)
        x-=1
    print(min(arr))
print(fun([7,8,3,4,15,13,4,1]))
        