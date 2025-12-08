ranks = [13,2,3,1,9]
suits = ["a","a","a","a","a"]  
if len(set(suits)) == 1:
      print("Flush")
freq={}
for i in ranks:
    if i not in freq:
        freq[i] = 0
    freq[i] += 1
for count in freq.values():
    if count >= 3:
        print( "Three of a Kind")
for count in freq.values():
    if count==2:
        print( "Pair") 
print( "High Card")