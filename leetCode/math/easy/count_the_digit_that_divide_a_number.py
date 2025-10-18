def fun(num):
 count=0
 for val in str(num):
   val=int(val)
   if val !=0 and num%val==0:
      count+=1
 print(count)
print(fun(7))