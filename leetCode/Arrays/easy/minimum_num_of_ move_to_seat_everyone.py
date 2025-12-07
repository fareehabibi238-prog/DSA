seats = [3,1,5]
students = [2,7,4]
x=sorted(seats)
y=sorted(students)
count=0
for i in range(len(seats)):
     m=abs(x[i]-y[i])  
     count+=m
print(count)