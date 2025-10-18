def fun(x):
  n=0
  for i in str(x):
    n+=int(i)
  if x%n==0:
    return n
  else:
    return -1
print (fun(18)) 
