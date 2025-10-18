def fun(n):
  x=2
  while True:
    if x%2==0 and x%n==0:
      return x
    x+=1
print(fun(5))