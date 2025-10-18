def fun(arr):
  x=0
  m=sum(arr)
  for a in arr:
    for i in str(a):
      x+=int(i)
  print(m-x)
print(fun([1,15,6,3]))