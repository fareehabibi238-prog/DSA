s="abc"
t="bca"
x=0
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] in t[j]:
            x+=abs(i-j)
print(x) 