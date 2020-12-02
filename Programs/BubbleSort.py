def bubblesort(y):
    x=list(y)
    for num in range(len(x)-1):
        i=0
        while i <len(x)-1:
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
            i+=1
    return x
s=bubblesort("987543025")
print s
