def fun(n):
  array=[]
  while n>0:
    if (n%3==0) or (n%5==0) or (n%7==0):
      array.append(n)
    n-=1
  print(sum(array))
print(fun(10)) 