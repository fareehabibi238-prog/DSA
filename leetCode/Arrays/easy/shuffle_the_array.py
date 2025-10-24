def fun(num):
    arr=[]
    midn=len(num)//2
    left=num[:midn]
    right=num[midn:]
    leftn=0
    rightn=0
    for i in range(len(num)):
        if i%2==0:
            if leftn<len(left):
                arr.append(left[leftn])
                leftn+=1
        else:
            if rightn<len(right):
                arr.append(right[rightn])
                rightn+=1
    print(arr)
print(fun([5,2,1,3,6,7]))
    