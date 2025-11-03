def fun(s,indices):
    m=[]
    result=[""]*len(s)
    for i in range(len(s)):
        result[indices[i]]=s[i]
    m="".join(result)
    print(m)
print(fun("codeleet", [4,5,6,7,0,2,1,3]))