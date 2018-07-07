a=int(input())
b=list()
i=0
for i in range(a):
x=int(input())
b.insert(i,x)
i=i+1
print(b)
c=sum(b)
print(c)
median=c/len(b)
print(median)
