a=int(input())
b=list()
i=0
for i in range(a):
x=int(input())
b.insert(i,x)
i=i+1
print(b)
for index,c in enumerate(b):
print(c,index)
