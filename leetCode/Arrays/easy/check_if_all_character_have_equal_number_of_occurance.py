freq={}
s="aabb"
for char in s:
    if char in freq:
            freq[char]+=1
    else:
            freq[char]=1
print(len(set(freq.values()))==1)       