def fun(num):
    count=0
    while num>=10:
        digit_sum = sum(int(d) for d in str(num))
        count += 1
    return count
print(fun(48))