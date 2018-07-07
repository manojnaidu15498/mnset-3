from datetime import timedelta
i1=int(input())
a=str(timedelta(minutes=i1))[:-3]
i2=int(input())
b=str(timedelta(minutes=i2))[:-3]
ans=i2-i1
diff=b=str(timedelta(minutes=ans))[:-3]
print(diff)
