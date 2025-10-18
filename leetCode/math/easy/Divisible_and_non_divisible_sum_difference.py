def fun(n,m):
 total_sum=(n*(n+1))//2
 k=n//m
 div_sum=m*(k*(k+1))//2
 answer=total_sum-div_sum
 j=answer-div_sum
 print(j)
print(fun(10,3))