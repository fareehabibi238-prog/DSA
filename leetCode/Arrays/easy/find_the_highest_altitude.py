gain=[-4,-3,-2,-1,4,3,2]
x=0
high=0
for i in gain:
    x=i+x
    high=max(high,x)
print(high)