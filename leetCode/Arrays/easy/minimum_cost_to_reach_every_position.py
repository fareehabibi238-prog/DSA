cost=[5,3,4,1,3,2]
for i in range(len(cost)-1):
    if cost[i]<cost[i+1]:
        x=cost[i+1]-cost[i]
        cost[i+1]-=x
print(cost)