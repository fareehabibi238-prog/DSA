def fun(nums):
    a,b,c=nums
    if a+b <=c or a+c<=b or c+b<=a:
        return "none"
    if a==b==c:
        return "equilateral"
    elif a==b or b==c or a==c:
        return "isosceles"
    else:
        return "scalene"
print(fun([3,3,3]))