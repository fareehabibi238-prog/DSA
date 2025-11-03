string="leet code"
broken="lt"
count = 0
words = string.split()
for word in words:
    if not any(ch in word.lower() for ch in broken):
        count += 1
print(count)