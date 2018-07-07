from datetime import timedelta
i=int(input())
a=str(timedelta(minutes=i))[:-3]
print(a)
