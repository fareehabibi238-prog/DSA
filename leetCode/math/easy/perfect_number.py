def fun(num):
   if num<=1:
       return False
   count=0
   for i in range(1,num):
       if num%i==0:
           count+=i
   return num==count
print(fun(7))
        