def fun(num):
  rev=int(str(num)[::-1])
  rev2=int(str(rev)[::-1])

  if num==rev2:
    return True
  else:
    return False
print(fun(1800)) 
