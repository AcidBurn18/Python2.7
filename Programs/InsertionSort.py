def insertionsort(y):
    for i in range(1,len(y)):
        v=y[i]
        j=i
        while y[j-1]>v and j>=1:
            y[j]=y[j-1]
            j=j-1
        y[j]=v
x=[1,5,84,68,20,58,47,3,3]
insertionsort(x)
print x
