def fun(nums):
    numStr=list(str(nums))
    for i in range(len(numStr)):
        if numStr[i]=='6':
            numStr[i]='9'
            break
    return int("".join(numStr))
print(fun(9669))