def fun(nums):
   even=[x for x in nums if x%2==0]
   odd=[x for x in nums if x%2 !=0]
   evi=0
   odi=0
   result=[]
   for i in range(len(nums)):
      if i %2==0:
         if evi<len(even):
            result.append(even[evi])
            evi+=1
         else:
           if odi<len(odd):
             result.append(odd[odi])
             odi+=1
      else:
             if i %2 !=0:
               if odi<len(odd):
                 result.append(odd[odi])
                 odi+=1
               else:
                  if evi<len(even):
                     result.append(even[evi])
                     evi+=1
   print(result) 
print(fun([3,1,2,4]))