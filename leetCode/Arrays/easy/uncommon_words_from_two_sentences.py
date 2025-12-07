s1 = "this apple is sweet"
s2 = "this apple is sour"
freq={}
for i in s1.split():
    freq[i]=freq.get(i,0)+1
for i in s2.split():
    freq[i]=freq.get(i,0)+1
    
result=[]
x=set(s1.split())
y=set(s2.split())
for i, b in freq.items():
    if b==1 and not(i in x and i in y):
        result.append(i)
print(result)