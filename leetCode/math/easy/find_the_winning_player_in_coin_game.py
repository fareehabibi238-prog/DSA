def fun(x,y):
    moves=min(x,y//4)
    if moves%2 !=0:
        return "Alice"
    else:
        return "Bob"
print(fun(4,10))