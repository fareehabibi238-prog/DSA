#1 Divisible and non divisible sum difference
""" def fun(n,m):
 total_sum=(n*(n+1))//2
 k=n//m
 div_sum=m*(k*(k+1))//2
 answer=total_sum-div_sum
 j=answer-div_sum
 print(j)
print(fun(10,3)) """

#2 convert the temprature
""" def fun(celsius):
    array=[]
    kelvin=celsius + 273.15
    fehrenheit=celsius*1.80+32.00
    array.append(kelvin,)
    array.append(fehrenheit)

    return array
print(fun(36.50)) """


#3 number of good pairs
""" def fun(nums):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                count+=1
    return count
print(fun([1,2,3,1,1,3])) """


#4 Find the closet person
""" def fun(x,y,z):
    count=0
    count2=0
    while x<z or y>z:
      if x<z:
        x+=1
        count+=1
      if y>z:
        y-=1
        count2+=1
    while y<z or x>z:
      if y<z:
        y+=1
        count2+=1
      if x>z:
        x-=1
        count+=1
    if count<count2:
        return 1
    elif count>count2:
        return 2
    else:
        return 0
print(fun(10,1,12))
 """



#5 find minimum opreations to make all elements divisible by 3
""" arr=[1,2,3,4]
count=0
for i in arr:
  if i%3 !=0:
    count+=1
print(count) """


#6 The two sneaky numbers of digitiville

""" def fun(nums):
  freq={}
  arr=[]
  for i in nums:
    if i in freq:
      freq[i]+=1
      arr.append(i)
    else:
      freq[i]=1
  print(arr)
print(fun([7,1,5,4,3,4,6,0,9,5,8,2])) """



#7 smallest even multiple
""" def fun(n):
  x=2
  while True:
    if x%2==0 and x%n==0:
      return x
    x+=1
print(fun(5)) """


#8 add two integers
""" def fun(num1,num2):
    n=num1+num2
    print(n)
print(fun(3,5)) """



# 9 subtract the product and sum of digits of an integers
""" def fun(n):
 m=(str(n))
 x=1
 l=0
 for i in str(n):
   x*=int(i)
   l+=int(i)
 return int(x-l)
print(fun(125)) """




#10 count the matches of tournament
""" def fun(n):
 count=0
 while n>1:
   if n%2==0:
     n=n//2
     count+=n
   else:
     n=(n-1)//2
     count+=n
     n+=1
 return count 
print(fun(7)) """