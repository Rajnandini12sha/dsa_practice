a=0
b=1
n=10
c=0
d=[a,b]
for i in range(0,n-2):
  c=b+c
  b=d[i+1]
  d.append(c)
print(d)