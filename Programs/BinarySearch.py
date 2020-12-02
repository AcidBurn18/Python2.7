x=raw_input("Enter the word to be Searched:= ")
low=0
y="abcdefghijklmnopqrstuvwxyz"
l=list(y)
high=len(y)-1
mid=0
for i in l:
    mid=(low+high)/2
    if l[mid]>x:
        high=mid-1
      
    else:
        low=mid+1
print "Yeah it Exist"
print "In
