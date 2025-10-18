def fun(num):
  single=[]
  double=[]
  for i in num:
    if i <10:
      single.append(i)
    else:
      double.append(i)
  if sum(single)==sum(double):
    return False
  else:
    return True
print(fun([1,2,3,4,5,14]))