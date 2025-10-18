def fun(n):
 m=(str(n))
 x=1
 l=0
 for i in str(n):
   x*=int(i)
   l+=int(i)
 return int(x-l)
print(fun(125)) 
