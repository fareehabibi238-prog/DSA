def fun(allowed,words):
    allowedSet=set(allowed)
    count=0
    for word in words:
        consistent=True
        for ch in word:
            if ch not in allowedSet:
                consistent=False
                break
        if consistent:
            count+=1
    return count
print(fun( "ab",["ad","bd","aaab","baa","badab"]))